from pipeline.train import train_model
import pandas as pd

if __name__ == "__main__":
    df = pd.read_csv("data/train.csv")
    train_model(df)
