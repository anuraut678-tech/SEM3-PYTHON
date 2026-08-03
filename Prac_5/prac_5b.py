import pandas as pd

# Read the CSV dataset
df = pd.read_csv("StressLevelDataset.csv")

# Display the dataset
print("Dataset:")
print(df)

# Display statistical information
print("\nStatistical Information:")
print(df.describe())
