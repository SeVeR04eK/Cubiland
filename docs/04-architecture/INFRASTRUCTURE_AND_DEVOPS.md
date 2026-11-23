# Infrastructure and DevOps

**Project:** Cubiland  
**Document:** Infrastructure and DevOps  
**Status:** Defined for MVP  
**Scope:** MVP and post-release deployment evolution

## 1. Overview

This document defines the infrastructure, containerization, environments, CI workflow, deployment approach, backups, monitoring and operational requirements for Cubiland.

The MVP uses a single VPS and Docker Compose. The infrastructure is intentionally kept simple; horizontal scaling and a full orchestration platform are not required at this stage.

## 2. Infrastructure Decisions

| Area | MVP Decision |
|---|---|
| Hosting | Single VPS |
| Operating system | Ubuntu Server 24.04 LTS |
| Container runtime | Docker Engine |
| Container orchestration | Docker Compose V2 |
| Reverse proxy / web server | Nginx |
| Backend runtime | FastAPI + Uvicorn |
| Database | PostgreSQL |
| Cache and rate-limit storage | Redis |
| Message broker | RabbitMQ |
| Background task processor | Celery |
| Celery workers | Celery workers for task execution |
| Celery Beat | Celery Beat for scheduled tasks |
| Email provider | Resend |
| Media storage | S3-compatible Object Storage |
| CI | GitHub Actions |
| Production CD | Deferred until after initial release |
| TLS certificates | Let's Encrypt |
| Firewall | UFW |

The VPS provider, instance size, production domain and Object Storage provider are deployment choices and are not fixed by this document.

## 3. Environments

The MVP uses two environments.

### 3.1 Development

Development is used for local implementation and testing.

- Run services locally with Docker Compose.
- Use development environment variables and credentials.
- Use a separate development database and Redis instance.
- Do not use production secrets or production user data.
- Support application reload and developer tooling where appropriate.

### 3.2 Production

Production runs on the VPS.

- Use Ubuntu Server 24.04 LTS.
- Run services using a production Docker Compose configuration.
- Use production-only secrets and environment variables.
- Persist PostgreSQL data using Docker volumes.
- Keep PostgreSQL and Redis inaccessible from the public internet.
- Expose only the required HTTP/HTTPS ports through Nginx.

A separate staging environment is not required for the MVP. It may be introduced when release validation needs a production-like environment.

## 4. Production Architecture

The MVP production deployment contains the following containers:

| Container | Responsibility |
|---|---|
| `nginx` | Serves the frontend static build, terminates HTTPS and proxies `/api/` requests to FastAPI |
| `api` | Runs the FastAPI application using Uvicorn |
| `db` | Runs PostgreSQL and stores persistent application data |
| `redis` | Provides caching and transient rate-limit state |
| `rabbitmq` | Message broker for Celery background tasks |
| `celery_worker` | Executes queued background tasks |
| `celery_beat` | Schedules periodic tasks when required |

Media files are stored in an external S3-compatible Object Storage service and are not stored in the PostgreSQL container or the application container filesystem.

### 4.1 Network Exposure

- Nginx is the only application container exposed to the public network.
- Expose ports `80` and `443` as required for HTTP redirection and HTTPS.
- FastAPI is reachable by Nginx through an internal Docker network.
- PostgreSQL, Redis, and RabbitMQ are reachable only by services on the appropriate internal Docker network.
- Do not publish PostgreSQL, Redis, or RabbitMQ ports publicly.
- RabbitMQ management interface port (15672) is exposed only in development, not in production.
- Use separate internal networks where useful to limit unnecessary service-to-service access.

### 4.2 Backend Instances

Run one FastAPI application container/instance for the initial MVP.

Additional backend instances may be introduced when traffic, availability requirements or resource utilization justify scaling. Nginx can then proxy to multiple backend instances.

## 5. Docker and Docker Compose

Docker Compose V2 manages the MVP services.

Requirements:

- Maintain a development Compose configuration and a production Compose configuration or clearly separated Compose overrides.
- Use explicit image versions; avoid relying on floating `latest` tags in production.
- Build the application from maintained Dockerfiles.
- Use non-root users inside application containers where practical.
- Define service dependencies and health checks.
- Use restart policies appropriate for long-running production services.
- Persist PostgreSQL data in a named Docker volume.
- Do not rely on a container's writable filesystem for persistent application data.
- Keep secrets out of Docker images and source control.
- Apply resource limits/reservations after selecting the VPS size and measuring application requirements.

Redis data is transient for the MVP. Redis is not the source of truth for user sessions, refresh-token records or application data.

