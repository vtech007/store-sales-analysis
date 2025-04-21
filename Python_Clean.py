# Install dependencies (if needed)
# !pip install pandas numpy seaborn

import pandas as pd
import numpy as np

# Load raw data
df = pd.read_csv("Stores.csv")  # Downloads

# Step 1: Handle missing values (impute median)
df['Daily_Customer_Count'].fillna(df['Daily_Customer_Count'].median(), inplace=True)

# Step 2: Remove outliers (sales > 200k)
df = df[df['Store_Sales'] <= 200000]

# Step 3: Feature engineering
df['Sales_per_SqFt'] = df['Store_Sales'] / df['Store_Area']
df['Customer_Density'] = df['Daily_Customer_Count'] / df['Store_Area']
df['High_Sales_Flag'] = np.where(df['Store_Sales'] > 150000, 1, 0)

# Step 4: Validate data integrity
assert df['Store_Sales'].min() >= 0, "Negative sales found!"
assert df['Items_Available'].max() <= 3000, "Invalid item count!"

# Step 5: Save cleaned data
df.to_csv("cleaned_store_sales.csv", index=False)

print("Cleaned dataset saved as 'kleand_store_sales.csv'")