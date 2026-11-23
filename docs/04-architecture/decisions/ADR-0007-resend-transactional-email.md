# ADR-0007: Resend for Transactional Email

- **Status:** Accepted
- **Date:** 2026-11-22
- **Scope:** MVP

## Context

Cubiland requires transactional email for account verification and password recovery. The backend needs a provider that can be integrated through an API without operating its own mail server.

## Decision

Use **Resend** as the transactional email provider for the MVP. Email delivery is performed asynchronously through Celery to avoid blocking HTTP requests. The backend uses an EmailService abstraction to decouple business logic from the Resend provider.

## Alternatives Considered

- **Self-hosted mail server:** not selected for the MVP because operating mail delivery and sender reputation adds unnecessary work.
- **Other hosted providers:** not selected; Resend was chosen for its developer-oriented API and available free tier for early usage.

## Consequences

**Benefits**
- Simple API integration through Celery background tasks.
- Asynchronous email delivery avoids blocking HTTP requests.
- EmailService abstraction allows provider replacement.
- One provider can handle verification and password-reset messages.

**Trade-offs**
- Delivery depends on an external provider and its current plan limits.
- A verified sending domain and DNS configuration are required for production delivery.

## Implementation Notes

Store the Resend API key only in backend environment/secrets configuration. Use Resend for email verification, password reset and approved transactional notifications. Configure domain verification and DNS records, including SPF and DKIM, before production use. Recheck current provider limits before relying on a free plan.

## Related Documents

- `../AUTHENTICATION_AND_SECURITY.md`
- `../INFRASTRUCTURE_AND_DEVOPS.md`
