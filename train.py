from pipeline.preprocess import preprocess
from pipeline.validate import validate_columns  # ✅ Import validation
from sklearn.linear_model import LogisticRegression
import joblib
import os

def train_model(df):
    validate_columns(df)  # ✅ Validate schema before anything
    X, y = preprocess(df)
    model = LogisticRegression()
    model.fit(X, y)
    
    os.makedirs("model", exist_ok=True)
    joblib.dump(model, "model/model.pkl")
    print("✅ Model trained and saved.")
