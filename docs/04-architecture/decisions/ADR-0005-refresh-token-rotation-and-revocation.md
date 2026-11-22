# ADR-0005: Refresh Token Rotation, Reuse Detection and Revocation

- **Status:** Accepted
- **Date:** 2026-11-22
- **Scope:** MVP

## Context

A long-lived Refresh Token can be stolen and replayed. Cubiland needs a way to invalidate old tokens, detect reuse and terminate affected sessions.

## Decision

Use **Refresh Token Rotation** on every successful refresh. Detect reuse of a previously rotated token and revoke the associated token family. Support current-session logout, logout-all and security-driven revocation. Perform rotation atomically in a PostgreSQL transaction.

## Alternatives Considered

- **Reusable long-lived Refresh Tokens:** not selected because a stolen token could remain usable until expiry.
- **Rotation without reuse detection:** not selected because replay of an old token would be harder to respond to.

## Consequences

**Benefits**
- Limits the useful lifetime of a stolen token and detects replay.
- Supports explicit session termination and security response.

**Trade-offs**
- Requires concurrency-safe transactional logic.
- Reuse detection may revoke the affected token family and require re-authentication.

## Implementation Notes

Invalidate the presented token and persist its replacement as one atomic operation. Use row locking or an equivalent conditional update to prevent concurrent successful rotation. Revoke the token family when reuse is detected. Revoke all user sessions after password reset or password change.

## Related Documents

- `../DOMAIN_AND_DATABASE.md`
- `../API_DESIGN.md`
- `../AUTHENTICATION_AND_SECURITY.md`
