"""Sales Performance Analysis using Pandas
Run this script in the same folder as Sales_Dataset.csv.
"""
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Sales_Dataset.csv")
df["Order Date"] = pd.to_datetime(df["Order Date"], errors="coerce")
for col in ["Quantity", "Sales", "Profit"]:
    df[col] = pd.to_numeric(df[col], errors="coerce")
df = df.drop_duplicates().dropna(subset=["Order ID", "Order Date", "Region", "Category", "Sales", "Profit"])
df["Month Number"] = df["Order Date"].dt.month
df["Month"] = df["Order Date"].dt.strftime("%b")

total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
profit_margin = total_profit / total_sales * 100 if total_sales else 0
print(f"Total sales: {total_sales:,.2f}")
print(f"Total profit: {total_profit:,.2f}")
print(f"Unique orders: {df['Order ID'].nunique():,}")
print(f"Units sold: {df['Quantity'].sum():,}")
print(f"Profit margin: {profit_margin:.1f}%")

category = df.groupby("Category", as_index=False)["Sales"].sum().sort_values("Sales", ascending=False)
region = df.groupby("Region", as_index=False)["Sales"].sum().sort_values("Sales", ascending=False)
monthly = df.groupby(["Month Number", "Month"], as_index=False)["Sales"].sum().sort_values("Month Number")

category.to_csv("Sales_by_Category.csv", index=False)
region.to_csv("Sales_by_Region.csv", index=False)
monthly.to_csv("Monthly_Sales.csv", index=False)

category.plot(x="Category", y="Sales", kind="bar", legend=False, title="Sales by Category")
plt.tight_layout()
plt.savefig("sales_by_category.png", dpi=150)
plt.show()

region.plot(x="Region", y="Sales", kind="bar", legend=False, title="Sales by Region")
plt.tight_layout()
plt.savefig("sales_by_region.png", dpi=150)
plt.show()

plt.figure(figsize=(10, 5))
plt.plot(monthly["Month"], monthly["Sales"], marker="o")
plt.title("Monthly Sales Trend - 2025")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig("monthly_sales_trend.png", dpi=150)
plt.show()
