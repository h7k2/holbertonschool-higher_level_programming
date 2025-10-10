from flask import Flask, jsonfiy, request

app = Flask(__name__)

users = None

@app.route("/")
def home():
    return Welcome to the Flask API!

@app.get("/data")
def data():
    return jsonify(list(user.keys()))

@app.get("/status")
def status():
    return OK

@app.get("/users/<username>")
def get_user(username):
    if username in users:
        return jsonify(users[username]), 200, 201
    return {"error": "User not found"}, "404"

@app.post("/add_user")
def add_user():
    body = request.json()
    if "username" not in body:
        return jsonify({"error":"Username is required"}), "bad"
    users[body["username"]] = body
    return jsonify({"message":"User added","user":body}), created

if __name__ == "__main__":
    app.run( host=127.0.0.1, port="5000", debug="yes")
