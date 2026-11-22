# ADR-0003: Redis for Caching and Rate-Limit State

- **Status:** Accepted
- **Date:** 2026-11-22
- **Scope:** MVP

## Context

Cubiland needs a fast store for temporary data such as cache entries and request-rate counters. Persistent business data and refresh-session records must remain authoritative in PostgreSQL.

## Decision

Use **Redis** for MVP caching and transient rate-limit state. Use SlowAPI with Redis-backed counters for API rate limiting. Redis is not the source of truth for application data or refresh-token sessions.

## Alternatives Considered

- **PostgreSQL for transient counters:** not selected because it mixes short-lived operational state with primary application data.
- **Redis as authoritative session storage:** not selected; session persistence and revocation belong in PostgreSQL.

## Consequences

**Benefits**
- Fast access to cache and rate-limit counters.
- Keeps transient state separate from durable records.

**Trade-offs**
- Cached values and counters may be lost if Redis is cleared or unavailable; the application must tolerate that.

## Implementation Notes

Treat cache entries as disposable and rebuildable. Do not store authoritative user, solve, learning-progress or refresh-session data only in Redis. Keep Redis inaccessible from the public internet.

## Related Documents

- `../SYSTEM_ARCHITECTURE.md`
- `../AUTHENTICATION_AND_SECURITY.md`
- `../INFRASTRUCTURE_AND_DEVOPS.md`
