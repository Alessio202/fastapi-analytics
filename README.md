FastAPI Analytics

A simple REST API built with FastAPI for managing users and performing data analytics using a PostgreSQL database.
The project is containerized with Docker to simplify deployment.

Features:
REST API built with FastAPI
User management endpoints
Basic analytics queries on stored data
PostgreSQL database integration
Containerized environment using Docker

Technologies Used:
Python 3
FastAPI
PostgreSQL
Docker
Git

API Example Endpoints:

Get all users
GET /users

Create a user
POST /users

Example request body:

{
  "name": "Alessio Di Bella",
  "age": "22",
  "city": "Roma",
  "password": "password"
}

Example analytics endpoint
GET /analytics/average-age

Running the Project
1. Clone the repository
git clone https://github.com/Alessio202/fastapi-analytics.git
cd fastapi-analytics
cp .env.example .env

2a. Run with Docker
docker-compose up --build

2b. Run locally
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install poetry
poetry install
uvicorn app.main:api --app-dir src --reload

2c. Run with Poetry installed (no venv)

poetry run uvicorn app.main:api --app-dir src --reload


The API will be available at:

http://localhost:8000
API Documentation


Swagger UI:
http://localhost:8000/docs

ReDoc:
http://localhost:8000/redoc