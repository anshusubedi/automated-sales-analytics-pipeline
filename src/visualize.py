import matplotlib.pyplot as plt
import os

def plot_sales_data(df):
    # Ensure a directory for outputs exists
    output_dir = 'outputs'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Grouping data by category to get average total amount
    # Note: Ensure your column name matches your CSV header exactly
    category_sales = df.groupby('Product Category')['Total Amount'].mean()
    
    # Create the bar chart
    plt.figure(figsize=(10, 6))
    category_sales.plot(kind='bar', color='skyblue')
    
    plt.title('Average Sales by Product Category')
    plt.xlabel('Category')
    plt.ylabel('Average Total Amount')
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    # Save the plot into the outputs folder
    save_path = os.path.join(output_dir, 'sales_analysis_chart.png')
    plt.savefig(save_path)
    print(f"Visualization saved as '{save_path}'")