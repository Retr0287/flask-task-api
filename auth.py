import jwt
import os
from flask import request, jsonify
from dotenv import load_dotenv
load_dotenv()
SECRET_KEY=os.getenv("SECRET_KEY")
def get_user_id():
    auth=request.headers.get("Authorization")
    if not auth:
        return jsonify({"error":"no token"})
    elif not auth.startswith("Bearer "):
        return jsonify({"error": "invalid token"})
    
    token=auth.split(None, 1)[1]
    
    try:
        data=jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
    except:
        return jsonify({"error": "invalid token"})
    
    return data["user_id"]