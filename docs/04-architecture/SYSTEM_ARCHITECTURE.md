# System Architecture

**Project:** Cubiland  
**Document:** System Architecture  
**Status:** Approved architectural direction  
**Scope:** MVP

## 1. Overview

Cubiland is a web-based speedcubing platform designed to help users learn, practice, track their solving performance, and manage their learning progress.

The MVP follows a **Modular Monolith architecture** with **Clean Architecture principles** on the backend. The system consists of a React frontend, a FastAPI backend, PostgreSQL, Redis, and S3-compatible Object Storage.

The application is deployed on a single VPS using Docker Compose, with Nginx acting as the reverse proxy and frontend web server.

## 2. High-Level Architecture

The system consists of the following components:

| Component | Technology | Responsibility |
|---|---|---|
| Frontend | React, TypeScript, Vite | User interface and client-side interactions |
| Admin Panel | React | Course and lesson content management |
| Backend | Python, FastAPI | Business logic and API |
| Database | PostgreSQL | Persistent application data |
| ORM | SQLAlchemy 2.0 AsyncIO | Database access |
| Migrations | Alembic | Database schema migrations |
| Cache | Redis | Temporary cached data and rate limiting |
| Message Broker | RabbitMQ | Task queue and message routing for background jobs |
| Background Task Processor | Celery | Asynchronous task execution |
| Celery Workers | Celery | Execute queued background tasks |
| Celery Beat | Celery Beat | Scheduled periodic tasks |
| Email Provider | Resend | Transactional email delivery |
| Object Storage | S3-compatible storage | Images and learning materials |
| Web Server / Reverse Proxy | Nginx | Static file serving, HTTPS and API routing |
| Containerization | Docker | Application containerization |
| Orchestration | Docker Compose | Container lifecycle management |

## 3. Architecture Style

### 3.1 Backend — Modular Monolith

The backend follows a Modular Monolith architecture.

The application is deployed as a single backend service, while its internal structure is divided into independent business modules.

This approach provides:
- Clear separation of business responsibilities.
- Easier maintenance and testing.
- Lower operational complexity than microservices.
- Flexibility to evolve individual modules as the product grows.

### 3.2 Clean Architecture

The backend follows Clean Architecture principles.

The main architectural layers are:

- **Presentation Layer** — API endpoints, request validation and response handling.
- **Application Layer** — use cases and application orchestration.
- **Domain Layer** — business entities, rules and domain logic.
- **Infrastructure Layer** — database access, external services, caching and storage integrations.

Dependencies should point inward, keeping business logic independent of external frameworks and infrastructure.

## 4. Backend Modules

The backend is organized into business-oriented modules.

| Module | Responsibility |
|---|---|
| Identity & Access | Authentication, authorization and account management |
| User Profiles | User profile information |
| Learning | Courses, sections, lessons and learning progress |
| Content Management | Administrative course and lesson management |
| Solving | Timer-related solve records and solve history |
| Statistics | Performance metrics and solving statistics |

Modules should maintain clear boundaries and communicate through well-defined interfaces.

## 5. Frontend Architecture

### 5.1 Technology Stack

- React
- TypeScript
- Vite

The frontend is a single application containing both the user-facing platform and the administrative interface.

### 5.2 State Management

The frontend uses:

- **TanStack Query** — server state, API data fetching, caching and synchronization.
- **Zustand** — shared client-side and UI state.
- **React Hooks** — local component state and reusable component logic.
- **React Context** — shared state where appropriate.

### 5.3 Application Areas

The frontend contains two main areas:

- **User Application** — learning courses, timer, solve history, statistics and profile.
- **Admin Panel** — course, section and lesson management.

The administrative interface is available under `/admin` and protected by role-based authorization.

## 6. Database and Data Storage

### 6.1 PostgreSQL

PostgreSQL is the primary persistent data store and the source of truth for application data.

SQLAlchemy 2.0 with AsyncIO is used for database access. Alembic manages schema migrations.

### 6.2 Redis

Redis is included in the MVP for caching and rate limiting.

It is not the authoritative storage for user accounts, course content or solve records. Persistent application data remains in PostgreSQL.

### 6.3 RabbitMQ

RabbitMQ is the message broker for Celery background tasks.

It queues and routes task messages between the FastAPI application and Celery workers. RabbitMQ ensures reliable task delivery and supports retry behavior for failed tasks.

RabbitMQ is not used as a cache or for persistent application data.

### 6.4 Celery Background Tasks

Celery executes asynchronous background tasks for operations that should not block HTTP requests.

Primary use cases:
- Email delivery (verification, password reset, security notifications)
- Future scheduled maintenance tasks
- Future expensive background calculations

Celery workers run independently of the FastAPI HTTP server. Tasks are queued through RabbitMQ and executed by workers. Celery Beat handles scheduled periodic tasks when required.

