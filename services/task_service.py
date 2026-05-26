from db import cursor, users_db
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