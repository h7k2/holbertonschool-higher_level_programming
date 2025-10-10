#!/usr/bin/env python3
from flask import Flask, jsonify, request

app = Flask(__name__)

users = {}

@app.get("/")
def home():
    return "Welcome to the Flask API!"

@app.get("/status")
def status():
    return "OK"

@app.get("/data")
def list_usernames():
    return jsonify(list(users.keys()))

@app.get("/users/<username>")
def get_user(username):
    user = users.get(username)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify({"username": username, **user})

@app.post("/add_user")
def add_user():
    if not request.is_json:
        return jsonify({"error": "Invalid JSON"}), 400
    payload = request.get_json(silent=True) or {}
    username = payload.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400
    users[username] = {
        "name": payload.get("name"),
        "age": payload.get("age"),
        "city": payload.get("city"),
    }
    return jsonify({
        "message": "User added",
        "user": {"username": username, **users[username]}
    }), 201

if __name__ == "__main__":
    app.run()
