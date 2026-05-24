import jwt
import os
import bcrypt
from flask import Flask, request, jsonify
from dotenv import load_dotenv
load_dotenv()
from db import cursor, users_db
from auth import get_user_id
from routes.auth_routes import auth_bp 
app=Flask(__name__)
SECRET_KEY=os.getenv("SECRET_KEY")
app.register_blueprint(auth_bp)

#TASK    
@app.route("/tasks", methods=['POST'])
def add_task():
    user_id = get_user_id()

    if type(user_id) != int:
        return user_id
    
    body = request.get_json()
    
    if "title" not in body:
        return jsonify({"error": "title required"}), 400

    if not body["title"].strip():
        return jsonify({"error": "title cannot be empty"}), 400
    cursor.execute(
        "INSERT INTO task (title, users_id) VALUES (%s, %s)",
        (body["title"], user_id)
    )
    users_db.commit()

    return jsonify({"message": "task created"}), 201

@app.route("/tasks", methods=['GET' ])
def get_tasks():
    user_id=get_user_id()
    cursor.execute(
        "SELECT * FROM task WHERE users_id = %s",
        (user_id,)
    )
    tasks = cursor.fetchall()
    return jsonify(tasks), 200

@app.route("/task/<int:task_id>", methods=['DELETE'])
def delete_tasks(task_id):
    user_id=get_user_id()
    cursor.execute("SELECT * FROM task WHERE id=%s", (task_id,))
    task=cursor.fetchone()
    if not task:
        return jsonify ({"error": "task not found"}), 404
    if task["user_id"]!=user_id:
        return jsonify ({"error": "access denied"}), 403

    cursor.execute("DELETE FROM task WHERE id=%s", (task_id,))
    users_db.commit()
    return jsonify({"message": "task deleted"}), 200

@app.route("/tasks/<int:task_id>", methods=['PATCH'])
def update_tasks(task_id):
    user_id=get_user_id()
    body = request.get_json()
    cursor.execute("SELECT * FROM task WHERE id=%s", (task_id,))
    task=cursor.fetchone()
    if not task:
        return jsonify ({"error": "task not found"}), 404
    if task["user_id"]!=user_id:
        return jsonify ({"error": "access denied"}), 403

    if "title" not in  body:
        return jsonify({"error": "title required"}), 400
    
    cursor.execute(
    "UPDATE task SET title = %s WHERE id=%s",
    (body["title"], task_id))
    users_db.commit()
    return jsonify({"message": "task updated"}), 200

        
if __name__ == "__main__": 
    app.run(debug=True)
