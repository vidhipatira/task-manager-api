# Task Manager API

## Tech Stack
- FastAPI
- PostgreSQL
- Python

## Features
- Create tasks
- View tasks

## How to Run
1. Install dependencies
2. Run:
   uvicorn main:app --reload

##rebuild and rerun your Docker image:

docker build -t task-api .
docker stop task-api-container
docker rm task-api-container
docker run -d -p 8000:8000 --name task-api-container task-api

## Test API endpoints
Use Postman or the Swagger UI (/docs) to check all routes for tasks (GET, POST, PUT, DELETE, etc.).
