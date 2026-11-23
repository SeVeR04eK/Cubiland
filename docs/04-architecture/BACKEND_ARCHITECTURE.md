# Backend Architecture

**Project:** Cubiland  
**Document:** Backend Architecture  
**Status:** Approved architectural direction  
**Scope:** MVP

## 1. Overview

The Cubiland backend is built with Python and FastAPI using a Modular Monolith architecture combined with Clean Architecture principles.

The backend is deployed as a single application but internally separated into independent business modules.

The architecture aims to provide:

- Clear separation of responsibilities.
- Maintainable and testable business logic.
- Explicit module boundaries.
- Independent development of business capabilities.
- Extensibility for future functionality.

The backend is responsible for business logic, authentication, authorization, data persistence, course management, solve recording and statistics.

## 2. Technology Stack

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| FastAPI | Backend framework and REST API |
| Uvicorn | ASGI server |
| SQLAlchemy 2.0 AsyncIO | Asynchronous database access |
| PostgreSQL | Primary relational database |
| Alembic | Database migrations |
| Redis | Caching and rate limiting |
| RabbitMQ | Message broker for background tasks |
| Celery | Background task processing |
| Celery Beat | Scheduled periodic tasks |
| Resend | Transactional email delivery |
| Pydantic | Data validation and serialization |
| JWT | Authentication |
| Docker | Containerization |
| Docker Compose | Local and production service orchestration |

## 3. Architectural Style

### 3.1 Modular Monolith

The application follows a Modular Monolith architecture.

All backend modules are part of one deployable application and run within the same backend service.

Each module is responsible for a specific business area and should encapsulate its own:

- Business logic.
- Application use cases.
- Data access requirements.
- API endpoints.
- Validation rules.

Modules should avoid direct dependencies on the internal implementation of other modules.

Communication between modules should happen through clearly defined interfaces and application-level operations.

### 3.2 Clean Architecture

The backend follows Clean Architecture principles.

The application is divided into four main layers:

1. Presentation
2. Application
3. Domain
4. Infrastructure

Dependencies point inward, toward the Domain Layer.

The Domain Layer must not depend on FastAPI, SQLAlchemy, Redis or other infrastructure technologies.

## 4. Application Layers

### 4.1 Presentation Layer

**Responsibility:** Handle incoming HTTP requests and outgoing responses.

Contains:

- FastAPI routers.
- API endpoints.
- Request and response schemas.
- Dependency injection.
- Authentication and authorization integration.
- HTTP-specific exception handling.

The Presentation Layer should not contain business logic.

Its responsibility is to validate incoming data, invoke application use cases and return appropriate HTTP responses.

### 4.2 Application Layer

**Responsibility:** Coordinate application operations and implement use cases.

Contains:

- Use cases.
- Application services.
- DTOs where required.
- Repository interfaces.
- Application-level validation.
- Transaction orchestration.

Examples:

- RegisterUser
- AuthenticateUser
- CreateCourse
- UpdateLesson
- RecordSolve
- GetUserStatistics

The Application Layer coordinates domain behavior and infrastructure abstractions without depending directly on framework-specific implementations.

### 4.3 Domain Layer

**Responsibility:** Represent core business concepts and enforce business rules.

Contains:

- Domain entities.
- Value objects.
- Domain services.
- Business rules.
- Domain exceptions.
- Repository interfaces.

The Domain Layer is independent of external frameworks and infrastructure.

Business rules should be implemented here whenever they belong to the domain rather than HTTP handling or persistence.

### 4.4 Infrastructure Layer

**Responsibility:** Provide implementations for external technical dependencies.

Contains:

- SQLAlchemy models.
- Repository implementations.
- Database configuration.
- Database session management.
- Redis integration.
- RabbitMQ integration.
- Celery application initialization and configuration.
- Celery task definitions.
- Email service implementation (Resend provider).
- Email templates.
- Object Storage integration.
- External service integrations.
- Security-related infrastructure implementations.

Infrastructure implementations satisfy interfaces defined by the inner application layers.

Background task infrastructure is organized separately to maintain clean boundaries:
- Celery application setup belongs in the infrastructure layer.
- Task definitions are organized by domain module.
- Email service abstraction allows provider replacement.

