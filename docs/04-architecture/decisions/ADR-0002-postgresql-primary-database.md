# ADR-0002: PostgreSQL as the Primary Database

- **Status:** Accepted
- **Date:** 2026-11-22
- **Scope:** MVP

## Context

Cubiland needs a reliable persistent store for users, profiles, learning progress, solves, courses, sessions and relational constraints.

## Decision

Use **PostgreSQL** as the primary persistent database. Access it through SQLAlchemy 2.0 AsyncIO and manage schema changes with Alembic.

## Alternatives Considered

- **Redis as the primary database:** not selected; Redis is intended for transient and cache workloads.
- **Separate databases for each module:** unnecessary for the MVP modular monolith.

## Consequences

**Benefits**
- Relational integrity, transactions and mature tooling.
- One authoritative store for application records.

**Trade-offs**
- Requires schema migrations, backups and database maintenance.

## Implementation Notes

Use UUID identifiers as defined in the domain model. Store solve duration as integer milliseconds (`BIGINT`). Use Alembic for versioned schema migrations.

## Related Documents

- `../SYSTEM_ARCHITECTURE.md`
- `../DOMAIN_AND_DATABASE.md`
- `../INFRASTRUCTURE_AND_DEVOPS.md`
