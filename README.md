# 🚨 AI-Driven Threat Detection & Prioritization

---

## 👥 Team Members
- Garach Viraj  
- Vaghasiya Jil  
- Dedakiya Manav  

---

## 📜 Disclaimer
This project integrates a **publicly available AI model** licensed under the **MIT License**  
(reference implementation: https://github.com/mahaswetaroy1/cybersecurity-threat-ai.git).

The model was **pre-trained and adapted** for this system.  
All **architecture design, preprocessing pipelines, risk scoring logic, API integration, and dashboard components** were developed independently during the hackathon.

---

## 📌 Project Overview
Modern security teams face **alert fatigue** caused by massive volumes of logs and monitoring alerts, increasing the risk of missing critical threats.

This project presents an **AI-driven threat detection and prioritization system** that:
- Detects anomalous behavior in network traffic
- Assigns dynamic risk scores
- Prioritizes alerts based on severity
- Provides visual insights through a web dashboard

The goal is to improve **SOC efficiency**, **early threat detection**, and **decision-making clarity**.

---

## ✨ Key Features
- Real-time anomaly detection  
- Risk-based threat scoring and prioritization  
- Interactive web dashboard for monitoring and alerts  
- Machine learning models:
  - Random Forest
  - XGBoost
  - Neural Networks  
- Robust preprocessing pipeline for imbalanced datasets  
- Model explainability using feature importance  
- Secure configuration using environment variables  
- Modular and scalable architecture  

---

## 🔗 Demo / Integration Example
To see how this system can be integrated into a website or application, visit:  
https://github.com/0Manav0/AI-threat-detect-2.git

---

## 📊 Dataset Requirements & Format

### Supported Dataset Types
This system is **dataset-agnostic** and can be trained on:
- Network traffic datasets
- Intrusion detection datasets
- Security event or flow logs
- Synthetic or simulated attack traffic

Common public datasets suitable for this architecture include:
- CICIDS-style datasets  
- UNSW-NB15-like datasets  
- Lab-generated or simulated logs  

> ⚠ The original datasets used during development are **not included** due to privacy, security, and size considerations.

---

### Required Data Format
The preprocessing pipeline expects **tabular data** in **CSV or ARFF** format with features similar to the following:

| Feature Name     | Description |
|------------------|------------|
| `timestamp`      | Event or flow timestamp |
| `src_ip`         | Source IP address |
| `dst_ip`         | Destination IP address |
| `src_port`       | Source port |
| `dst_port`       | Destination port |
| `protocol`       | Network protocol (TCP, UDP, ICMP, etc.) |
| `packet_count`   | Number of packets |
| `byte_count`     | Number of bytes transferred |
| `flow_duration` | Duration of the network flow |
| `flag_counts`    | TCP flag statistics |
| `label`          | Normal / Attack (or attack category) |

✅ The **`label` column is mandatory** for supervised training.

---

### Data Preprocessing
The preprocessing pipeline includes:
- Label encoding of categorical features
- Handling missing or inconsistent values
- Class imbalance mitigation (oversampling / weighting)
- Feature normalization where required

Implemented in:

src/preprocess.py


---

### Using Your Own Dataset
1. Place the dataset inside the `data/` directory  
2. Ensure it follows the feature structure described above  
3. Run preprocessing:
```bash
python src/preprocess.py


Train the model:

python src/train.py


Trained models are automatically saved to:

models/

Synthetic & Test Data

For experimentation:

You may use synthetic datasets

Or simulated network traffic matching the schema

This allows testing without exposing real or sensitive data.

🚀 Installation & Setup
Prerequisites

Python 3.11+

pip

Virtual environment tool (venv recommended)

Installation Steps
1️⃣ Clone the repository
git clone https://github.com/0Manav0/AI-threat-detect.git
cd AI-threat-detect

2️⃣ Create and activate virtual environment
python -m venv venv
source venv/bin/activate      # Linux / macOS
venv\Scripts\activate         # Windows

3️⃣ Install dependencies
pip install -r requirements.txt

🟠 Usage Guide
A. Preprocess Data
python src/preprocess.py

B. Train the Model
python src/train.py

C. Test Predictions (Optional)
python src/predict.py

D. Deploy API
python src/deploy.py


➡ Visit: http://127.0.0.1:5000

Submit requests through the web interface.

📁 Project Structure
cybersecurity-threat-ai/
├── models/            # Trained ML models
├── data/              # Input datasets (user-provided)
├── templates/         # HTML templates
├── static/            # CSS, JS, assets
├── src/               # Core AI & API logic
│   ├── preprocess.py
│   ├── train.py
│   ├── predict.py
│   └── deploy.py
├── requirements.txt
├── README.md
├── .gitignore
└── LICENSE

📖 How It Works
🔍 Data Ingestion

Network or log data is loaded, cleaned, and normalized.

📊 Feature Engineering

Traffic behavior, protocol patterns, and statistical features are extracted.

🤖 Model Training

ML models learn patterns distinguishing normal and malicious activity.

🚨 Anomaly Detection

Incoming data is scored to detect suspicious behavior.

⚡ Alert Prioritization

Threats are ranked using model confidence and risk scoring logic.

📈 Visualization

A dashboard presents alerts, trends, and insights for analysts.
