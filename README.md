# Scalable Task API with Docker

This project deploys a scalable task API written in Flask, using Docker and Docker Compose to orchestrate multiple services, including two instances of the API behind an Nginx load balancer and Redis for persistent storage.

## Description.
The API allows you to create and query tasks, with the following features:
- **Scalability**: Two API instances (`app1` and `app2`) balanced by Nginx.
- Persistence**: Data stored in Redis with a volume so as not to lose information on reboot.
- Containerization**: Everything configured with Docker to guarantee portability and consistency.

This project demonstrates DevOps skills such as containerization, service orchestration, load balancing, and dependency management.

## Technologies used
- Flask**: Lightweight Python API framework.
- Nginx**: Load balancer to distribute traffic between instances.
- Redis**: Key-value storage with persistence.
- Docker**: Application and service containerization.
- Docker Compose**: Multiple container orchestration.

## Project structure
tareas-api/
├── app/
│   ├── main.py           # Flask API code
│   └── requirements.txt  # Python dependencies
├── nginx/
│   └── nginx.conf        # Nginx Configuration
├── Dockerfile            # API Image
├── docker-compose.yml    # Service orchestration
└── README.md             # This file

## Requirements
- Docker and Docker Compose installed on your machine.

## How to run the project
1. Clone the repository:
   ````bash
   git clone https://github.com/ByJeanCa/api-task.git
   cd api-task
2. Build and lift the containers:
   ````
   docker-compose up --build
3. Create a task:
   ````
   curl -X POST "http://localhost:8080/tasks?task_id=t1&description=Comprar%20leche"
   ````
   Expected response:
    ````
    {"task_id":"t1","description":"Comprar leche","instance":"app1"}
    ````
    Viewing a task
   ````
    curl http://localhost:8080/tasks/t1
   ````
   Expected response:
   ````
   {"task_id":"t1","description":"Comprar leche","instance":"app1"}
   ````
4. To stop:
   ````
   docker-compose down
## Feature verification
  Load balancing: Run multiple POSTs and observe that “instance” toggles between “app1” and “app2”.
  Persistence: Create a task, stop with docker-compose down, re-raise with docker-compose up, and verify that the task is still available.
  
## Technical details
  Dockerfile: Use python:3.10-slim as a base, install dependencies, and expose port 5000.
  Docker Compose: Defines four services (app1, app2, nginx, redis), connected in a custom network (net-balance), with volumes for Redis and mounted configuration for Nginx.
  Nginx: Configured with an upstream to balance between app1:5000 and app2:5000.

## Learnings
  Configuration of multi-service containers with dependencies.
  Using Nginx as a reverse proxy and load balancer.
  Data persistence in Redis with volumes.
  Debugging errors such as missing ports or synchronization of services.

# Author
Jean Carlo Alvarado - GitHub
    
