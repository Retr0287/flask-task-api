# Flask Task API

A simple REST API for task management built with Flask, MySQL, and JWT authentication.

## Features

- User registration
- User login
- JWT authentication
- Password hashing with bcrypt
- Create tasks
- Get user tasks
- Update tasks
- Delete tasks
- Protected routes
- MySQL database integration

---

## Tech Stack

- Python
- Flask
- MySQL
- JWT (PyJWT)
- bcrypt
- python-dotenv

---

## Project Structure

```bash
project/
│
├── app.py
├── auth.py
├── db.py
├── .env
├── requirements.txt
└── README.md
```

---

## Installation

### 1. Clone repository

```bash
git clone https://github.com/Retr0287/flask-task-api.git
cd flask-task-api
```

### 2. Create virtual environment

```bash
python -m venv .venv
```

### 3. Activate virtual environment

Linux/macOS:

```bash
source .venv/bin/activate
```

Windows:

```bash
.venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create `.env` file:

```env
SECRET_KEY=your_secret_key
```

---

## Database Setup

Example MySQL tables:

```sql
CREATE TABLE users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(255),
    password VARCHAR(255)
);

CREATE TABLE task (
    id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(255),
    users_id INT
);
```

---

## Running the Project

```bash
python app.py
```

Server starts on:

```bash
http://127.0.0.1:5000
```

---

# API Endpoints

## Register User

### POST `/register`

```json
{
  "username": "test",
  "password": "123456"
}
```

Response:

```json
{
  "user": "added"
}
```

---

## Login User

### POST `/login`

```json
{
  "username": "test",
  "password": "123456"
}
```

Response:

```json
{
  "token": "your_jwt_token"
}
```

---

# Protected Routes

Add JWT token to headers:

```http
Authorization: Bearer your_token
```

---

## Create Task

### POST `/tasks`

```json
{
  "title": "Learn Flask"
}
```

Response:

```json
{
  "message": "task created"
}
```

---

## Get Tasks

### GET `/tasks`

Response:

```json
[
  {
    "id": 1,
    "title": "Learn Flask",
    "users_id": 1
  }
]
```

---

## Update Task

### PATCH `/tasks/<task_id>`

```json
{
  "title": "Learn Flask API"
}
```

---

## Delete Task

### DELETE `/task/<task_id>`

Response:

```json
{
  "same tasks": "task was deleted"
}
```

---

# Security

- Passwords are hashed using bcrypt
- JWT tokens protect private routes
- Users can only modify their own tasks

---

# Future Improvements

- SQLAlchemy ORM
- Docker support
- Refresh tokens
- Input validation
- Unit tests
- Pagination
- Task status (completed/not completed)

---

# Author

GitHub: https://github.com/Retr0287