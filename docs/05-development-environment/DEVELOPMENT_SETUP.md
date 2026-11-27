# Development Environment Setup

This document describes how to set up and run the Cubiland development
environment.

## Prerequisites

-   Docker and Docker Compose V2
-   Git
-   Python 3.14.x (for local backend development, optional if using
    Docker)
-   Poetry 2.x
-   Node.js 18+ (for local frontend development, optional if using
    Docker)

## Quick Start with Docker

The recommended way to run the development environment is using Docker
Compose.

### 1. Clone the Repository

``` bash
git clone <repository-url>
cd Cubiland
```

### 2. Configure Environment Variables

Copy the example environment file and configure it:

``` bash
cp .env.example .env
```

Edit `.env` with your local configuration. The default values work for
Docker Compose:

-   Database: `db:5432`
-   Redis: `redis:6379`
-   RabbitMQ: `rabbitmq:5672`
-   API: <http://localhost:8000>
-   RabbitMQ Management UI: <http://localhost:15672>

### 3. Start Services

Start all services:

``` bash
docker compose up -d
```

This starts: 
- PostgreSQL 16 (port 5432) 
- Redis 7 (port 6379) 
- RabbitMQ with Management Plugin (ports 5672, 15672) 
- FastAPI Backend (port 8000) 
- Celery Worker (port 8001) 
- Celery Beat (port 8002)

### 4. Verify Services

Check that all services are running:

``` bash
docker compose ps
```

Access the API: 
- API: <http://localhost:8000> 
- API Documentation: <http://localhost:8000/docs> 
- RabbitMQ Management UI: <http://localhost:15672> (use credentials from .env)

### 5. Stop Services

Stop all services:

``` bash
docker compose down
```

To also remove volumes:

``` bash
docker compose down -v
```

## Service Details

### PostgreSQL

-   Image: `postgres:16-alpine`
-   Default database: `cubiland`
-   Default user: `cubiland`
-   Port: 5432
-   Data persisted in Docker volume `postgres_data`

### Redis

-   Image: `redis:7-alpine`
-   Port: 6379
-   Data persisted in Docker volume `redis_data`

### RabbitMQ

-   Image: `rabbitmq:3-management-alpine`
-   AMQP port: 5672
-   Management UI port: 15672
-   Data persisted in Docker volume `rabbitmq_data`
-   Default user: `cubiland`
-   Default vhost: `/`

### FastAPI Backend

-   Built from `./backend/Dockerfile`
-   Port: 8000
-   Hot reload enabled for development
-   Source code mounted from `./backend`
-   Depends on db, redis, rabbitmq

### Celery Worker

-   Built from `./backend/Dockerfile`
-   Executes background tasks
-   Source code mounted from `./backend`
-   Depends on db, redis, rabbitmq

### Celery Beat

-   Built from `./backend/Dockerfile`
-   Schedules periodic tasks
-   Schedule persisted in Docker volume `celery_beat_data`
-   Depends on rabbitmq

## Local Development (Without Docker)

For local development without Docker, you need to run services
separately:

### Backend

``` bash
cd backend
poetry install --no-root
poetry run uvicorn src.main:app --reload --port 8000
```

### Backend Tests

Run the complete backend test suite from the `backend` directory:

``` bash
poetry run pytest
```

Use verbose output or run an individual test file:

``` bash
poetry run pytest -v
poetry run pytest tests/test_config.py
```

Application logs use readable console output in development and structured
JSON output in production. Both structlog and standard-library log records
use the centralized logging configuration.

### Frontend

Frontend development is not yet configured. The package.json has
dependencies but no build scripts. Frontend setup will be documented
when development begins.

### External Services

You must run PostgreSQL, Redis, and RabbitMQ locally or use cloud
services. Update `.env` with appropriate connection strings.

## Environment Variables

See `.env.example` for all available environment variables. Key
variables:

-   `ENVIRONMENT`: development/production
-   `DATABASE_URL`: PostgreSQL connection string
-   `REDIS_URL`: Redis connection string
-   `CELERY_BROKER_URL`: RabbitMQ connection string for Celery
-   `JWT_SECRET_KEY`: Secret for JWT signing
-   `RESEND_API_KEY`: Resend email API key (placeholder for development)
-   `FRONTEND_URL`: Frontend URL for CORS

## Troubleshooting

### Port Conflicts

If ports are already in use, modify the port mappings in
`docker-compose.yml` or stop conflicting services.

### Database Connection Issues

Ensure the database service is healthy before starting the API:

``` bash
docker compose up -d db
docker compose logs db
```

### RabbitMQ Connection Issues

Check RabbitMQ logs:

``` bash
docker compose logs rabbitmq
```

Access the management UI at <http://localhost:15672> to verify queues
and connections.

### Rebuilding Containers

After changes to `./backend/Dockerfile` or dependencies:

``` bash
docker compose build api celery_worker celery_beat
docker compose up -d
```

## Git Workflow

See [GIT_WORKFLOW.md](GIT_WORKFLOW.md) for the branching strategy and
pull request process.
