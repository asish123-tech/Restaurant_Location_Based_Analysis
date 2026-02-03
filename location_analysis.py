import pandas as pd
import matplotlib.pyplot as plt
import os

if not os.path.exists("output"):
    os.makedirs("output")
df = pd.read_csv("dataset/Dataset.csv")

print("Dataset loaded successfully")
print("Total number of restaurants:", len(df))
# -----------------------------
# Top 10 Cities with Most Restaurants
# -----------------------------

city_counts = df["City"].value_counts().head(10)

plt.figure()
city_counts.plot(kind="bar")
plt.title("Top 10 Cities with Most Restaurants")
plt.xlabel("City")
plt.ylabel("Number of Restaurants")
plt.tight_layout()

plt.savefig("output/top_10_cities_restaurants.png")
plt.show()
print("Top 10 Cities with Most Restaurants plot saved as 'output/top_10_cities_restaurants.png'")
# -----------------------------
# Average Rating by City (Top 10)
# -----------------------------

avg_rating_city = (
    df.groupby("City")["Aggregate rating"]
    .mean()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure()
avg_rating_city.plot(kind="bar")
plt.title("Average Restaurant Rating by City (Top 10)")
plt.xlabel("City")
plt.ylabel("Average Rating")
plt.tight_layout()

plt.savefig("output/average_rating_by_city.png")
plt.show()
print("Average Rating by City plot saved as 'output/average_rating_by_city.png'")

# -----------------------------
# Price Range Distribution in Top City
# -----------------------------

top_city = df["City"].value_counts().idxmax()

price_distribution = (
    df[df["City"] == top_city]["Price range"]
    .value_counts()
    .sort_index()
)

plt.figure()
price_distribution.plot(kind="bar")
plt.title(f"Price Range Distribution in {top_city}")
plt.xlabel("Price Range")
plt.ylabel("Number of Restaurants")
plt.tight_layout()

plt.savefig("output/price_range_distribution.png")
plt.show()
print("Price Range Distribution plot saved as 'output/price_range_distribution.png'")

