import pandas as pd
from scipy.io import arff
from sklearn.preprocessing import LabelEncoder
from pathlib import Path


INPUT_ARFF = "data/full-d/KDDTrain+Multi.arff"
OUTPUT_CSV = "data/KDDTrain+Multi.csv"
LABEL_COL = "class"


def load_arff(filepath):
    """Load ARFF file and decode byte strings."""
    data, meta = arff.loadarff(filepath)
    df = pd.DataFrame(data)
    df = df.map(lambda x: x.decode() if isinstance(x, bytes) else x)
    return df


def preprocess_dataframe(df):
    """
    Encode categorical features and ensure label column consistency.
    """
    if LABEL_COL not in df.columns:
        raise ValueError(f"Required label column '{LABEL_COL}' not found in dataset")

    label_encoders = {}

    for col in df.columns:
        if df[col].dtype == "object":
            le = LabelEncoder()
            df[col] = le.fit_transform(df[col])
            label_encoders[col] = le

    return df, label_encoders


def save_csv(df, output_path):
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"[+] Preprocessed data saved to {output_path}")


if __name__ == "__main__":
    df = load_arff(INPUT_ARFF)
    df, encoders = preprocess_dataframe(df)
    save_csv(df, OUTPUT_CSV)
