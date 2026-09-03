import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sales - sales.csv")

# 1. Bar Chart - Sales by Product
plt.figure(figsize=(8, 5))
plt.bar(df["Product"], df["Sales"])
plt.title("Sales by Product")
plt.xlabel("Product")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.show()


# 2. Line Chart - Sales by Order
plt.figure(figsize=(8, 5))
plt.plot(df["Order_ID"], df["Sales"], marker="o")
plt.title("Sales by Order")
plt.xlabel("Order ID")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.show()


# 3. Histogram - Distribution of Sales
plt.figure(figsize=(8, 5))
plt.hist(df["Sales"], bins=5)
plt.title("Distribution of Sales")
plt.xlabel("Sales")
plt.ylabel("Frequency")
plt.show()


# 4. Pie Chart - Sales by Category
category_sales = df.groupby("Category")["Sales"].sum()

plt.figure(figsize=(7, 7))
plt.pie(category_sales, labels=category_sales.index, autopct="%1.1f%%")
plt.title("Sales Distribution by Category")
plt.show()
