import streamlit as st
import pandas as pd
import os
import matplotlib.pyplot as plt
st.write(os.listdir())
df = pd.read_csv("nassau_candy.csv", on_bad_lines="skip", engine="python")

st.sidebar.title("📌 Project Overview")
st.markdown("### 👩‍💻 Created by Priyanka")
st.sidebar.info(
"""
Nassau Candy Distributor

Sales & Profit Analysis

Created using:
- Python
- Pandas
- Matplotlib
- Streamlit
"""
)
# Title
st.title("📊 Sales and Profit Analysis Dashboard")
st.write("Interactive Business Intelligence Dashboard developed using Python, Pandas, Matplotlib and Streamlit.")
total_sales = df["Sales"].sum()

total_profit = df["Gross Profit"].sum()

total_orders = len(df)
col1, col2, col3 = st.columns(3)

col1.metric("💰 Total Sales", f"{total_sales:.2f}")

col2.metric("📈 Total Profit", f"{total_profit:.2f}")

col3.metric("Total Orders", total_orders)
st.divider()

st.markdown("""
### 📖 Project Description

This dashboard analyzes the sales and profit performance of Nassau Candy Distributor.

The main objectives are:

- Analyze overall sales performance
- Calculate profit margin
- Identify Top 10 Most Profitable Products
- Analyze Division-wise Profit
- Analyze Region-wise Profit
- Visualize business insights using charts

This dashboard is developed using Python, Pandas, Matplotlib and Streamlit.
""")
st.divider()

st.markdown(
    "### Welcome to the Sales and Profit Analysis Dashboard 📈"
)
st.divider()
# Read the dataset
df = pd.read_csv("Nassau Candy Distributor.csv")

# Summary Boxes

total_sales = df["Sales"].sum()

total_profit = df["Gross Profit"].sum()

total_orders = len(df)

col1, col2, col3 = st.columns(3)

col1.metric("Total Sales", f"${total_sales:,.0f}")

col2.metric("Total Profit", f"${total_profit:,.0f}")

col3.metric("Total Orders", total_orders)


# Dataset Shape
st.header("📊 Dataset Shape")
st.write(df.shape)
st.divider()

# First 5 Rows
st.header("📋 First 5 Rows")
st.write(df.head())
st.divider()

# Profit Margin
df["Profit Margin %"] = (df["Gross Profit"] / df["Sales"]) * 100

st.header("💰 Profit Margin")
st.write(
    df[
        ["Product Name", "Sales", "Gross Profit", "Profit Margin %"]
    ].head()
)
st.divider()

# Top 10 Most Profitable Products
top_products = (
    df.groupby("Product Name")["Gross Profit"]
    .sum()
    .sort_values(ascending=False)
)

st.header("🏆 Top 10 Most Profitable Products")
st.write(top_products.head(10))
fig, ax = plt.subplots(figsize=(10,5))

ax.bar(
    top_products.head(10).index,
    top_products.head(10).values
)
ax.set_xlabel("Product Name")
ax.set_ylabel("Gross Profit")

plt.xticks(rotation=90)
plt.tight_layout()

st.pyplot(fig)

st.divider()

# Division-wise Profit
division_profit = (
    df.groupby("Division")["Gross Profit"]
    .sum()
    .sort_values(ascending=False)
)

st.header("🏢 Division-wise Profit")
st.write(division_profit)
ax.bar(
    division_profit.index,
    division_profit.values
)

st.pyplot(fig)
st.divider()

# Region-wise Profit
region_profit = (
    df.groupby("Region")["Gross Profit"]
    .sum()
    .sort_values(ascending=False)
)

st.header("🌍 Region-wise Profit")
st.write(region_profit)
fig, ax = plt.subplots(figsize=(8,8))

ax.bar(
    region_profit.index,
    region_profit.values
)
st.pyplot(fig)
st.divider()
# Top 10 Products Chart

st.header("📈 Top 10 Most Profitable Products Chart")


fig, ax = plt.subplots(figsize=(10,5))

ax.bar(top_products.head(10).index,
       top_products.head(10).values)

plt.xticks(rotation=90)

st.pyplot(fig)
st.divider()
st.header("📌 Conclusion")

st.success("""
The dashboard successfully analyzes sales and profit performance,
identifies top products, and provides division-wise and region-wise insights.
""")
st.divider()
