import pandas as pd

df = pd.read_csv("sales - sales.csv")

print("Sales Dataset:")
print(df)

print("\nTotal Sales by Category:")
print(df.groupby("Category")["Sales"].sum())

print("\nAverage Sales by Category:")
print(df.groupby("Category")["Sales"].mean())

print("\nTotal Quantity Sold by Category:")
print(df.groupby("Category")["Quantity"].sum())

print("\nTotal Sales by Region:")
print(df.groupby("Region")["Sales"].sum())

print("\nAverage Sales by Region:")
print(df.groupby("Region")["Sales"].mean())

print("\nMaximum Sales by Category:")
print(df.groupby("Category")["Sales"].max())
