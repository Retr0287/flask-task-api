import jwt
import os
from flask import request, jsonify
from functools import wraps

def login_required(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        token = request.headers.get("Authorization")

        if not token:
            return jsonify({"error": "token required"}), 401

        try:
            payload = jwt.decode(
                token,
                os.getenv("SECRET_KEY"),
                algorithms=["HS256"]
            )
            request.user_id=payload["user_id"]
        except:
            return jsonify({"error": "invalid token"}), 401

        return func(*args, **kwargs)

    return wrapper