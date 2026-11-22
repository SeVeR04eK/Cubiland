# ADR-0006: Access and Refresh Token Transport and Lifetimes

- **Status:** Accepted
- **Date:** 2026-11-22
- **Scope:** MVP

## Context

The React frontend needs an authentication flow that supports short-lived API credentials and persistent login sessions while reducing exposure of long-lived credentials to browser JavaScript.

## Decision

Use a **JWT Access Token** signed with HS256 and valid for **15 minutes**. Keep it in React application memory and send it in the `Authorization: Bearer` header.

Use an opaque cryptographically random Refresh Token valid for **30 days**, delivered in an `HttpOnly`, `Secure`, `SameSite=Lax` Cookie. Do not store either token in `localStorage` or `sessionStorage`.

## Alternatives Considered

- **Store both tokens in localStorage:** not selected because persistent browser storage is accessible to JavaScript.
- **Send the Refresh Token as a readable header:** not selected because the chosen Cookie transport keeps it inaccessible to JavaScript.
- **Long-lived Access Tokens:** not selected because they delay the effect of credential compromise and revocation.

## Consequences

**Benefits**
- Short-lived Access Tokens limit exposure.
- HttpOnly Cookie prevents ordinary JavaScript access to the Refresh Token.
- In-memory Access Token avoids persistent browser storage.

**Trade-offs**
- Cookie authentication requires CSRF protection.
- Access Token loss on page reload requires a refresh request.
- Cookie attributes and same-site deployment must be configured consistently.

## Implementation Notes

Validate JWT signature, allowed algorithm, issuer, audience and time claims. Protect Cookie-authenticated state-changing endpoints with Origin validation and a CSRF token. Prefer serving frontend and API from the same site through Nginx.

## Related Documents

- `../API_DESIGN.md`
- `../AUTHENTICATION_AND_SECURITY.md`
- `../INFRASTRUCTURE_AND_DEVOPS.md`
