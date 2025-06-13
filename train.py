from pipeline.preprocess import preprocess
from sklearn.linear_model import LogisticRegression
import joblib
import os

def train_model(df):
    X, y = preprocess(df)
    model = LogisticRegression()
    model.fit(X, y)
    
    os.makedirs("model", exist_ok=True)
    joblib.dump(model, "model/model.pkl")
    print("✅ Model trained and saved.")