RabbitMQ data is persisted using Docker volumes to survive container restarts. Celery Beat scheduler state is also persisted.

## 6. Nginx and HTTPS

Nginx is responsible for:

- Serving the built React frontend.
- Forwarding `/api/` requests to the FastAPI service.
- Redirecting HTTP traffic to HTTPS.
- Terminating TLS.
- Setting appropriate proxy headers.
- Enforcing reasonable request body and timeout limits.
- Serving static assets efficiently.

HTTPS is mandatory in production.

Use Let's Encrypt for TLS certificates, with Certbot or an equivalent ACME client for certificate issuance and renewal. Certificate renewal must be automated and monitored.

The preferred deployment serves the frontend and API from the same site/origin. This simplifies browser Cookie behavior and reduces cross-origin configuration.

## 7. Configuration and Secrets

Application configuration is supplied through environment variables.

Requirements:

- Keep `.env` files out of Git.
- Commit only example files containing placeholders, such as `.env.example`.
- Use separate configuration and credentials for development and production.
- Store production secrets on the VPS with restricted file permissions or use a deployment secret manager.
- Never bake secrets into Docker images or frontend builds.
- Rotate credentials when compromise is suspected.

Secrets include, at minimum:

- PostgreSQL credentials.
- Redis credentials if enabled.
- RabbitMQ credentials.
- JWT signing secret.
- Resend API key.
- Object Storage credentials.

The frontend must receive only public configuration values. Backend secrets must never be included in frontend environment variables or static assets.

## 8. Continuous Integration

GitHub Actions is the selected CI platform.

### 8.1 Pull Request Workflow

CI runs for Pull Requests targeting `main`.

The workflow should perform:

1. Dependency installation.
2. Backend linting and formatting checks.
3. Backend type checking.
4. Backend automated tests.
5. Frontend linting and type checking.
6. Frontend automated tests where available.
7. Database migration validation.
8. Docker image build validation.

The exact commands are defined by the project's package scripts and tooling configuration.

### 8.2 Branch Protection

The `main` branch is protected.

- Feature and fix branches are merged through Pull Requests.
- Direct pushes to `main` are disabled for normal development.
- Required CI checks must pass before merge.
- A Pull Request review requirement may be enabled when additional collaborators are working on the project.

### 8.3 CI Scope Before Release

Before the initial release, CI validates code and build artifacts only.

CI does not automatically deploy to the production VPS. Production deployment is performed through a controlled manual release procedure until the post-release CD stage is introduced.

## 9. Deployment Strategy

### 9.1 Initial MVP Release

The initial production release uses a controlled manual deployment process:

1. Merge validated changes into `main`.
2. Select the release commit.
3. Build the production images.
4. Back up the production database if an existing production database is being upgraded.
5. Apply reviewed database migrations.
6. Start or update services with the production Compose configuration.
7. Verify container health and application endpoints.
8. Review application and Nginx logs.

Do not deploy unreviewed code directly to production.

### 9.2 Post-Release CI/CD

Automatic CD is deferred until after the initial release.

The planned post-release pipeline may:

1. Run CI checks.
2. Build versioned Docker images.
3. Push images to GitHub Container Registry (GHCR).
4. Connect to the VPS through a restricted SSH deployment identity.
5. Pull the selected image versions.
6. Apply database migrations as a controlled deployment step.
7. Update services through Docker Compose.
8. Run health checks.
9. Stop or roll back the release if deployment verification fails.

The post-release pipeline must use protected GitHub environment secrets and must not expose deployment credentials to untrusted Pull Request workflows.

## 10. Database Migrations

Alembic manages PostgreSQL schema migrations.

Requirements:

- Commit migration files to Git.
- Review generated migrations before applying them.
- Validate migrations in CI against a disposable/test database.
- Apply migrations as an explicit deployment step.
- Back up production data before migrations that may be destructive or difficult to reverse.
- Do not rely on application startup to silently create or alter production schema.
- Keep migrations compatible with the deployment sequence where possible.

For changes requiring multiple deployment steps, prefer an expand-and-contract migration approach so that the currently running application and the next application version can coexist safely.

## 11. Database Backups and Recovery

### 11.1 Backup Strategy

PostgreSQL is the primary persistent data store and must be backed up.

The MVP backup policy is:

- Create a daily PostgreSQL logical backup using `pg_dump`.
- Retain the latest 7 daily backups.
- Retain 4 weekly backups.
- Store backup copies outside the VPS in S3-compatible Object Storage.
- Protect backup access using separate credentials and restricted permissions.
- Encrypt backups in transit and at rest where supported.
- Do not store backup credentials in the application container.

### 11.2 Recovery Validation

