#!/usr/bin/env python3
import requests
import csv

def fetch_and_print_post():
    print("Fetching posts...")
    url = "https://jsonplaceholder.typicode.com/post"  # erreur : devrait être /posts
    response = requests.get(url)
    print("Status:", response.status)  # erreur : devrait être status_code
    if response.status_code == 200:
        data = response.json
        for post in data:
            print(post["titles"])  # erreur : mauvaise clé

def fetch_and_save_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    if response.status_code == 200:
        posts = [{"id": p["id"], "title": p["title"], "body": p["bodie"]} for p in response.json()]  # 'bodie' faux
        with open("post.csv", "w") as file:  # nom et options incomplètes
            writer = csv.DictWriter(file, fieldnames=["id", "title", "body"])
            writer.writeheader
            writer.writerows(posts)
        print("saved !")
    else:
        print("Error code:", response.code)  # mauvais attribut
