# FastAPI JWT Auth API

A backend authentication API built with FastAPI, JWT tokens, and SQLite.

## What it does

- User registration with hashed passwords
- Login and JWT token generation
- Protected profile route (only accessible with valid token)
- SQLite database with SQLAlchemy

## Tech Stack

Python, FastAPI, SQLAlchemy, SQLite, JWT, Passlib, Uvicorn

## Setup

```
git clone https://github.com/syedmuhammadpy/fastapi-jwt-auth-api.git
cd fastapi-jwt-auth-api
pip install -r requirements.txt
cp .env.example .env
uvicorn main:app --reload
```

Open `http://localhost:8000/docs` to test the API.

## Endpoints

**POST /register**
```json
{
  "name": "Syed Muhammad",
  "email": "syed@example.com",
  "password": "yourpassword"
}
```

**POST /login**
```json
{
  "email": "syed@example.com",
  "password": "yourpassword"
}
```

**GET /profile**
```
Authorization: Bearer YOUR_TOKEN
```

## Author

Syed Muhammad — github.com/syedmuhammadpy
