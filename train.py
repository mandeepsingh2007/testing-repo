import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier  # example model
from sklearn.metrics import accuracy_score
import sys
import os

# Define required columns (update as per your real dataset)
REQUIRED_COLUMNS = ['feature1', 'feature2', 'feature3', 'target']

def load_and_validate_csv(file_path):
    if not os.path.exists(file_path):
        print(f"❌ File not found: {file_path}")
        sys.exit(1)

    try:
        df = pd.read_csv(file_path)
    except Exception as e:
        print(f"❌ Failed to read CSV: {e}")
        sys.exit(1)

    # Find missing columns
    missing = [col for col in REQUIRED_COLUMNS if col not in df.columns]
    if missing:
        print(f"❌ Missing required columns: {missing}")
        sys.exit(1)

    # Warn about extra columns but continue
    extra = [col for col in df.columns if col not in REQUIRED_COLUMNS]
    if extra:
        print(f"⚠️ Warning: Extra columns found (will be ignored): {extra}")

    # Keep only required columns and in correct order
    df = df[REQUIRED_COLUMNS]

    return df

def train_model(df):
    # Separate features and target
    X = df.drop('target', axis=1)
    y = df['target']

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Example: Random Forest
    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)

    # Evaluate
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    print(f"✅ Training complete. Accuracy on test set: {acc:.4f}")

    return model

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python train.py <csv_file>")
        sys.exit(1)

    csv_file = sys.argv[1]
    df = load_and_validate_csv(csv_file)
    model = train_model(df)
