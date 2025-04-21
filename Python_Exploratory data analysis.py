# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned dataset
df = pd.read_csv("cleaned_store_sales.csv")

# --- Visualization 1: Store Area vs. Sales ---
plt.figure(figsize=(10, 6))
sns.scatterplot(
    x='Store_Area', 
    y='Store_Sales', 
    data=df,
    hue='High_Sales_Flag',  # Color-code high-sales stores
    palette={0: 'gray', 1: 'blue'}
)
plt.title("Store Area vs. Sales (High-Sales Stores Flagged)", fontsize=14)
plt.xlabel("Store Area (sq. ft.)", fontsize=12)
plt.ylabel("Daily Sales ($)", fontsize=12)
plt.grid(True)
plt.show()

# --- Visualization 2: Sales Efficiency by High-Sales Flag ---
plt.figure(figsize=(10, 6))
sns.boxplot(
    x='High_Sales_Flag', 
    y='Sales_per_SqFt', 
    data=df,
    palette="Set2"
)
plt.title("Sales per SqFt by High-Sales Flag", fontsize=14)
plt.xlabel("High Sales Flag (1 = High Sales)", fontsize=12)
plt.ylabel("Sales per SqFt ($)", fontsize=12)
plt.xticks([0, 1], ["Low Sales", "High Sales"])
plt.show()

# --- Key Finding Calculation: 25% Higher Sales in Large Stores ---
large_stores = df[df['Store_Area'] > 1500]
avg_sales_large = large_stores['Store_Sales'].mean()

small_stores = df[df['Store_Area'] <= 1500]
avg_sales_small = small_stores['Store_Sales'].mean()

sales_increase = ((avg_sales_large - avg_sales_small) / avg_sales_small) * 100
print(f"Sales increase in large stores (>1500 sq. ft.): {sales_increase:.1f}%")