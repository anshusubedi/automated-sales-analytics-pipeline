from src.extract import load_raw_data
from src.transform import clean_data
from src.analyze import run_statistical_analysis
from src.visualize import plot_sales_data # Add this import

def main():
    print("--- Pipeline Initiated ---")
    df = load_raw_data()
    if df is not None:
        df_cleaned = clean_data(df)
        run_statistical_analysis(df_cleaned)
        plot_sales_data(df_cleaned) # Add this line
        print("--- Pipeline Finished Successfully ---")

if __name__ == "__main__":
    main()