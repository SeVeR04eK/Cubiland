# ADR-0008: Single VPS and Docker Compose for the MVP

- **Status:** Accepted
- **Date:** 2026-11-22
- **Scope:** MVP

## Context

The MVP needs a production environment that is straightforward to operate without introducing orchestration complexity before traffic and availability requirements are known.

## Decision

Deploy the MVP on a **single VPS running Ubuntu Server 24.04 LTS**, using Docker Engine and Docker Compose V2. Use Nginx, one FastAPI instance, PostgreSQL and Redis as the primary containers.

## Alternatives Considered

- **Kubernetes or another cluster orchestrator:** not selected because the MVP does not require multi-node orchestration.
- **Multiple VPS instances:** deferred until availability or scaling requirements justify them.

## Consequences

**Benefits**
- Simple deployment and operational model.
- Clear separation of services through containers.
- Low infrastructure overhead for the MVP.

**Trade-offs**
- The VPS is a single point of failure.
- Scaling and high availability are limited until the architecture is expanded.

## Implementation Notes

Expose Nginx publicly; keep FastAPI, PostgreSQL and Redis on internal Docker networks. Persist PostgreSQL data in Docker volumes. Use Let's Encrypt for HTTPS. Configure UFW and SSH key-based access. Keep Development and Production separate; staging is deferred.

## Related Documents

- `../SYSTEM_ARCHITECTURE.md`
- `../INFRASTRUCTURE_AND_DEVOPS.md`
