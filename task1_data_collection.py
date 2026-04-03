
# TrendPulse Task 1
# Fetch data from HackerNews API and categorize stories

import requests
import json
import os
import time
from datetime import datetime

os.makedirs("data", exist_ok=True)

headers = {"User-Agent": "TrendPulse/1.0"}

category_keywords = {
    "technology": ["ai", "software", "tech", "code", "computer", "data", "cloud", "api", "gpu", "llm"],
    "worldnews": ["war", "government", "country", "president", "election", "climate", "attack", "global"],
    "sports": ["nfl", "nba", "fifa", "sport", "game", "team", "player", "league", "championship"],
    "science": ["research", "study", "space", "physics", "biology", "discovery", "nasa", "genome"],
    "entertainment": ["movie", "film", "music", "netflix", "book", "show", "award", "streaming"]
}

def fetch_json(url, session):
    try:
        response = session.get(url, headers=headers, timeout=15)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return None

def find_matching_categories(title):
    title_lower = title.lower()
    matched = []

    for category, keywords in category_keywords.items():
        for keyword in keywords:
            if keyword in title_lower:
                matched.append(category)
                break

    return matched

session = requests.Session()

top_url = "https://hacker-news.firebaseio.com/v0/topstories.json"
story_ids = fetch_json(top_url, session)

if not story_ids:
    print("Failed to fetch top story IDs")
else:
    story_ids = story_ids[:500]

    all_stories = []

    for story_id in story_ids:
        item_url = f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json"
        story = fetch_json(item_url, session)

        if not story:
            continue

        title = story.get("title")
        if not title:
            continue

        matched = find_matching_categories(title)

        if not matched:
            continue

        all_stories.append({
            "id": story.get("id"),
            "title": title,
            "score": story.get("score", 0),
            "descendants": story.get("descendants", 0),
            "by": story.get("by", "unknown"),
            "matched_categories": matched
        })

    category_count = {cat: 0 for cat in category_keywords}
    collected = []
    used_ids = set()

    for story in all_stories:
        if story["id"] in used_ids:
            continue

        possible = [cat for cat in story["matched_categories"] if category_count[cat] < 25]

        if not possible:
            continue

        selected = min(possible, key=lambda c: category_count[c])

        record = {
            "post_id": story["id"],
            "title": story["title"],
            "category": selected,
            "score": story["score"],
            "num_comments": story["descendants"],
            "author": story["by"],
            "collected_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        collected.append(record)
        used_ids.add(story["id"])
        category_count[selected] += 1

    time.sleep(2)

    today = datetime.now().strftime("%Y%m%d")
    file_path = f"data/trends_{today}.json"

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(collected, file, indent=4, ensure_ascii=False)

    print(f"Collected {len(collected)} stories.")
    print("Category counts:", category_count)
