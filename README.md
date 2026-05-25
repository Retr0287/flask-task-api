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

```bash
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
```

---

# API Endpoints

## Authentication

### Register

```http
POST /register
```

Body:

```json
{
  "username": "test",
  "password": "123456"
}
```

---

### Login

```http
POST /login
```

Returns JWT token.

---

# Tasks

## Create Task

```http
POST /tasks
```

Headers:

```http
Authorization: YOUR_TOKEN
```

Body:

```json
{
  "title": "Learn Flask"
}
```

---

## Get Tasks

```http
GET /tasks
```

---

## Update Task

```http
PATCH /tasks/<task_id>
```

---

## Delete Task

```http
DELETE /task/<task_id>
```

---

# Installation

Clone repository:

```bash
git clone https://github.com/Retr0287/flask-task-api.git
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create `.env` file:

```env
SECRET_KEY=your_secret_key
```

Configure MySQL database in `db.py`.

Run server:

```bash
python app.py
```

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