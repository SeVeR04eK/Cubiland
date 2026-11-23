# ADR-0012: RabbitMQ as Message Broker

- **Status:** Accepted
- **Date:** 2026-11-23
- **Scope:** MVP

## Context

Cubiland requires a reliable message broker to queue and route background tasks between the FastAPI application and Celery workers. The broker must support task persistence, retry behavior, and reliable delivery to prevent task loss during worker restarts or temporary failures.

## Decision

Use **RabbitMQ** as the message broker for Celery background tasks. RabbitMQ queues and routes task messages, ensuring reliable delivery and supporting retry behavior for failed tasks.

## Alternatives Considered

- **Redis as broker:** not selected because Redis is already used for caching and rate limiting; using it as a broker would conflate responsibilities and lose task durability on restart.
- **Kafka:** not selected due to operational complexity for MVP requirements.
- **SQS:** not selected to avoid external service dependency for the initial MVP.

## Consequences

**Benefits**
- Reliable task persistence survives broker restarts.
- Built-in retry and dead-letter queue capabilities.
- Mature, battle-tested message broker.
- Clear separation of concerns: Redis for caching, RabbitMQ for messaging.
- Supports task routing and prioritization if needed later.

**Trade-offs**
- Additional infrastructure component to operate.
- Requires disk space for message persistence.
- Management interface adds operational surface (exposed only in development).

## Implementation Notes

### Configuration

- **Broker URL:** Configured via `CELERY_BROKER_URL` environment variable.
- **Virtual host:** Configurable via `RABBITMQ_VHOST`.
- **Authentication:** Username and password via environment variables.
- **Persistence:** RabbitMQ data persisted in Docker volume.
- **Management interface:** Port 15672 exposed only in development, not in production.

### Network Security

- RabbitMQ is reachable only by services on the internal Docker network.
- Do not publish RabbitMQ ports publicly in production.
- Management interface is disabled or not exposed in production.

### Task Reliability

- Tasks are persisted until acknowledged by a worker.
- Unacknowledged tasks are re-queued on worker failure.
- Supports retry policies configured in Celery.
- No Dead Letter Queue required for MVP; failed tasks are logged.

### Integration with Celery

- Celery connects to RabbitMQ using AMQP protocol.
- Task serialization uses JSON (not pickle).
- Task queues can be organized by domain or priority if needed.
- Celery workers auto-reconnect on connection failure.

## Related Documents

- `../BACKEND_ARCHITECTURE.md`
- `../INFRASTRUCTURE_AND_DEVOPS.md`
- `ADR-0011: Celery for Background Task Processing`
