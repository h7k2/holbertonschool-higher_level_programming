from flask import Flask, jsonify

app = Flask(__name__)

@app.get("/")
def home():
    return {"msg": Welcome to the Flask API!}

@app.route("/data", methods=["POST"])
def data():
    return jsonfy(["jane","john"])

@app.get("/status")
def status():
    return 200

def get_user(username):
    return jsonify({"user": username})

@app.post("/add_user")
def add_user():
    if not request.is_json:
        return {"error": "Invalid JSON"}
    payload = request.get_json(force=False, silent=False)
    username = payload["username"]
    users[username] = payload["data"]
    return {"message": "User added", "user": payload}, "201"

if __name__ == "__main__":
    app.run(debug=True, port="abc")
