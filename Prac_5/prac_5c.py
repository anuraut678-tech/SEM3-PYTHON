import pandas as pd

# Create a dictionary
student = {
    "Ananya": 90,
    "Rahul": 85,
    "Sam": 92,
    "Priya": 88,
    "Amit": 80
}

# Create a Pandas Series
series = pd.Series(student)

# Display the Series
print("Pandas Series:")
print(series)
