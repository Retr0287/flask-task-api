from flask import Blueprint, request, jsonify
from db import cursor, users_db
from decorators.auth_decorator import login_required
from utils.validators import validate_task
from services.task_service import create_task, get_user_tasks
from exceptions.api_exeptions import NotFoundError, ForbiddenError, ValidationError
task_bp=Blueprint("task", __name__)
#TASK    
@task_bp.route("/tasks", methods=['POST'])
@login_required
def add_task():
    body = request.get_json()
    error = validate_task(body)
    if error:
        return error
    user_id = request.user_id 
    create_task(body["title"], user_id)

    return jsonify({"message": "task created"}), 201

@task_bp.route("/tasks", methods=['GET' ])
def get_tasks():
    user_id=request.user_id
    tasks = get_user_tasks(user_id)
    return jsonify(tasks), 200

@task_bp.route("/tasks/<int:task_id>", methods=['DELETE'])
@login_required
def delete_tasks(task_id):
    user_id=request.user_id
    cursor.execute("SELECT * FROM task WHERE id=%s", (task_id,))
    task=cursor.fetchone()
    if not task:
        raise NotFoundError("task not found")
    if task["user_id"]!=user_id:
        raise ForbiddenError("accses denied")

    cursor.execute("DELETE FROM task WHERE id=%s", (task_id,))
    users_db.commit()
    return jsonify({"message": "task deleted"}), 200

@task_bp.route("/tasks/<int:task_id>", methods=['PATCH'])
@login_required
def update_tasks(task_id):
    user_id=request.user_id
    body = request.get_json()
    error=validate_task(body)
    if error:
        return error
    cursor.execute("SELECT * FROM task WHERE id=%s", (task_id,))
    task=cursor.fetchone()
    if not task:
        raise NotFoundError("task not found")
    if task["user_id"]!=user_id:
        raise ForbiddenError("accses denied")

    if "title" not in  body:
        raise ValidationError("title required")
    
    cursor.execute(
    "UPDATE task SET title = %s WHERE id=%s",
    (body["title"], task_id))
    users_db.commit()
    return jsonify({"message": "task updated"}), 200