# Flask Tasks API

Backend REST API built with Flask, MySQL and JWT authentication.

This project was created as backend development practice and includes authentication, protected routes, CRUD operations and database interaction.

---

# Features

- User registration
- User login
- JWT token authentication
- Protected routes using Authorization header
- Create tasks for authorized users
- Get tasks only for current user
- Update tasks
- Delete tasks
- Access control for task ownership
- MySQL database integration
- Environment variables support with .env

---

# Technologies Used

- Python
- Flask
- MySQL
- mysql.connector
- PyJWT
- python-dotenv

---

# API Endpoints

## Authentication

### Register User
POST /register

### Login User
POST /login

Returns JWT token for authorized requests.

---

## Tasks

### Create Task
POST /tasks

### Get User Tasks
GET /tasks

### Update Task
PATCH /tasks/<task_id>

Allows updating task title only for task owner.

### Delete Task
DELETE /task/<task_id>

Allows deleting tasks only for task owner.

---

# Authorization

Protected routes require JWT token in Authorization header:

bash Authorization: Bearer your_token 

---

# Project Structure

bash app.py              # Main Flask application requirements.txt    # Project dependencies README.md           # Documentation .env                # Environment variables 

---

# Learning Goals

This project was built to practice:

- REST API development
- Flask backend fundamentals
- JWT authentication
- CRUD operations
- MySQL integration
- Protected routes
- User authorization logic
- Git & GitHub workflow
