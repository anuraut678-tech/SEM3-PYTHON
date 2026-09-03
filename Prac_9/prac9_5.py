import pandas as pd

df = pd.read_csv("movie_ratings - movie_ratings.csv")

print("Missing Values in Each Column:")
print(df.isnull().sum())

print("\nRows Containing Missing Values:")
print(df[df.isnull().any(axis=1)])

# Fill missing Rating with average Rating
df["Rating"] = df["Rating"].fillna(df["Rating"].mean())

# Fill missing Votes with average Votes
df["Votes"] = df["Votes"].fillna(df["Votes"].mean())

print("\nDataset After Handling Missing Values:")
print(df)

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())
