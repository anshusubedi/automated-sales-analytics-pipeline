import pandas as pd

def clean_data(df):
    df['Date'] = pd.to_datetime(df['Date'])
    missing_count = df.isnull().sum().sum()
    print(f"Cleaning complete. Found {missing_count} missing values.")
    df['Product Category'] = df['Product Category'].str.lower()
    return df