## 5. Backend Business Modules

The backend is divided into the following modules.

### 5.1 Identity & Access

Responsible for user identity and access management.

Main responsibilities:

- User registration.
- User authentication.
- Access Token generation.
- Refresh Token handling.
- Password management.
- Role-based authorization.
- Account-related operations.
- Email verification token generation and validation.
- Password reset token generation and validation.
- Scheduling email delivery tasks through Celery.

### 5.2 User Profiles

Responsible for user profile information.

Main responsibilities:

- Retrieving user profiles.
- Updating profile information.
- Managing user-specific profile data.

### 5.3 Learning

Responsible for the learning experience.

Main responsibilities:

- Retrieving available courses.
- Retrieving course sections.
- Retrieving lessons.
- Managing learning progress.
- Recording completed lessons.
- Providing course content to users.

### 5.4 Content Management

Responsible for administrative course content management.

Main responsibilities:

- Creating and editing courses.
- Managing course sections.
- Creating and editing lessons.
- Managing lesson ordering.
- Managing publication status.
- Managing learning materials and media references.

Administrative operations must require appropriate permissions.

### 5.5 Solving

Responsible for solve records and solving history.

Main responsibilities:

- Recording completed solves.
- Retrieving solve history.
- Managing solve records.
- Validating solve-related data.
- Supporting solve-related operations.

The timer itself runs on the frontend. The backend receives and persists completed solve records.

### 5.6 Statistics

Responsible for analyzing user solving performance.

Main responsibilities:

- Calculating performance metrics.
- Providing personal best results.
- Calculating averages.
- Providing statistics over selected periods.
- Supporting statistics visualization in the frontend.

Statistics must be based on persisted solve records and follow consistent calculation rules.

## 6. Module Boundaries and Dependencies

Modules should remain logically independent.

The following rules apply:

- A module owns its business logic.
- A module should not directly manipulate another module's database models.
- Cross-module operations should use defined interfaces or application-level services.
- Shared functionality should be introduced only when it represents genuinely common behavior.
- Circular dependencies between modules must be avoided.

Examples:

- Learning provides course and lesson information to the user-facing application.
- Content Management manages course content through its own administrative operations.
- Solving owns solve records.
- Statistics uses solve data through an explicitly defined module interface.

## 7. Database Access

The backend uses SQLAlchemy 2.0 with AsyncIO for asynchronous database access.

### 7.1 Database Interaction

- PostgreSQL is the primary database.
- SQLAlchemy provides ORM functionality.
- Alembic manages database schema migrations.
- Database operations use asynchronous SQLAlchemy APIs.
- Database sessions are managed through application dependencies and appropriate transaction boundaries.

### 7.2 Repository Pattern

The application uses the Repository Pattern to separate business operations from persistence details.

Repository interfaces are defined in the inner layers.

Their SQLAlchemy-based implementations belong to the Infrastructure Layer.

Use cases should depend on repository abstractions rather than directly accessing SQLAlchemy models.

### 7.3 Transactions

Database transactions should be managed at the application use-case boundary where appropriate.

Operations that must succeed or fail together should be executed within a single transaction.

## 8. API Layer

FastAPI provides the HTTP API.

API endpoints should:

- Validate request data.
- Enforce authentication and authorization.
- Invoke application use cases.
- Return structured responses.
- Use appropriate HTTP status codes.
- Avoid containing business logic.

The API uses JSON for request and response payloads.

The versioned API prefix is:

`/api/v1`

Detailed endpoint definitions, schemas and response conventions are specified in `API_DESIGN.md`.

## 9. Dependency Injection

FastAPI dependency injection is used to provide application dependencies.

Examples include:

- Database sessions.
- Repository implementations.
- Application use cases.
- Authentication context.
- Authorization dependencies.

Dependency configuration should remain organized and should not introduce unnecessary coupling between modules.

## 10. Authentication and Authorization

Authentication uses JWT Access Tokens and Refresh Tokens.

Authorization is based on user roles and permissions.

The MVP requires at least:

- User
- Admin

Administrative use cases must verify that the authenticated user has the required administrative permissions.

Detailed token lifecycle, refresh handling, password security and authorization policies are defined in `AUTHENTICATION_AND_SECURITY.md`.

