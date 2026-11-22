# Architecture Decision Records (ADRs)

**Project:** Cubiland  
**Status:** Accepted decisions for the MVP

This directory records the main architectural decisions made for Cubiland. Each ADR briefly explains its context, decision, alternatives and consequences.

## ADR Index

| ADR | Decision | Status |
|---|---|---|
| [ADR-0001](ADR-0001-modular-monolith-clean-architecture.md) | Backend: Modular Monolith + Clean Architecture | Accepted |
| [ADR-0002](ADR-0002-postgresql-primary-database.md) | PostgreSQL as the primary database | Accepted |
| [ADR-0003](ADR-0003-redis-cache-and-rate-limiting.md) | Redis for caching and rate-limit state | Accepted |
| [ADR-0004](ADR-0004-refresh-session-persistence.md) | Refresh sessions in PostgreSQL; token hashes only | Accepted |
| [ADR-0005](ADR-0005-refresh-token-rotation-and-revocation.md) | Refresh Token Rotation, reuse detection and revocation | Accepted |
| [ADR-0006](ADR-0006-token-transport-and-lifetimes.md) | Access/Refresh Token transport and lifetimes | Accepted |
| [ADR-0007](ADR-0007-resend-transactional-email.md) | Resend for transactional email | Accepted |
| [ADR-0008](ADR-0008-single-vps-docker-compose.md) | Single VPS with Ubuntu and Docker Compose | Accepted |
| [ADR-0009](ADR-0009-github-actions-ci-and-deferred-cd.md) | GitHub Actions CI; defer automatic production CD | Accepted |
| [ADR-0010](ADR-0010-s3-compatible-media-storage.md) | S3-compatible Object Storage for media | Accepted |

## Statuses

- **Proposed** — under discussion; not approved.
- **Accepted** — approved and used as the current direction.
- **Deprecated** — no longer recommended, retained for history.
- **Superseded** — replaced by a later ADR.

When an accepted decision changes, create a new ADR and mark the earlier record as superseded. Do not silently rewrite decision history.

## Related Architecture Documents

- `../SYSTEM_ARCHITECTURE.md`
- `../BACKEND_ARCHITECTURE.md`
- `../DOMAIN_AND_DATABASE.md`
- `../API_DESIGN.md`
- `../AUTHENTICATION_AND_SECURITY.md`
- `../INFRASTRUCTURE_AND_DEVOPS.md`