### 6.5 Resend Email

Resend is the transactional email provider for the MVP.

It delivers:
- Email verification messages
- Password reset emails
- Security-related notifications
- Other transactional emails when needed

Email delivery is performed asynchronously through Celery tasks to avoid blocking HTTP requests.

### 6.6 Object Storage

An S3-compatible Object Storage service is used for images and learning materials.

PostgreSQL stores the relevant metadata and storage references, while the actual files are stored in Object Storage.

The specific storage provider is TBD.

## 7. API Communication

The frontend communicates with the backend through a REST API.

- Data format: JSON.
- Transport: HTTPS.
- API version prefix: `/api/v1`.
- Backend framework: FastAPI.

WebSockets are not required for the MVP.

The timer runs on the client side. Completed solve results are sent to the backend for persistence and subsequent statistical analysis.

## 8. Authentication and Authorization

The application uses JWT-based authentication:

- Access Tokens.
- Refresh Tokens.

The system supports role-based access control.

At minimum, the following roles are required:

- **User** — access to standard platform functionality.
- **Admin** — access to administrative course and lesson management.

Token lifecycle, storage, rotation and revocation policies are specified in `AUTHENTICATION_AND_SECURITY.md`.

## 9. Admin Panel and Content Management

The MVP includes a basic administrative interface integrated into the main React application.

Administrators can:

- Create, edit and delete courses.
- Manage course sections and lessons.
- Add and edit lesson content.
- Upload images and learning materials.
- Change the order of sections and lessons.
- Preview lessons.
- Publish and unpublish courses and lessons.

All administrative operations are performed through protected backend API endpoints.

## 10. Infrastructure and Deployment

### 10.1 Deployment Model

The MVP is deployed on a single VPS.

Docker Compose manages the application containers.

The specific VPS provider is TBD.

### 10.2 Nginx

Nginx acts as the single public entry point.

Its responsibilities include:

- Serving the built React frontend.
- Reverse proxying API requests to FastAPI.
- Handling HTTPS.
- Routing incoming requests.

### 10.3 Deployment Components

The deployment consists of:

- Nginx
- React frontend static build
- FastAPI backend
- PostgreSQL
- Redis
- RabbitMQ
- Celery workers
- Celery Beat (if periodic tasks are required)

Object Storage is accessed as an external service.

## 12. High-Level Request Flow

### 12.1 Standard API Request

1. The user interacts with the React frontend.
2. React sends an HTTPS request to the API.
3. Nginx forwards the request to FastAPI.
4. FastAPI processes the request through the appropriate application module.
5. The application accesses PostgreSQL and, when appropriate, Redis or Object Storage.
6. FastAPI returns a JSON response.
7. React updates the interface.

### 12.2 Solve Recording

1. The user completes a solve using the client-side timer.
2. The frontend sends the completed solve to the backend.
3. The backend validates and persists the solve in PostgreSQL.
4. The frontend receives the response and updates the solve history and relevant statistics.

### 12.3 Course Content Management

1. An administrator accesses `/admin`.
2. The backend verifies authentication and administrative permissions.
3. The administrator creates or edits course content.
4. The backend validates and persists the content in PostgreSQL.
5. Uploaded media files are stored in Object Storage.
6. Published content becomes available to users through the learning interface.

### 12.4 Email Delivery (Background Task)

1. The user performs an action requiring email (registration, password reset).
2. FastAPI processes the request and generates the necessary token.
3. The application queues a Celery task with the email payload.
4. RabbitMQ receives and stores the task message.
5. A Celery worker picks up the task.
6. The worker calls the EmailService abstraction.
7. The EmailService uses the Resend provider to send the email.
8. The task completes with success or is retried on transient failures.

## 13. Architectural Principles

The system follows these principles:

- **Simplicity First** — avoid unnecessary infrastructure and architectural complexity in the MVP.
- **Modular Design** — organize backend functionality around clear business responsibilities.
- **Separation of Concerns** — isolate domain logic from frameworks and infrastructure.
- **Single Source of Truth** — PostgreSQL remains the authoritative persistent data store.
- **Security by Design** — protect user data and administrative operations.
- **Extensibility** — allow future features and infrastructure components without requiring a complete architectural redesign.

## 14. Future Scalability

The architecture allows future evolution, including:

- Additional learning methods and course types.
- More advanced statistics and performance analysis.
- Expanded administrative capabilities.
- Additional application modules.
- Infrastructure scaling when required by actual traffic.

Microservices and Kubernetes are not part of the MVP architecture.

## 15. Related Documents

- `BACKEND_ARCHITECTURE.md`
- `DOMAIN_AND_DATABASE.md`
- `API_DESIGN.md`
- `AUTHENTICATION_AND_SECURITY.md`
- `INFRASTRUCTURE_AND_DEVOPS.md`
- `README.md`