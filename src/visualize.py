import matplotlib.pyplot as plt

def plot_sales_data(df):
    # Grouping data by category to get average total amount
    category_sales = df.groupby('Product Category')['Total Amount'].mean()
    
    # Create the bar chart
    plt.figure(figsize=(10, 6))
    category_sales.plot(kind='bar', color='skyblue')
    
    plt.title('Average Sales by Product Category')
    plt.xlabel('Category')
    plt.ylabel('Average Total Amount')
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    # Save the plot
    plt.savefig('sales_analysis_chart.png')
    print("Visualization saved as 'sales_analysis_chart.png'")