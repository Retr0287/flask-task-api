from db import cursor, users_db
def create_task(title, user_id):
    cursor.execute("INSERT INTO task (title, user_id) VALUES (%s, %s)", (title, user_id))
    users_db.commit()