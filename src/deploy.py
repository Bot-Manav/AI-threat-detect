from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import pandas as pd
import joblib
import secrets
import os
from datetime import datetime

# Store all predictions here
PREDICTION_HISTORY = []
app = Flask(__name__, template_folder="../templates", static_folder="../static")
app.secret_key = secrets.token_hex(16)  # Use a secure random string in production

# Load the trained model
MODEL_PATH = "models/threat_detector_rf.pkl"
if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(f"Model file not found at {MODEL_PATH}")
model = joblib.load(MODEL_PATH)

# Automatically get feature names from the model
FEATURE_COLUMNS = list(model.feature_names_in_)

@app.route("/")
def index():
    return render_template("index.html", feature_columns=FEATURE_COLUMNS)

history_data = []

@app.route("/explanation")
def explanation():
    try:
        explanation_data = session.pop('explanation', None)
        if explanation_data is None:
            explanation_data = {
                'prediction': 0,
                'confidence': 0.0,
                'explanation': "No input provided yet.",
                'features': ["Please submit the form to see the explanation."],
                'warning': ""
            }
        return render_template("explanation.html",
                               prediction=explanation_data['prediction'],
                               confidence=explanation_data['confidence'],
                               explanation=explanation_data['explanation'],
                               features=explanation_data['features'],
                               warning=explanation_data['warning'])
    except Exception as e:
        return f"An error occurred: {str(e)}"

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()
        df = pd.DataFrame([data])
        pred, conf = model_predict(df)

        # Generate simple rule-based issues (optional: add more)
        issues = []
        if data.get("num_failed_logins", 0) > 3:
            issues.append("Multiple failed login attempts detected.")
        if data.get("root_shell", 0) == 1:
            issues.append("Root shell access detected.")
        if data.get("su_attempted", 0) > 0:
            issues.append("Switch user attempts detected.")
        if not issues:
            issues.append("No obvious threats detected.")

        # Add warning if prediction=1 and confidence > 0.55
        warning = ""
        if pred[0] == 1 and conf[0] > 0.55:
            warning = "⚠ Warning: High confidence threat detected!"

        # Store explanation in session
        session['explanation'] = {
            'prediction': int(pred[0]),
            'confidence': round(conf[0], 2),
            'explanation': "The system identified potential issues.",
            'features': issues,
            'warning': warning
        }

        # Store in prediction history
        if 'PREDICTION_HISTORY' not in session:
            session['PREDICTION_HISTORY'] = []
        session['PREDICTION_HISTORY'].append({
            'input': data,
            'prediction': int(pred[0]),
            'confidence': round(conf[0], 2),
            'issues': issues,
            'warning': warning
        })

        # Return JSON to JS
        return jsonify({
            "success": True,
            "prediction": pred.tolist(),
            "confidence": conf.tolist(),
            "issues": issues,
            "warning": warning
        })

    except Exception as e:
        return jsonify({"error": str(e)})

@app.route("/history")
def history():
    past_data = session.get('PREDICTION_HISTORY', [])
    return render_template("history.html", past_data=past_data)

@app.route("/analytics")
def analytics():
    past_data = session.get('PREDICTION_HISTORY', [])
    timestamps = [i+1 for i in range(len(past_data))]  # simple counter as timestamp
    values = [d['prediction'] for d in past_data]
    confidences = [d['confidence'] for d in past_data]
    return render_template("analytics.html", timestamps=timestamps, values=values, confidences=confidences)


def model_predict(df):
    pred = model.predict(df)
    conf = model.predict_proba(df)[:, 1]
    return pred, conf

if __name__ == "__main__":
    app.run(debug=True)

