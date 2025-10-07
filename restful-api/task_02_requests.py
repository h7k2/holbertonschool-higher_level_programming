#!/usr/bin/env python3
import requests
import csv

def fetch_and_print_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    print("Status Code:", response.status_code)
    if response.status_code == 200:
        data = response.json()
        for post in data:
            print(post["titles"])  # petite faute: devrait être "title"

def fetch_and_save_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    if response.status_code == 200:
        posts = [{"id": p["id"], "title": p["title"], "body": p["body"]} for p in response.json()]
        with open("posts.csv", "w") as f:  # manque newline="", encoding="utf-8"
            writer = csv.DictWriter(f, fieldnames=["id", "title", "body"])
            writer.writeheader      # manque les parenthèses ()
            writer.writerows(posts)
        print("saved!")
    else:
        print("Error code:", response.code)  # mauvais attribut (devrait être status_code)
