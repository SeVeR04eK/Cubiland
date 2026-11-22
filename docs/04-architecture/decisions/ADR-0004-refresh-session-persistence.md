# ADR-0004: Refresh Session Persistence in PostgreSQL

- **Status:** Accepted
- **Date:** 2026-11-22
- **Scope:** MVP

## Context

Refresh Tokens must support persistent session tracking, logout, revocation and reuse detection. The system needs to validate current session state rather than relying only on token expiry.

## Decision

Persist refresh-session/token records in **PostgreSQL**. Store only a cryptographic hash of each Refresh Token; never store the plaintext token.

## Alternatives Considered

- **Redis-only session persistence:** not selected because PostgreSQL is the durable source of truth for session lifecycle.
- **Plaintext token storage:** rejected because a database leak would expose usable Refresh Tokens.

## Consequences

**Benefits**
- Durable session records and transactional updates.
- A database leak does not directly reveal reusable plaintext Refresh Tokens.

**Trade-offs**
- Refresh validation requires a database lookup or a carefully invalidated cache.
- Token hashing and lookup add work to the refresh flow.

## Implementation Notes

Use the `UserSession`/session model described in `../DOMAIN_AND_DATABASE.md`. Associate records with a user and token family. Track expiration and revocation state. Never log token values or hashes.

## Related Documents

- `../DOMAIN_AND_DATABASE.md`
- `../AUTHENTICATION_AND_SECURITY.md`
