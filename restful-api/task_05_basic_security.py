#!/usr/bin/env python3
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager, create_access_token,
    jwt_required, get_jwt_identity
)
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['JWT_SECRET'] = 'change_me'

jwt = JWTManager(app)
auth = HTTPBasicAuth()

users = {
    "user1": {"username": "user1", "password": generate_password_hash("password"), "role": "user"},
    "admin1": {"username": "admin1", "password": generate_password_hash("password"), "role": "admin"},
}

@auth.verify_password
def verify_password(username, password):
    u = users.get(username)
    if u and check_password_hash(u["password"], password):
        return username

@app.get('/basic-protected')
@auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted"

@app.post('/login')
def login():
    data = request.get_json(silent=True) or {}
    username = data.get('username')
    password = data.get('password')
    u = users.get(username)
    if not username or not password or not u or not check_password_hash(u['password'], password):
        return jsonify({"error": "Bad username or password"}), 401
    token = create_access_token(identity={"username": username, "role": u["role"]})
    return jsonify(access_token=token)

@app.get('/jwt-protected')
@jwt_required()
def jwt_protected():
    ident = get_jwt_identity()
    if not ident:
        return jsonify({"error": "Missing or invalid token"}), 401
    return "JWT Auth: Access Granted"

@app.get('/admin-only')
@jwt_required()
def admin_only():
    current_user = get_jwt_identity()
    if current_user.get('role') != 'admin':
        return jsonify({"error": "Admin access required"}), 403
    return "Admin Access: Granted"

@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401

@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401

@jwt.expired_token_loader
def handle_expired_token_error(jwt_header, jwt_payload):
    return jsonify({"error": "Token has expired"}), 401

if __name__ == '__main__':
    app.run()
