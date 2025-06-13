REQUIRED_COLUMNS = {"age", "gender", "income", "purchased"}

def validate_columns(df):
    missing = REQUIRED_COLUMNS - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {missing}")
    print("✅ Column validation passed.")
