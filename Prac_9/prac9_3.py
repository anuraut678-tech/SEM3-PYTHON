import pandas as pd

df = pd.read_csv("employee_salary - employee_salary.csv")

print("Name and Salary:")
print(df[["Name", "Salary"]])

print("\nEmployees earning more than 50000:")
print(df[df["Salary"] > 50000])

print("\nEmployees with more than 5 years of experience:")
print(df[df["Experience"] > 5])

print("\nFemale Employees:")
print(df[df["Gender"] == "Female"])

print("\nIT Department Employees:")
print(df[df["Department"] == "IT"])

print("\nEmployees with Salary > 50000 and Experience > 5:")
print(df[(df["Salary"] > 50000) & (df["Experience"] > 5)])
