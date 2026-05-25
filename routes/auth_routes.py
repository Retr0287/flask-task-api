import jwt
import os
import bcrypt
from flask import Blueprint, request, jsonify
from dotenv import load_dotenv
from db import cursor, users_db
load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")
auth_bp = Blueprint("auth", __name__)
# REGISTER
@auth_bp.route("/register", methods=["POST"])
def add_user():
    data = request.get_json()
    if not data:
        return jsonify({"error": "json required"}), 400
    if "username" not in data or "password" not in data:
        return jsonify({"error": "username and password required"}), 400
    password = data["password"]
    hashed_password = bcrypt.hashpw(
        password.encode(),
        bcrypt.gensalt()
    )
    cursor.execute(
        "INSERT INTO users (username, password) VALUES (%s, %s)",
        (data["username"], hashed_password)
    )
    users_db.commit()
    return jsonify({"message": "user created"}), 201


# LOGIN
@auth_bp.route("/login", methods=["POST"])
def search_user():
    data = request.get_json()
    if not data:
        return jsonify({"error": "json required"}), 400
    if "username" not in data or "password" not in data:
        return jsonify({"error": "username and password required"}), 400
    password = data["password"]
    cursor.execute(
        "SELECT * FROM users WHERE username = %s",
        (data["username"],)
    )
    user = cursor.fetchone()
    if not user:
        return jsonify({"error": "user not found"}), 404
    if not bcrypt.checkpw(
        password.encode(),
        user["password"].encode()
    ):
        return jsonify({"error": "wrong password"}), 403
    payload = {
        "user_id": user["id"]
    }
    token = jwt.encode(
        payload,
        SECRET_KEY,
        algorithm="HS256"
    )
    return jsonify({"token": token}), 200