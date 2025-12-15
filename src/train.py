import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import joblib
from pathlib import Path


DATA_PATH = "data/KDDTrain+Multi.csv"
MODEL_PATH = "models/threat_detector_rf.pkl"
LABEL_COL = "class"


def load_data(filepath):
    df = pd.read_csv(filepath)
    if LABEL_COL not in df.columns:
        raise ValueError(f"Label column '{LABEL_COL}' not found in dataset")
    return df


def train_model(df):
    X = df.drop(LABEL_COL, axis=1)
    y = df[LABEL_COL]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    model = RandomForestClassifier(
        n_estimators=100,
        random_state=42,
        n_jobs=-1
    )

    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    print("\nClassification Report:\n")
    print(classification_report(y_test, y_pred))

    return model


def save_model(model, path):
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, path)
    print(f"[+] Model saved to {path}")


if __name__ == "__main__":
    df = load_data(DATA_PATH)
    model = train_model(df)
    save_model(model, MODEL_PATH)
