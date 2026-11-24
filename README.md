# Cubiland

**Cubiland** is a speedcubing platform designed to help cubers learn, practice, track their performance, and improve their solving skills.

The platform is being developed around the **3×3×3 Rubik’s Cube** and the **CFOP method**, with a focus on structured learning, deliberate practice, performance analytics, and gamification.

[![Figma](https://img.shields.io/badge/Figma-Design-F24E1E?logo=figma&logoColor=white)](https://www.figma.com/design/koIB4YZF2P1bfkXj0xOpLa/Cubiland-%E2%80%94-UX-UI-Design?node-id=1-845&t=kjRGJoPFvCzcoXBv-1)

---

## Project Overview

Cubiland aims to bring the key parts of a cuber's training workflow into one platform:

- **Learn** — study solving methods and algorithms.
- **Practice** — train solving skills and work on specific areas.
- **Track** — record solves and monitor performance over time.
- **Improve** — use statistics and progress insights to guide training.

The product scope and interface are being developed alongside the technical implementation. Features listed here describe the intended platform, not necessarily functionality that is already implemented.

## Technology Stack

### Backend

- **Python 3.14**
- **FastAPI** — API framework
- **SQLAlchemy 2.x** — database toolkit and ORM
- **Alembic** — database migrations
- **PostgreSQL** — relational database
- **asyncpg** — asynchronous PostgreSQL driver
- **Pydantic Settings** — application configuration
- **Celery** — background task processing foundation
- **Redis** — caching and task-result backend foundation
- **RabbitMQ** — message broker

### Frontend

- **React 18**
- **React DOM**
- **TanStack Query** — server-state management
- **Zustand** — client-side state management

### Development & Infrastructure

- **Docker Compose** — local service orchestration
- **Poetry** — Python dependency management
- **Nginx** — planned reverse proxy for production deployment

## Architecture

The backend is organized around feature modules and separated into architectural layers:

- `domain` — domain models and business rules
- `application` — use cases and application logic
- `presentation` — API-facing components
- `infrastructure` — technical integrations and implementations

The initial module structure includes:

- Identity
- Solving
- Learning
- Statistics
- User Profiles
- Content Management

This structure establishes the foundation for implementation. It does not imply that these modules already contain completed business functionality.

## Repository Structure

```text
cubiland/
├── backend/
│   ├── alembic/
│   ├── src/
│   │   ├── infrastructure/
│   │   ├── modules/
│   │   │   ├── content_management/
│   │   │   ├── identity/
│   │   │   ├── learning/
│   │   │   ├── solving/
│   │   │   ├── statistics/
│   │   │   └── user_profiles/
│   │   └── shared/
│   ├── tests/
│   ├── Dockerfile
│   ├── pyproject.toml
│   └── poetry.lock
├── frontend/
│   ├── src/
│   │   ├── app/
│   │   ├── features/
│   │   ├── services/
│   │   └── shared/
│   ├── Dockerfile
│   └── package.json
├── docs/
├── nginx/
│   └── nginx.conf
└── docker-compose.yml
```

## Current Implementation

The repository currently contains the initial application and infrastructure scaffolding:

- A minimal FastAPI application with a `GET /health` health-check endpoint.
- A Poetry-managed backend project with its initial dependencies.
- Initial backend module and layer packages.
- A minimal Celery application placeholder. Broker configuration, task discovery, and application tasks are not implemented yet.
- A frontend package with the initial React and state-management dependencies. Frontend build tooling and application scripts are not configured yet.
- An Nginx configuration reserved for a future production deployment; it is not part of the current development Compose setup.

The core product functionality is still under development.

## Getting Started

### Prerequisites

- Python 3.14.x
- Poetry 2.x
- Docker Desktop with Docker Compose
- Node.js and npm (when starting frontend development)

### Backend

Open a terminal in the `backend/` directory and install the dependencies:

```bash
poetry install --no-root
```

The minimal API application can be started with:

```bash
poetry run uvicorn src.main:app --reload
```

The health-check endpoint is available at:

```text
http://127.0.0.1:8000/health
```

Expected response:

```json
{
  "status": "ok"
}
```

### Infrastructure

From the repository root, start the services defined in the Docker Compose configuration:

```bash
docker compose up -d
```

Check service status:

```bash
docker compose ps
```

Stop the services:

```bash
docker compose down
```

The backend's Celery integration is currently a placeholder; starting its container does not mean background task processing is fully configured.

## Documentation

Detailed project documentation is maintained in the [`docs/`](docs/) directory, including product discovery, requirements, design, architecture, and development-environment documentation.

## License

All rights reserved. See [`LICENSE`](LICENSE) for details.
