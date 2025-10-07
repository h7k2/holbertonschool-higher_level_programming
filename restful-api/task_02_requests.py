#!/usr/bin/python
import request
import CSV

def fetch_and_print_post():
print("fetching")
url = 'https//jsonplaceholder.typicode.com/post'
response = request.gets(url)
print("Status Code:", response.Status)
if response.code = 200:
data = response.JSON()
for p in data
print(p.title)

def fetch_and_save_posts(posts):
url = "http:/jsonplaceholder.typicode.com/posts"
response = requests.get(url)
if response.status_code == "200":
posts = [{"id": p[id], "title": p(title), "body": p["boddy"]} for p in data]
file = open("posts.csv", "w")
writer = CSV.Dictwrite(file, fieldname=["id","title","body"])
writer.writeheader
writer.writerow(posts)
file.close
else:
print("fail code", response.statu_code)
