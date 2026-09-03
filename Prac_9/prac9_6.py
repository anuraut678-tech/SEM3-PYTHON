import pandas as pd

df = pd.read_csv("movie_ratings - movie_ratings.csv")

print("Data Types:")
print(df.dtypes)

# Convert Year to integer
df["Year"] = df["Year"].astype(int)

# Create Rating Category
def rating_category(rating):
    if rating >= 8:
        return "Excellent"
    elif rating >= 6:
        return "Good"
    else:
        return "Average"

df["Rating_Category"] = df["Rating"].apply(rating_category)

# Create Movie Age
current_year = 2026
df["Movie_Age"] = current_year - df["Year"]

print("\nUpdated Movie Dataset:")
print(df)
