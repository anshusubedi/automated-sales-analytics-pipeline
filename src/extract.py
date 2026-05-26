import pandas as pd
import os

def load_raw_data():
    # This path tells Python to look inside the data/raw folder
    file_path = os.path.join("data", "raw", "retail_sales_dataset.csv")
    
    if not os.path.exists(file_path):
        print(f"Error: Could not find file at {file_path}")
        return None
    
    print(f"Loading data from: {file_path}")
    return pd.read_csv(file_path)

if __name__ == "__main__":
    # This block runs only when you run this script directly
    df = load_raw_data()
    if df is not None:
        print(f"Success! The dataset has {len(df)} rows.")
        print(df.head()) # Shows the first 5 rows