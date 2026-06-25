import pandas as pd

# Read the dataset
df = pd.read_csv("nassau_candy.csv")

# Show first 5 rows
print("FIRST 5 ROWS")
print(df.head())

print("\n--------------------")

# Show column names
print("COLUMN NAMES")
print(df.columns)

print("\n--------------------")

# Basic information
print("DATASET SHAPE")
print(df.shape)


# Calculate Profit Margin %

df["Profit Margin %"] = (df["Gross Profit"] / df["Sales"]) * 100

print("\nPROFIT MARGIN %")

print(
    df[
        ["Product Name", "Sales", "Gross Profit", "Profit Margin %"]
    ].head()
)

# Top 10 Most Profitable Products

top_products = df.groupby("Product Name")["Gross Profit"].sum()

top_products = top_products.sort_values(ascending=False)

print("\nTOP 10 MOST PROFITABLE PRODUCTS")

print(top_products.head(10))

import matplotlib.pyplot as plt

# Create bar chart

top10 = top_products.head(10)

plt.figure(figsize=(10,6))

plt.bar(top10.index, top10.values)

plt.xticks(rotation=90)

plt.title("Top 10 Most Profitable Products")

plt.xlabel("Product Name")

plt.ylabel("Gross Profit")

plt.tight_layout()

plt.show()

# Division-wise Profit Analysis

division_profit = df.groupby("Division")["Gross Profit"].sum()

division_profit = division_profit.sort_values(ascending=False)

print("\nDIVISION-WISE PROFIT")

print(division_profit)

 #Division-wise Bar Chart

plt.figure(figsize=(8,5))

plt.bar(division_profit.index, division_profit.values)

plt.xticks(rotation=45)

plt.title("Division-wise Gross Profit")

plt.xlabel("Division")

plt.ylabel("Gross Profit")

plt.tight_layout()

plt.show()

# Region-wise Profit Analysis

region_profit = df.groupby("Region")["Gross Profit"].sum()

region_profit = region_profit.sort_values(ascending=False)

print("\nREGION-WISE PROFIT")

print(region_profit)

# Region-wise Profit Analysis

region_profit = df.groupby("Region")["Gross Profit"].sum()

region_profit = region_profit.sort_values(ascending=False)

print("\nREGION-WISE PROFIT")

print(region_profit)