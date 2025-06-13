import pandas as pd

def preprocess(df):
    df = df.copy()
    df["gender"] = df["gender"].map({"Male": 0, "Female": 1})
    X = df[["age", "gender", "income"]]
    y = df["purchased"]
    return X, y
