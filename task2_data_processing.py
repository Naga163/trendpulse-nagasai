
# TrendPulse Task 2
# Load the JSON file from Task 1, clean the data, and save it as a CSV file

import pandas as pd
import glob


# Find all JSON files inside the data folder
json_files = glob.glob("data/*.json")

# Select the latest JSON file
latest_file = max(json_files)
print("Using file:", latest_file)

# Load the JSON data into a pandas DataFrame
df = pd.read_json(latest_file)

# Show original number of rows before cleaning
print("Original rows:", len(df))

# Remove duplicate stories based on post_id
df = df.drop_duplicates(subset=["post_id"])

# Remove rows where title is missing
df = df.dropna(subset=["title"])

# Fill missing numeric values with 0
df["score"] = df["score"].fillna(0)
df["num_comments"] = df["num_comments"].fillna(0)

# Convert collected_at column into datetime format
df["collected_at"] = pd.to_datetime(df["collected_at"])

# Print DataFrame information after cleaning
print("\nCleaned DataFrame info:")
print(df.info())

# Save cleaned data to CSV
df.to_csv("data/trends_clean.csv", index=False)

print("\nClean CSV created successfully.")
print("Final rows:", len(df))
