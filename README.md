# FastAPI JWT Auth API
A backend authentication API built with FastAPI, JWT tokens, and SQLite.

## What it does
- User registration with hashed passwords
- Login and JWT token generation
- Protected profile route (only accessible with valid token)
- SQLite database with SQLAlchemy

## API Preview
![API Docs](FastAPI_JWT_Auth_API.png)

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

## What I Learned
- I didn't know how JWT worked before this project.
  Now I understand how a token is created after
  login and how it's used to access protected routes.

- Learned that you should never save a plain password
  in a database — bcrypt hashes it so even if someone
  gets the database, they can't read the password.

- First time I split a project into separate files
  like auth.py, models.py, schemas.py — made
  everything much cleaner.

- Connecting SQLite with SQLAlchemy was confusing
  at first but makes sense now.

- Learned why .env file and .gitignore matter —
  never upload your secrets to GitHub.

## Author
Syed Muhammad — github.com/syedmuhammadpy
