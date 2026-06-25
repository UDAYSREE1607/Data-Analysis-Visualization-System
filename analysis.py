import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read CSV file
df = pd.read_csv("data/sales_data.csv")

# Check Missing Values
print("\nMissing Values:")
print(df.isnull().sum())

# Remove Missing Values
df = df.dropna()

# Remove Duplicate Rows
df = df.drop_duplicates()

# Display dataset
print(df)

# Analysis
print("\nTotal Sales:", df["Sales"].sum())
print("Total Profit:", df["Profit"].sum())

# Sales Chart
plt.figure(figsize=(8,5))
sns.barplot(x="Product", y="Sales", data=df)
plt.title("Sales by Product")
plt.xticks(rotation=45)
plt.savefig("images/product_sales.png")
plt.show()

# Profit Chart
plt.figure(figsize=(8,5))
sns.barplot(x="Product", y="Profit", data=df)
plt.title("Profit by Product")
plt.xticks(rotation=45)
plt.savefig("images/profit_chart.png")
plt.show()

# Pie Chart
category_sales = df.groupby("Category")["Sales"].sum()

plt.figure(figsize=(6,6))
category_sales.plot(kind="pie", autopct="%1.1f%%")
plt.title("Category Sales Distribution")
plt.ylabel("")
plt.savefig("images/category_sales_pie.png")
plt.show()

# Highest Selling Product
highest_product = df.loc[df["Sales"].idxmax()]

print("\nHighest Selling Product:")
print(highest_product)

# Category Wise Sales
category_sales = df.groupby("Category")["Sales"].sum()

print("\nCategory Wise Sales:")
print(category_sales)

# Summary Statistics
print("\nSummary Statistics:")
print(df.describe())

top_products = df.sort_values(
    by="Sales",
    ascending=False
).head(5)

plt.figure(figsize=(8,5))

sns.barplot(
    x="Sales",
    y="Product",
    data=top_products
)

plt.title("Top 5 Products by Sales")

plt.savefig("images/top_products.png")
plt.show()

print("\nBusiness Insights")

print(
    f"Highest Sales Product: {highest_product['Product']}"
)

print(
    f"Total Categories: {df['Category'].nunique()}"
)

print(
    f"Average Profit: {df['Profit'].mean():.2f}"
)