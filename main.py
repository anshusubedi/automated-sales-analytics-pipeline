from src.extract import load_raw_data
from src.transform import clean_data
from src.analyze import run_statistical_analysis

def main():
    print("--- Pipeline Initiated ---")
    df = load_raw_data()
    if df is not None:
        df_cleaned = clean_data(df)
        run_statistical_analysis(df_cleaned)
        print("--- Pipeline Finished Successfully ---")

if __name__ == "__main__":
    main()