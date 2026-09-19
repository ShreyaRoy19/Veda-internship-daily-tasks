# Multi-User Task Management API

A secure, multi-user Task Management REST API built with **FastAPI**, **SQLAlchemy**, and **SQLite**. This application implements user authentication, authorization, and task CRUD operations with strict resource isolation to prevent cross-user access and vulnerabilities like IDOR.

---

## Features

- **User Authentication**: Secure user registration and token-based login using OAuth2 and JWT.
- **Password Hashing**: Industry-standard password hashing using `passlib` and bcrypt.
- **Task CRUD Operations**: Authenticated users can Create, Read, Update, and Delete their own tasks[cite: 1].
- **Data Isolation & Authorization**: Database queries are automatically filtered by user identity, ensuring users cannot access or modify another user's tasks[cite: 1].
- **Interactive Documentation**: Built-in Swagger UI and ReDoc endpoints for instant API testing.

---

## Tech Stack

- **Python 3.10+**
- **FastAPI** (Web framework)[cite: 1]
- **SQLAlchemy** (ORM)[cite: 1]
- **SQLite** (Database)[cite: 1]
- **Pydantic** (Data validation)
- **Python-JOSE & Passlib** (Security and JWT handling)

---

## Project Structure

```text
task_manager_api/
│
├── database.py       # SQLAlchemy engine and session setup
├── models.py         # Database models (User and Task)
├── schemas.py        # Pydantic data validation schemas
├── auth.py           # JWT token generation and current user dependency
├── main.py           # FastAPI application entry point and routes
└── README.md         # Project documentation
