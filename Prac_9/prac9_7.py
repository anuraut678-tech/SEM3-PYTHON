import pandas as pd

df = pd.read_csv("sales - sales.csv")

print("Sales Dataset:")
print(df)

print("\nAverage Sales:")
print(df["Sales"].mean())

print("\nMaximum Sales:")
print(df["Sales"].max())

print("\nMinimum Sales:")
print(df["Sales"].min())

print("\nMedian Sales:")
print(df["Sales"].median())

print("\nStandard Deviation of Sales:")
print(df["Sales"].std())

print("\nAverage Price:")
print(df["Price"].mean())

print("\nAverage Quantity:")
print(df["Quantity"].mean())

print("\nTotal Number of Orders:")
print(len(df))
