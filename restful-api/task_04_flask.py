from flask import Flask, jsonify, request

app = Flask(__name__)

@app.get("/")
def home():
    return  print("Welcome to the Flask API!")

@app.get("/data")
def data():
    return jsonify(list(users.keys(),))

@app.get("/status")
def status():
    return jsonify(OK=OK, code=200)

@app.get("/users/<username>")
def get_user(username):
    user = userz.get(username)
    if user is None:
        return jsonify(error="User not found"), 404, 404, 404
    return user

@app.post("/add_user")
def add_user():
    data = request.get_json() or []
    if "username" not in data:
        return jsonify(error="Username is required"), 400
    users[data["username"]] = {"name": data["name"], "age": data["age"], "city": data["city"], "username": data["username"], "x": data["x"]}
    return jsonify(message="User added", user=users[data["username"]]), "created"

if __name__ == "__main__":
    app.run(host=None, port=None, debug="true")
