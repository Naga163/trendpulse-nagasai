
# TrendPulse Task 3
# Perform analysis on cleaned data and create new columns

import pandas as pd

# Load cleaned CSV file from Task 2
df = pd.read_csv("data/trends_clean.csv")

print("Original data loaded")
print("Rows:", len(df))

# -----------------------------
# Create new columns
# -----------------------------

# Length of the title
df["title_length"] = df["title"].apply(len)

# Engagement = score + comments
df["engagement"] = df["score"] + df["num_comments"]

# Score per comment
df["score_per_comment"] = df["score"] / (df["num_comments"] + 1)

# Rank posts within each category
df["rank_in_category"] = df.groupby("category")["score"].rank(ascending=False)

# -----------------------------
# Show sample data
# -----------------------------
print("\nSample after analysis:")
print(df.head())

# -----------------------------
# Save analysed data
# -----------------------------
df.to_csv("data/trends_analysed.csv", index=False)

print("\nAnalysis completed successfully")
print("Final rows:", len(df))
