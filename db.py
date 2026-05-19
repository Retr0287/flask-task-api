import mysql.connector
import os
users_db = mysql.connector.connect(
host=os.getenv("DB_HOST"),
user=os.getenv("DB_USER"),
password=os.getenv("DB_PASSWORD"),
database=os.getenv("DB_NAME")
)
cursor=users_db.cursor(dictionary=True)
    