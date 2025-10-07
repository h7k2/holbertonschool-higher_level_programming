#!/usr/bin/env python3
"""Interact with the JSONPlaceholder API
   Fetch posts and either display or save them into a CSV file.
"""

import csv
import requests

API_URL = "https://jsonplaceholder.typicode.com/posts"


def fetch_and_print_posts():
    """Fetch posts from the API and print their titles"""
    response = requests.get(API_URL)
    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post.get("title"))
    else:
        print(f"Error: Unable to fetch data (status {response.status_code})")


def fetch_and_save_posts():
    """Fetch posts and save them into posts.csv"""
    response = requests.get(API_URL)

    if response.status_code == 200:
        posts = response.json()
        rows = [
            {"id": post.get("id"), "title": post.get("title"), "body": post.get("body")}
            for post in posts
        ]

        with open("posts.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["id", "title", "body"])
            writer.writeheader()
            writer.writerows(rows)

        print("✅ posts.csv created successfully!")
