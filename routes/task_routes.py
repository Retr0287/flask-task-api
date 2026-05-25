from flask import Blueprint, request, jsonify
from db import cursor, users_db
from task_api.auth import get_user_id
from decorators.auth_decorator import login_required

task_bp=Blueprint("task", __name__)
#TASK    
@task_bp.route("/tasks", methods=['POST'])
@login_required
def add_task():
    user_id = get_user_id()

    if type(user_id) != int:
        return user_id
    
    body = request.get_json()
    if not body:
        return jsonify({"error": "json required"}), 400
    
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

@task_bp.route("/tasks", methods=['GET' ])
def get_tasks():
    user_id=get_user_id()
    cursor.execute(
        "SELECT * FROM task WHERE users_id = %s",
        (user_id,)
    )
    tasks = cursor.fetchall()
    return jsonify(tasks), 200

@task_bp.route("/tasks/<int:task_id>", methods=['DELETE'])
@login_required
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

@task_bp.route("/tasks/<int:task_id>", methods=['PATCH'])
@login_required
def update_tasks(task_id):
    user_id=get_user_id()
    body = request.get_json()
    if not body:
        return jsonify({"error": "json required"}), 400
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