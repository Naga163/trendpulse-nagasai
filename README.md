# TrendPulse

TrendPulse is a mini data pipeline project that collects trending stories from the Hacker News API, cleans the data, performs analysis, and creates visualizations.

## Project Workflow

Hacker News API  
→ `task1_data_collection.py`  
→ `data/trends_YYYYMMDD.json`  
→ `task2_data_processing.py`  
→ `data/trends_clean.csv`  
→ `task3_analysis.py`  
→ `data/trends_analysed.csv`  
→ `task4_visualization.py`  
→ `outputs/chart1_top_posts.png`  
→ `outputs/chart2_subreddits.png`  
→ `outputs/chart3_scatter.png`

## Tasks

### Task 1: Data Collection
Fetches top Hacker News stories using API calls, categorizes them, and saves the data as JSON.

### Task 2: Data Processing
Loads the JSON file, removes duplicates, handles missing values, and saves a cleaned CSV file.

### Task 3: Analysis
Creates additional analytical columns such as title length, engagement, score per comment, and rank in category.

### Task 4: Visualization
Generates charts to visualize top posts, category distribution, and the relationship between score and comments.

## Files in This Project

- `task1_data_collection.py` — collects data from the API
- `task2_data_processing.py` — cleans and prepares the data
- `task3_analysis.py` — performs feature engineering and analysis
- `task4_visualization.py` — creates charts from analysed data

## How to Run

Run the files in this order:

```bash
python task1_data_collection.py
python task2_data_processing.py
python task3_analysis.py
python task4_visualization.py
