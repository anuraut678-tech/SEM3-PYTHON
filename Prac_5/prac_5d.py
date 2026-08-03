import pandas as pd

# Create a Pandas Series
marks = pd.Series([45, 60, 75, 30, 90, 55, 80])

print("Original Series:")
print(marks)

# Filter the Series using a Boolean condition
filtered = marks[marks > 50]

print("\nFiltered Series (Marks > 50):")
print(filtered)
