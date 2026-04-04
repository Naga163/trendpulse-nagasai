
# TrendPulse Task 4
# Create visualizations from analysed data

import pandas as pd
import matplotlib.pyplot as plt
import os

# Create outputs folder if it doesn't exist
os.makedirs("outputs", exist_ok=True)

# Load analysed data
df = pd.read_csv("data/trends_analysed.csv")

print("Data loaded successfully")
print("Total rows:", len(df))

# -----------------------------------
# Chart 1: Top 10 posts by score
# -----------------------------------
top_posts = df.sort_values(by="score", ascending=False).head(10)

plt.figure(figsize=(12, 7))
plt.barh(top_posts["title"], top_posts["score"])
plt.xlabel("Score")
plt.ylabel("Post Title")
plt.title("Top 10 Trending Posts by Score")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig("outputs/chart1_top_posts.png")
plt.close()

print("Chart 1 created")

# -----------------------------------
# Chart 2: Posts per category
# -----------------------------------
category_counts = df["category"].value_counts()

plt.figure(figsize=(8, 5))
category_counts.plot(kind="bar")
plt.xlabel("Category")
plt.ylabel("Number of Posts")
plt.title("Posts per Category")
plt.tight_layout()
plt.savefig("outputs/chart2_subreddits.png")
plt.close()

print("Chart 2 created")

# -----------------------------------
# Chart 3: Score vs Comments
# -----------------------------------
plt.figure(figsize=(8, 6))
plt.scatter(df["num_comments"], df["score"])
plt.xlabel("Number of Comments")
plt.ylabel("Score")
plt.title("Score vs Number of Comments")
plt.tight_layout()
plt.savefig("outputs/chart3_scatter.png")
plt.close()

print("Chart 3 created")

print("\nAll visualizations created successfully!")