- Periodically restore a backup into a separate test database.
- Verify that the restored database can be accessed and that expected tables and records are present.
- Document the restore procedure.
- Treat an untested backup as unverified.

Redis does not require a separate backup for the MVP because it stores transient cache and rate-limit state, not authoritative application data.

The backup schedule and retention policy should be reviewed as data volume and recovery requirements grow.

## 12. Monitoring and Logging

MVP monitoring uses built-in service health checks and logs rather than a dedicated Prometheus/Grafana stack.

### 12.1 Health Checks

- Define Docker health checks for services where meaningful.
- Check application readiness through a backend health endpoint.
- Ensure PostgreSQL health checks verify database readiness.
- Ensure Redis health checks verify that Redis responds.
- Ensure RabbitMQ health checks verify that the broker is accepting connections.
- Ensure Celery workers are running and able to process tasks.
- Use health status during manual deployment verification.

### 12.2 Logging

- Use Python application logging for backend events.
- Use Docker logging for container output.
- Use Nginx access and error logs.
- Prefer structured application logs.
- Configure Docker log rotation to prevent unbounded disk usage.
- Set appropriate log levels per environment.
- Avoid logging passwords, tokens, cookies, API keys or other secrets.

### 12.3 Additional Monitoring

Sentry, Prometheus and Grafana are not required for the initial MVP.

They may be introduced later when error tracking, metrics, alerting or operational visibility justify the additional services.

## 13. Server Security

The production VPS must follow basic host-hardening practices:

- Keep Ubuntu security updates current.
- Configure UFW to allow only required inbound ports, normally SSH, HTTP and HTTPS.
- Use SSH key authentication.
- Disable SSH password authentication after key access has been verified.
- Disable direct root SSH login.
- Restrict SSH access where practical.
- Use a non-root administrative account with controlled sudo access.
- Do not expose Docker daemon TCP access publicly.
- Restrict permissions on environment and backup files.
- Monitor disk usage, especially Docker images, logs and database volumes.

SSH configuration changes must be tested with an active recovery session before closing the existing connection.

## 14. Resource Management and Scaling

The initial deployment uses one VPS and one backend instance.

Exact CPU, RAM and disk limits depend on the selected VPS size and must be measured rather than guessed.

Operational requirements:

- Monitor CPU, memory and disk usage.
- Configure container log rotation.
- Set reasonable application worker and connection-pool settings for the available resources.
- Keep PostgreSQL and Redis internal.
- Review PostgreSQL storage growth and backup size.
- Scale vertically before introducing unnecessary infrastructure complexity.

If traffic or availability requirements increase, consider multiple API instances behind Nginx, managed PostgreSQL, managed Redis or a separate worker tier.

## 15. MVP and Future Infrastructure

| Capability | MVP | Post-Release / Future |
|---|---|---|
| Hosting | Single VPS | Reassess as usage grows |
| OS | Ubuntu Server 24.04 LTS | Upgrade through supported LTS path |
| Containers | Docker Engine + Compose V2 | Reassess only if orchestration needs grow |
| Reverse proxy | Nginx | Retain or reassess |
| Backend instances | One | Multiple if required |
| Environments | Development + Production | Add Staging if needed |
| CI | GitHub Actions on Pull Requests | Retain |
| Production CD | Manual controlled release | Automated deployment via GHCR and SSH |
| Database migrations | Alembic, explicit deployment step | Automated controlled migration stage |
| Backups | Daily + weekly retention, off-VPS | Reassess RPO/RTO and backup strategy |
| Monitoring | Health checks and logs | Add Sentry/metrics/alerting if justified |
| Background jobs | Celery + RabbitMQ for email tasks | Additional task types if required |

## 16. Remaining Deployment Decisions

These values are intentionally left configurable until the relevant infrastructure is selected:

| Decision | Status |
|---|---|
| VPS provider and instance size | Select before deployment |
| Production domain | Select before deployment |
| S3-compatible Object Storage provider | Select before media deployment |
| Exact CPU/RAM/disk limits | Set for selected VPS |
| Backup encryption and provider-specific lifecycle rules | Configure with storage provider |
| SSH source-IP restrictions | Configure for deployment environment |
| Exact application worker and DB pool sizes | Tune against VPS resources |
| Production alerting destination | Define if/when alerting is introduced |

## 17. Related Documents

- `SYSTEM_ARCHITECTURE.md`
- `BACKEND_ARCHITECTURE.md`
- `DOMAIN_AND_DATABASE.md`
- `API_DESIGN.md`
- `AUTHENTICATION_AND_SECURITY.md`
- `README.md`
- `decisions/ADR_TEMPLATE.md`
