import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
os.makedirs("../outputs", exist_ok=True)



# Load dataset
df = pd.read_csv("../data/sales_data.csv")

# Display first 5 rows
print("First 5 Rows of Dataset:")
print(df.head())
print("\nDataset Information:")
print(df.info())

print("\nColumn Names:")
print(df.columns)

print("\nMissing Values:")
print(df.isnull().sum())
print("\nBefore Cleaning - Shape:", df.shape)

# Remove duplicates
df = df.drop_duplicates()

# Remove missing values
df = df.dropna()

print("After Cleaning - Shape:", df.shape)
print("\nSummary Statistics:")
print(df.describe())

# Total Sales
print("\nTotal Sales:", df["Sales"].sum())

# Average Sales
print("Average Sales:", df["Sales"].mean())

# Category-wise Sales
category_sales = df.groupby("Category")["Sales"].sum()
print("\nSales by Category:")
print(category_sales)
print("\nGenerating Bar Chart...")

plt.figure(figsize=(6,4))
sns.barplot(x="Category", y="Sales", data=df)

plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")

plt.tight_layout()
plt.savefig("../outputs/sales_bar_chart.png")
plt.show()
plt.savefig("../outputs/sales_bar_chart.png")
plt.show()

print("\nSaving Cleaned Data to Excel...")
df.to_excel("../outputs/cleaned_sales_data.xlsx", index=False)
print("Excel File Saved Successfully!")