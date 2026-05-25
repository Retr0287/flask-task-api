# Flask Task API

A backend REST API built with Flask and MySQL.

This project was created as a learning backend application focused on authentication, JWT authorization, CRUD operations, and project structure organization.

## Features

- User registration
- User login
- JWT authentication
- Protected routes
- Task CRUD operations
- Password hashing with bcrypt
- MySQL database integration
- Flask Blueprints
- Custom decorators
- Validators/helpers
- Modular backend structure

---

# Technologies

- Python
- Flask
- MySQL
- JWT (PyJWT)
- bcrypt
- dotenv

---

# Project Structure
task_api/
│
├── routes/
│   ├── auth_routes.py
│   └── task_routes.py
│
├── decorators/
│   └── auth_decorator.py
│
├── utils/
│   └── validators.py
│
├── auth.py
├── db.py
├── app.py
├── requirements.txt
└── .env

---

# API Endpoints

## Authentication

### Register
POST /register

Body:
{
  "username": "test",
  "password": "123456"
}

---

### Login
POST /login

Returns JWT token.

---

# Tasks

## Create Task
POST /tasks

Headers:
Authorization: YOUR_TOKEN

Body:
{
  "title": "Learn Flask"
}

---

## Get Tasks
GET /tasks

---

## Update Task
PATCH /tasks/<task_id>

---

## Delete Task
DELETE /task/<task_id>

---

# Installation

Clone repository:
git clone https://github.com/Retr0287/flask-task-api.git

Install dependencies:
pip install -r requirements.txt

Create .env file:
SECRET_KEY=your_secret_key

Configure MySQL database in db.py.

Run server:
python app.py

---

# Goals Of This Project

This project was built to practice:

- Backend development fundamentals
- REST API architecture
- Authentication systems
- Flask project organization
- Database interaction
- Writing cleaner and reusable code

---

# Future Improvements

- Refresh tokens
- SQLAlchemy migration
- Docker support
- Unit testing
- Pagination
- Task categories
- User roles
- Deployment

---

# Author

GitHub:
https://github.com/Retr0287