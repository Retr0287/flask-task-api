from flask import request
from db import cursor, users_db
from exceptions.api_exeptions import ForbiddenError,NotFoundError,ValidationError
from utils.validators import validate_task
def create_task(title, user_id):
    try:
        cursor.execute("INSERT INTO task (title, users_id) VALUES (%s, %s)", (title, user_id))
        users_db.commit()

    except Exception as e:
        print(e)
        return False
    
    return True

def get_user_tasks(user_id):
    cursor.execute("SELECT * FROM task WHERE users_id=%s", (user_id))
    return cursor.fetchall()

def delete_user_task(task_id, user_id):
    cursor.execute("SELECT * FROM task WHERE id=%s", (task_id,))
    task=cursor.fetchone()
    if not task:
        raise NotFoundError("task not found")
    if task["user_id"]!=user_id:
        raise ForbiddenError("accses denied")

    cursor.execute("DELETE FROM task WHERE id=%s", ("user_id"))
    users_db.commit()

def patch_user_task(task_id, user_id):
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