## 11. Caching

Redis is included in the MVP for caching and rate limiting.

The backend may use caching for frequently accessed data when appropriate.

Caching rules should account for:

- Cache expiration.
- Cache invalidation.
- Data consistency.
- Cache failures.
- Avoiding stale course or user information.

Redis must not replace PostgreSQL as the source of truth for persistent application data.

Caching should be introduced selectively rather than applied to every database operation.

## 12. Background Task Processing

### 12.1 Celery and RabbitMQ

Celery and RabbitMQ are part of the MVP infrastructure for asynchronous task execution.

**Responsibilities:**

- Celery executes background tasks independently of HTTP request processing.
- RabbitMQ acts as the message broker, queuing and routing task messages.
- Celery Workers pick up and execute queued tasks.
- Celery Beat schedules periodic tasks when required.

**Configuration:**

- Broker: RabbitMQ (not Redis).
- Serialization: JSON (not pickle).
- Task acknowledgement: Enabled.
- Retry policy: Bounded retries with exponential backoff for transient failures.
- Worker concurrency: Configurable based on available resources.
- Result backend: Not required for email tasks; results are ignored where not needed.

### 12.2 Email Service Architecture

The backend uses an EmailService abstraction to decouple business logic from the email provider.

**Architecture:**

- Application layer queues email tasks through Celery.
- Celery workers execute email tasks.
- Workers call the EmailService abstraction.
- EmailService implementation uses the Resend provider.
- Email templates are separated from business logic.

**Requirements:**

- Support HTML and plain-text email content.
- Handle provider errors and temporary delivery failures.
- Implement retry behavior through Celery.
- Never log passwords, reset tokens, verification tokens, or API keys.
- The backend must not depend directly on Resend throughout the application.

### 12.3 Task Reliability

**Error Handling:**

- Temporary Resend API failures: Retry with exponential backoff.
- Network timeouts: Retry with bounded attempts.
- RabbitMQ connection failures: Workers reconnect automatically.
- Worker restarts: Tasks are re-queued from RabbitMQ.
- Retry exhaustion: Failed tasks are logged for investigation.

**Idempotency:**

- Email tasks should be idempotent where practical.
- Duplicate task execution is possible (at-least-once delivery).
- Token validation and consumption happen in the backend to prevent misuse.

**Dead Letter Queue:**

- A Dead Letter Queue is not required for the MVP.
- Failed tasks are logged and monitored through Celery/worker logs.

## 13. Error Handling and Logging

The backend should implement consistent error handling.

Requirements:

- Centralized HTTP exception handling.
- Consistent API error response structure.
- Appropriate logging of application errors.
- Separation of internal errors from public API messages.
- No exposure of sensitive information in error responses or logs.

Business exceptions should be distinguishable from infrastructure and unexpected application errors.

## 14. Testing Strategy

The backend should support multiple testing levels.

### 14.1 Unit Tests

Test individual domain rules and application use cases.

Unit tests should avoid unnecessary external infrastructure dependencies.

### 14.2 Integration Tests

Test interactions with:

- PostgreSQL.
- Repository implementations.
- Redis where applicable.
- RabbitMQ and Celery task execution.
- Email service integration.
- Application module integrations.

### 14.3 API Tests

Test HTTP endpoints, including:

- Request validation.
- Response structures.
- Authentication.
- Authorization.
- Error handling.
- Main application workflows.

## 15. Backend Design Principles

The following principles guide backend implementation:

- **Single Responsibility** — each component should have a clearly defined responsibility.
- **Dependency Inversion** — inner layers must not depend on infrastructure implementations.
- **Encapsulation** — modules should protect their internal implementation.
- **Explicit Interfaces** — module interactions should be clearly defined.
- **Testability** — business logic should be testable independently of external infrastructure.
- **Pragmatism** — avoid unnecessary abstractions and complexity.
- **Consistency** — follow common patterns across modules.

## 16. Related Documents

- `SYSTEM_ARCHITECTURE.md`
- `DOMAIN_AND_DATABASE.md`
- `API_DESIGN.md`
- `AUTHENTICATION_AND_SECURITY.md`
- `INFRASTRUCTURE_AND_DEVOPS.md`
- `README.md`