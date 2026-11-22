# ADR-0001: Backend Architecture — Modular Monolith and Clean Architecture

- **Status:** Accepted
- **Date:** 2026-11-22
- **Scope:** MVP

## Context

Cubiland needs a backend structure that supports several product areas while remaining practical to develop and deploy as an MVP. Distributed services would add operational complexity before independent scaling is needed.

## Decision

Build the backend as a **Modular Monolith** and organize it using **Clean Architecture** principles. Keep domain areas modular inside one deployable FastAPI application.

## Alternatives Considered

- **Microservices:** deferred because they add deployment, networking and observability overhead.
- **One unstructured application:** not selected because it weakens boundaries as the codebase grows.

## Consequences

**Benefits**
- Clear module boundaries with a simple deployment.
- Easier local development and transactions across modules.

**Trade-offs**
- Boundaries must be maintained through code structure and review.
- Modules are not independently deployable or scalable.

## Implementation Notes

Keep business rules independent of FastAPI and infrastructure details where practical. Separate domain, application, infrastructure and presentation concerns.

## Related Documents

- `../SYSTEM_ARCHITECTURE.md`
- `../BACKEND_ARCHITECTURE.md`
