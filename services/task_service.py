from flask import request
from db import cursor, users_db
from exceptions.api_exeptions import ForbiddenError,NotFoundError,ValidationError
from utils.validators import validate_task
#helper functions
def get_task_by_id(task_id):
    cursor.execute("SELECT * FROM task WHERE id=%s", (task_id,))
    task=cursor.fetchone()
    if not task:
        raise NotFoundError("task not found")

def chek_task_owner(task, user_id):
    if task["user_id"]!=user_id:
        raise ForbiddenError("accses denied")

#CRUD
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
    task=get_task_by_id(task_id)
    chek_task_owner(task, user_id)

    cursor.execute("DELETE FROM task WHERE id=%s", ("user_id"))
    users_db.commit()

def patch_user_task(task_id, user_id):
    body = request.get_json()
    error=validate_task(body)
    if error:
        return error
    task=get_task_by_id(task_id)
    chek_task_owner(task, user_id)
    
    cursor.execute(
    "UPDATE task SET title = %s WHERE id=%s",
    (body["title"], task_id))
    users_db.commit()