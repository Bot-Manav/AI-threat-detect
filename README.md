# 🚨 AI-Driven Threat Detection & Prioritization

---

## 👥 **TEAM MEMBERS**  
- Garach Viraj  
- Vaghasiya Jil  
- Dedakiya Manav  

---

## 📜 **Disclaimer**  
*This project uses the publicly available AI model, which is licensed under the MIT License (see [here](https://github.com/mahaswetaroy1/cybersecurity-threat-ai.git)). The model was pre-trained and integrated into this project. All other components, features, and implementation were developed during the hackathon.*

---

## 📌 **Project Overview**  
Security teams face an overwhelming number of alerts from monitoring systems, leading to **alert fatigue** and the risk of missing critical threats. This project aims to build an **AI-powered system** that intelligently detects, prioritizes, and scores threats in real-time to help cybersecurity teams respond effectively.

The system processes network data, applies machine learning algorithms, and presents actionable insights through a web interface for visualization, alert management, and tracking.

---

## 📂 **Features**

✅ **Real-time anomaly detection**  
✅ **Threat scoring and prioritization** based on risk levels  
✅ **Interactive dashboard** for visual insights and alert management  
✅ **Machine learning models** including Random Forest, XGBoost, and Neural Networks  
✅ **Data preprocessing pipelines** for handling imbalanced datasets  
✅ **Model explainability and reporting** using feature importance and visualization  
✅ **Secure environment setup** with `.env` configuration  
✅ **Scalable and modular architecture** for integration with other systems  

---

## Feature trying
for trying how to get this in your website visit : https://github.com/0Manav0/AI-threat-detect-2.git

## 🚀 **Installation**

### ✅ Prerequisites
- Python 3.11 or above  
- `pip` installed  
- Virtual environment tool (`venv` recommended)

### ✅ Steps

**1️⃣ Clone the repository:**
```bash
git clone https://github.com/0Manav0/AI-threat-detect.git
⚠ NOTE: YOU MUST SAVE THE MAIN (PARENT) FOLDER AS cybersecurity-threat-ai-main

2️⃣ Create and activate a virtual environment:

bash
Copy code
python -m venv venv
source venv/bin/activate    # For Linux/macOS
venv\Scripts\activate       # For Windows
3️⃣ Install the required dependencies:

bash
Copy code
pip install -r requirements.txt
4️⃣ Set up environment variables:

bash
Copy code
python -m venv venv
source venv/bin/activate    # For Linux/macOS
venv\Scripts\activate       # For Windows
🟠 Step-by-Step Usage
A. Preprocess the Data
Converts ARFF to CSV, applies label encoding.

bash
Copy code
python src\preprocess.py
B. Train the Model
Trains a Random Forest classifier on the preprocessed data.

bash
Copy code
python src\train.py
C. Test the Model Locally (Optional)
bash
Copy code
python src\predict.py
D. Deploy the API
Runs the Flask server for real-time predictions.

bash
Copy code
python src\deploy.py
➡ After that, visit: http://127.0.0.1:5000, pick your request in the form, and submit.

📁 Project Structure
csharp
Copy code
cybersecurity-threat-ai-main/
├── models/                # Trained ML models
├── data/                  # Input datasets (unzip required)
├── templates/             # HTML templates
├── static/                # CSS, JS, and images
├── src/                   # Python files of AI (deploy.py, train.py, predict.py, preprocess.py)
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation
├── .gitignore             # Git ignore file
⚠ SPECIAL NOTE:
Please place preprocessing-checkpoint.ipynb and all .ipynb files inside a folder named .ipynb_checkpoints. Also, unzip the data folder and check for duplicates in it. Sorry for the inconvenience!

📖 How It Works
🔍 Data Ingestion
Network data logs or synthetic datasets are loaded, cleaned, and preprocessed.

📊 Feature Engineering
Important features like traffic rate, protocol behavior, and historical patterns are calculated.

🤖 Model Training
Algorithms like Random Forest, XGBoost, and Neural Networks are trained on labeled data.

🚨 Anomaly Detection
Incoming data is scored based on the trained models to detect suspicious activity.

⚡ Alert Prioritization
Alerts are ranked based on severity using statistical thresholds and model output.

📈 Visualization
A web dashboard displays charts, graphs, and logs to help analysts make informed decisions.

⚙ Usage
Run locally for testing and analysis.

Extend models with additional data or tuning parameters.

Deploy using gunicorn, Docker, or cloud platforms like AWS, GCP, or Heroku.

Integrate with other SIEM tools using APIs.
