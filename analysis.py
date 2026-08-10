import pandas as pd

df = pd.read_csv("books.csv")

# Clean the Price column
df["Price"] = df["Price"].str.replace(r"[^0-9.]", "", regex=True)
df["Price"] = df["Price"].astype(float)

print(df.head())
print("\nNumber of books:", len(df))
print("\nAverage price:", df["Price"].mean())
print("\nHighest price:", df["Price"].max())
print("\nLowest price:", df["Price"].min())
print("\nRating distribution:")
print(df["Rating"].value_counts())
import matplotlib.pyplot as plt

rating_counts = df["Rating"].value_counts()

rating_counts.plot(kind="bar")

plt.title("Book Rating Distribution")
plt.xlabel("Rating")
plt.ylabel("Number of Books")
plt.tight_layout()
plt.show()
most_expensive = df.loc[df["Price"].idxmax()]
print("\nMost expensive book:")
print(most_expensive["Title"])
print("Price:", most_expensive["Price"])
cheapest = df.loc[df["Price"].idxmin()]

print("\nCheapest book:")
print(cheapest["Title"])
print("Price:", cheapest["Price"])
print("\nAverage price by rating:")
print(df.groupby("Rating")["Price"].mean())
import matplotlib.pyplot as plt

avg_price_rating = df.groupby("Rating")["Price"].mean()

avg_price_rating.plot(kind="bar")

plt.title("Average Book Price by Rating")
plt.xlabel("Rating")
plt.ylabel("Average Price (£)")
plt.tight_layout()
plt.savefig("book_rating_distribution.png")
plt.show()
df.to_csv("books_cleaned.csv", index=False)

print("\nCleaned data saved to books_cleaned.csv")
print("\nTop 5 Most Expensive Books:")
print(df.nlargest(5, "Price")[["Title", "Price"]])
print("\nTop 5 Most Cheapest Books:")
print(df.nsmallest(5, "Price")[["Title", "Price"]])
print("\nMissing values:")
print(df.isnull().sum())
plt.savefig("price_by_rating.png")