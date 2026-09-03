import pandas as pd

df = pd.read_csv("movie_ratings - movie_ratings.csv")

print("Original Movie Dataset:")
print(df)

print("\nMovies sorted by Rating in Ascending Order:")
print(df.sort_values("Rating"))

print("\nMovies sorted by Rating in Descending Order:")
print(df.sort_values("Rating", ascending=False))

print("\nMovies sorted by Votes in Descending Order:")
print(df.sort_values("Votes", ascending=False))

print("\nTop 5 Movies based on Rating:")
print(df.sort_values("Rating", ascending=False).head(5))

print("\nBottom 3 Movies based on Rating:")
print(df.sort_values("Rating").head(3))
