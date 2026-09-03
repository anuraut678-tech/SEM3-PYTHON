import pandas as pd

df = pd.read_csv("employee_salary - employee_salary.csv")

print("Employee Dataset:")
print(df)

print("\nFirst 5 Records:")
print(df.head(5))

print("\nNumber of Employees:")
print(len(df))

print("\nColumn Names:")
print(df.columns)

print("\nAverage Salary:")
print(df["Salary"].mean())

print("\nAverage Experience:")
print(df["Experience"].mean())
