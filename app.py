import jwt
import os
from flask import Flask, request, jsonify
from dotenv import load_dotenv
load_dotenv()
from db import cursor, users_db
from auth import get_user_id
app=Flask(__name__)
SECRET_KEY=os.getenv("SECRET_KEY")

#REGISTER
@app.route("/register", methods=['POST'])
def add_user():
    data=request.get_json()

    cursor.execute(
        "INSERT INTO users (username, password) VALUES (%s, %s)", 
        (data["username"], data["password"])
    )

    users_db.commit()

    return jsonify({"user":"added"})

#LOGIN
@app.route('/login', methods=['POST'])
def search_user():
    data=request.get_json()

    cursor.execute(
    "SELECT * FROM users WHERE username = %s",
    (data["username"],)
    )

    user = cursor.fetchone()

    if not user:
        return jsonify({"error": "user not found"})

    if user["password"] !=data["password"]:
        return jsonify({"error": "wrong password"})
    
    payload = {
    "user_id": user["id"]
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    return jsonify({"token": token})


#TASK    
@app.route("/tasks", methods=['POST'])
def add_task():
    user_id=get_user_id()
    body = request.get_json()
    cursor.execute(
        "INSERT INTO task (title, user_id) VALUES (%s, %s)",
        (body["title"], user_id)
    )
    users_db.commit()

    return jsonify({"message": "task created"})

@app.route("/tasks", methods=['GET' ])
def get_tasks():
    request.headers.get("Authorization")
    user_id=get_user_id()
    cursor.execute(
        "SELECT * FROM task WHERE user_id = %s",
        (user_id,)
    )
    tasks = cursor.fetchall()
    return jsonify(tasks)

@app.route("/task/<int:task_id>", methods=['DELETE'])
def delete_tasks(task_id):
    user_id=get_user_id()
    cursor.execute("SELECT * FROM task WHERE id=%s", (task_id,))
    task=cursor.fetchone()
    if not task:
        return jsonify ({"error": "task not found"})
    if task["user_id"]!=user_id:
        return jsonify ({"error": "access denied"})

    cursor.execute("DELETE FROM task WHERE id=%s", (task_id,))
    users_db.commit()
    return jsonify({"same tasks":"task was deleted"})

@app.route("/tasks/<int:task_id>", methods=['PATCH'])
def update_tasks(task_id):
    user_id=get_user_id()
    body = request.get_json()
    cursor.execute("SELECT * FROM task WHERE id=%s", (task_id,))
    task=cursor.fetchone()
    if not task:
        return jsonify ({"error": "task not found"})
    if task["user_id"]!=user_id:
        return jsonify ({"error": "access denied"})

    if "title" not in  body:
        return jsonify({"error": "title required"})
    
    cursor.execute(
    "UPDATE task SET title = %s WHERE id=%s",
    (body["title"], task_id))
    users_db.commit()
    return jsonify({"success": "title updated"})

        
if __name__ == "__main__": 
    app.run(debug=True)
