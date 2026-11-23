# ADR-0011: Celery for Background Task Processing

- **Status:** Accepted
- **Date:** 2026-11-23
- **Scope:** MVP

## Context

Cubiland requires asynchronous background task execution for operations that should not block HTTP requests, particularly email delivery for account verification and password reset. The backend needs a reliable task processing system that can handle retries, scheduling, and independent execution from the HTTP server.

## Decision

Use **Celery** as the background task processing framework for the MVP. Celery workers execute tasks asynchronously, decoupling time-consuming operations from HTTP request handling.

## Alternatives Considered

- **FastAPI BackgroundTasks:** not selected because tasks are tied to the HTTP request lifecycle and do not survive server restarts.
- **RQ (Redis Queue):** not selected; Celery provides more mature scheduling and retry capabilities.
- **Custom background threads:** not selected due to complexity in reliability, monitoring, and scaling.

## Consequences

**Benefits**
- Asynchronous task execution prevents HTTP request blocking.
- Independent worker processes can be scaled separately from the API.
- Built-in retry mechanisms with exponential backoff.
- Celery Beat supports scheduled periodic tasks.
- Clean separation between application logic and task execution.

**Trade-offs**
- Additional operational complexity with worker processes.
- Requires a message broker (RabbitMQ).
- Task execution is at-least-once, not exactly-once.

## Implementation Notes

### Configuration

- **Broker:** RabbitMQ (not Redis).
- **Serialization:** JSON (not pickle for security).
- **Task acknowledgement:** Enabled.
- **Retry policy:** Bounded retries with exponential backoff for transient failures.
- **Worker concurrency:** Configurable based on available resources.
- **Result backend:** Not required for email tasks; results are ignored where not needed.

### Architecture

- Celery application initialization belongs in the infrastructure layer.
- Task definitions are organized by domain module.
- Application layer queues tasks through Celery.
- Workers execute tasks and call appropriate services (e.g., EmailService).
- Celery-specific code must not leak into domain logic.

### Task Reliability

- Temporary Resend API failures: Retry with exponential backoff.
- Network timeouts: Retry with bounded attempts.
- RabbitMQ connection failures: Workers reconnect automatically.
- Worker restarts: Tasks are re-queued from RabbitMQ.
- Retry exhaustion: Failed tasks are logged for investigation.
- Email tasks should be idempotent where practical.
- A Dead Letter Queue is not required for the MVP.

### Primary Use Cases

- Email delivery (verification, password reset, security notifications).
- Future scheduled maintenance tasks.
- Future expensive background calculations.

## Related Documents

- `../BACKEND_ARCHITECTURE.md`
- `../AUTHENTICATION_AND_SECURITY.md`
- `../INFRASTRUCTURE_AND_DEVOPS.md`
- `ADR-0012: RabbitMQ as Message Broker`
