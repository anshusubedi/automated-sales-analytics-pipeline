import pandas as pd
from scipy import stats
from src.extract import load_raw_data
from src.transform import clean_data

def run_statistical_analysis(df):
    # Filter for the two categories
    cat1 = df[df['Product Category'] == 'electronics']['Total Amount']
    cat2 = df[df['Product Category'] == 'clothing']['Total Amount']
    
    # Perform t-test
    t_stat, p_value = stats.ttest_ind(cat1, cat2)
    
    print(f"--- Statistical Analysis ---")
    print(f"Comparison: Electronics vs Clothing")
    print(f"T-statistic: {t_stat:.4f}")
    print(f"P-value: {p_value:.4f}")
    
    if p_value < 0.05:
        print("Result: The difference in spending is STATISTICALLY SIGNIFICANT.")
    else:
        print("Result: The difference in spending is NOT statistically significant.")