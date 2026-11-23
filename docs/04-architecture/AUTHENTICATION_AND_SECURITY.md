# Authentication and Security

**Project:** Cubiland  
**Document:** Authentication and Security  
**Status:** Defined for MVP  
**Scope:** MVP

## 1. Overview

This document defines authentication, session management, authorization and application security requirements for Cubiland.

The backend is responsible for credential verification, token issuance, session lifecycle, email verification, password recovery and access control.

### 1.1 Security Principles

- Apply defense in depth.
- Never store plaintext passwords or refresh tokens.
- Keep authentication and authorization decisions on the backend.
- Use short-lived Access Tokens and rotating Refresh Tokens.
- Revoke sessions when credentials or account security are compromised.
- Do not expose secrets or sensitive authentication data in API responses or logs.
- Validate all untrusted input.
- Use HTTPS in production.

## 2. Password Security

### 2.1 Password Hashing

Passwords are hashed using **Argon2id**.

Requirements:

- Use a maintained Argon2id implementation.
- Generate a unique cryptographically random salt for each password.
- Store the encoded password hash, including the algorithm parameters and salt.
- Never store plaintext passwords.
- Never log passwords.
- Verify passwords using the password-hashing library's verification function.
- Rehash passwords on successful login when stored parameters are outdated.

Argon2id parameters must be configurable and selected for the production environment using current security guidance and deployment resources.

### 2.2 Password Policy

MVP password requirements:

- Minimum length: 8 characters.
- Maximum length: 128 characters.
- Allow long passphrases.
- Do not require arbitrary combinations of uppercase letters, digits or special characters.
- Reject commonly used and known-compromised passwords.
- Do not silently truncate passwords.

The same policy applies to registration and password reset.

## 3. JWT Access Tokens

### 3.1 Configuration

| Property | Decision |
|---|---|
| Token type | JWT Access Token |
| Signing algorithm | HS256 |
| Lifetime | 15 minutes |
| Transport | `Authorization: Bearer <token>` |
| Frontend storage | In-memory only |

The signing secret must be generated using a cryptographically secure random generator, stored outside source control and supplied through environment configuration. It must not be reused for unrelated cryptographic purposes.

### 3.2 Claims

Access Tokens include the following claims:

| Claim | Purpose |
|---|---|
| `sub` | User UUID |
| `sid` | Current session UUID |
| `iss` | Expected token issuer |
| `aud` | Expected API audience |
| `iat` | Issued-at timestamp |
| `exp` | Expiration timestamp |
| `jti` | Unique token identifier |

The backend validates the signature, allowed algorithm, issuer, audience, expiration and required claims. The backend must not trust a token merely because it can be decoded.

The user's current role and account status must be enforced by backend authorization logic. Role changes must not depend solely on potentially stale client-side state.

### 3.3 Access Token Lifecycle

- Access Tokens are short-lived and expire after 15 minutes.
- When an Access Token expires, the frontend requests a new token using the Refresh Token flow.
- Access Tokens are held in application memory and are not persisted in `localStorage` or `sessionStorage`.
- On application startup, the frontend may use the Refresh flow to establish a new in-memory Access Token.

## 4. Refresh Tokens and Session Persistence

### 4.1 Storage

Refresh Tokens are persisted through the `UserSession` entity/table in PostgreSQL.

The database stores a cryptographic hash of each Refresh Token, never the plaintext token.

A session record includes, at minimum:

- `id` — UUID session identifier.
- `user_id` — owning user.
- `token_hash` — hash of the current Refresh Token.
- `token_family_id` — identifier for the token family.
- `expires_at` — expiration timestamp.
- `revoked_at` — nullable revocation timestamp.
- `created_at` — creation timestamp.
- `replaced_by_session_id` — nullable reference to the replacement session/token record, if modeled as a separate record.

The exact relational representation must remain consistent with `DOMAIN_AND_DATABASE.md`. If token rotation is modeled as multiple token records within a session family, the schema must preserve the ability to identify and revoke the entire family.

### 4.2 Refresh Token Configuration

| Property | Decision |
|---|---|
| Token type | Opaque, cryptographically random token |
| Lifetime | 30 days |
| Storage | Hash in PostgreSQL |
| Transport | HttpOnly Cookie |
| Rotation | Required on every successful refresh |
| Reuse detection | Required |

Refresh Tokens are opaque random values, not JWTs. This allows the backend to enforce server-side session state and revocation.

### 4.3 Refresh Token Rotation

Every successful refresh operation performs the following steps:

1. Read the Refresh Token from the configured HttpOnly Cookie.
2. Validate the token by hashing it and locating the corresponding active database record.
3. Verify that it has not expired or been revoked.
4. Invalidate the presented token.
5. Generate a new cryptographically random Refresh Token.
6. Persist only its hash and link it to the same token family.
7. Issue a new Access Token and set the replacement Refresh Token Cookie.
8. Commit the rotation atomically.

The database transaction must prevent the same Refresh Token from being successfully rotated more than once. Use row-level locking or an equivalent concurrency-safe conditional update.

A failed or rolled-back rotation must not leave the user with an invalidated old token and no usable replacement.

### 4.4 Reuse Detection

If a previously rotated or revoked Refresh Token is presented again, the backend treats it as possible token theft:

- Identify the associated `token_family_id`.
- Revoke all active tokens/sessions in that family.
- Reject the refresh request.
- Require the user to authenticate again.

The event should be logged as a security event without logging the token itself.

### 4.5 Refresh Token Expiration

A newly issued Refresh Token has a 30-day lifetime. A successful rotation issues a replacement with a new 30-day expiration.

If the Refresh Token expires, the user must log in again.

### 4.6 Session Revocation

The backend supports:

- Revoking the current session on logout.
- Revoking all sessions on logout-all.
- Revoking all sessions after a password reset or password change.
- Revoking a token family after Refresh Token reuse detection.
- Administrative/security revocation when required.

Protected requests must not continue to be authorized solely on the basis of a valid JWT if its associated session has been revoked. The backend validates the session identified by the `sid` claim, using PostgreSQL and/or a carefully invalidated Redis cache. This enables revocation to take effect before the Access Token's natural expiration.

## 5. Token Transport and Cookie Security

### 5.1 Access Token

- The frontend stores the Access Token in memory only.
- Requests to protected API endpoints send it using the `Authorization: Bearer` header.
- It is not stored in browser persistent storage.

### 5.2 Refresh Token Cookie

The Refresh Token is delivered in a Cookie with these attributes:

- `HttpOnly`
- `Secure` in production
- `SameSite=Lax`
- Restricted `Path`, preferably the authentication refresh/logout path where practical
- Explicit expiration/max-age consistent with the 30-day token lifetime

The cookie must be cleared when the corresponding session is logged out or invalidated.

The frontend must not attempt to read the Refresh Token Cookie.

### 5.3 Deployment Origin

The preferred deployment is a same-origin application: Nginx serves the frontend and proxies `/api/` to FastAPI under the same site.

If the frontend and API use separate origins, the deployment must explicitly configure credentialed CORS, cookie behavior and CSRF protection. Cross-site cookie requirements must be reviewed before deployment; `SameSite=Lax` is intended for the same-site deployment model.

## 6. Email Verification

### 6.1 Email Provider

**Resend** is the selected transactional email provider for the MVP.

Email delivery is performed asynchronously through Celery to avoid blocking HTTP requests. The backend uses an EmailService abstraction to decouple business logic from the Resend provider.

The Resend API key is stored in environment configuration and must never be committed to source control or exposed to the frontend.

The free plan may be used during MVP development within the provider's current limits. Domain verification and DNS configuration, including SPF and DKIM, are deployment tasks.

### 6.2 Verification Flow

1. The user registers with an email address and password.
2. The backend creates the account in an unverified state.
3. The backend generates a cryptographically random, single-use verification token.
4. The backend stores only the token hash and its expiration in PostgreSQL.
5. The application queues an email delivery task through Celery.
6. RabbitMQ receives the task message.
7. A Celery worker picks up the task and calls the EmailService.
8. The EmailService uses the Resend provider to deliver the verification link.
9. The user opens the link.
10. The backend validates the token, marks the email as verified and invalidates the token.

Verification token lifetime: **15 minutes**.

### 6.3 Verification Requirements

- Verification tokens are single-use.
- Only token hashes are stored.
- Expired or previously used tokens are rejected.
- A resend-verification endpoint is provided.
- Resend requests are rate-limited.
- Protected application functionality requires a verified email.
- Registration and verification responses must not expose sensitive account data.

Suggested endpoint:

`POST /auth/email/verification/resend`

The verification link is handled by a frontend route that submits the token to the backend verification endpoint. The token must not be written to application logs or analytics.

## 7. Password Reset

### 7.1 Endpoints

| Method | Endpoint | Description |
|---|---|---|
| POST | `/auth/password/forgot` | Request a password-reset email |
| POST | `/auth/password/reset` | Set a new password using a reset token |

### 7.2 Reset Flow

1. The user submits an email address.
2. The backend returns a generic response regardless of whether the account exists.
3. If an eligible account exists, the backend generates a cryptographically random, single-use reset token.
4. Only the token hash is stored in PostgreSQL.
5. The application queues an email delivery task through Celery.
6. RabbitMQ receives the task message.
7. A Celery worker picks up the task and calls the EmailService.
8. The EmailService uses the Resend provider to deliver the reset link.
9. The user submits the token and new password.
10. The backend validates the token and password policy.
11. The password is hashed using Argon2id and updated.
12. The reset token is invalidated.
13. All active Refresh Sessions for that user are revoked.

Reset token lifetime: **15 minutes**.

The API must not reveal whether an email address is registered. Reset requests and attempts must be rate-limited.

## 8. Session Management

### 8.1 Multiple Sessions

A user may have multiple active sessions simultaneously, for example on a desktop and a mobile device.

Each device/session has its own Refresh Token and session record.

### 8.2 Session Endpoints

| Method | Endpoint | Description |
|---|---|---|
| POST | `/auth/logout` | Revoke the current session |
| POST | `/auth/logout-all` | Revoke all sessions belonging to the authenticated user |
| POST | `/auth/refresh` | Rotate the current session's Refresh Token |

Logout must revoke the current server-side session and clear the Refresh Token Cookie.

Logout-all must revoke all active sessions for the authenticated user and clear the current Refresh Token Cookie.

Password reset and password change revoke all active sessions. The user must authenticate again on each device.

## 9. Authorization (RBAC)

### 9.1 Roles

The MVP uses two roles:

- `USER`
- `ADMIN`

The role is stored in PostgreSQL and enforced by backend authorization logic.

### 9.2 Authorization Rules

- `USER` can access permitted user functionality and their own private resources.
- `ADMIN` can access authorized administrative content-management and media operations.
- Users cannot change their own role.
- Role changes are performed only through trusted administrative/backend processes.
- Ownership checks are required independently of role checks.
- Frontend route protection is a usability measure, not an authorization boundary.

A separate fine-grained permission entity/system is not required for the MVP.

## 10. CSRF Protection

Refresh Token authentication uses Cookies, so state-changing Cookie-authenticated endpoints require CSRF protection.

MVP requirements:

- Set the Refresh Token Cookie with `SameSite=Lax`.
- Set `HttpOnly` and `Secure` in production.
- Validate the `Origin` header against the configured trusted frontend origin for state-changing requests.
- Require a CSRF token in a dedicated request header for `/auth/refresh` and `/auth/logout`.
- Use a secure double-submit CSRF pattern: the CSRF value is available to the frontend separately from the HttpOnly Refresh Token Cookie, and the backend verifies that the submitted header matches the expected CSRF cookie/token.
- Rotate or invalidate CSRF state as appropriate when the authentication session changes.
- Never place the Refresh Token itself in a readable Cookie or CSRF header.

The CSRF token is not an authentication credential and does not replace Refresh Token validation.

## 11. CORS

CORS is configured through environment-specific settings.

Requirements:

- Allow only explicitly configured frontend origins.
- Do not use `Access-Control-Allow-Origin: *` with credentialed requests.
- Enable credentials only for trusted origins that require Cookie-based authentication.
- Allow only required methods: `GET`, `POST`, `PATCH`, `PUT`, `DELETE`, and `OPTIONS` for preflight.
- Allow only required headers, including `Authorization`, `Content-Type` and the configured CSRF header.
- Do not reflect arbitrary Origin values.
- Keep development and production origin allowlists separate.

The preferred same-origin Nginx deployment minimizes the need for cross-origin browser requests.

## 12. Rate Limiting

Redis is used for distributed rate-limit counters. **SlowAPI** is the selected rate-limiting integration for FastAPI.

Initial MVP limits:

| Endpoint / Operation | Initial Limit |
|---|---:|
| Login | 5 requests / minute |
| Register | 3 requests / hour per IP |
| Forgot Password | 3 requests / hour per IP |
| Email Verification | 5 requests / hour per IP |
| Refresh | 10 requests / minute |
| Other API endpoints | 100 requests / minute |

These are initial configuration values, not permanent security guarantees. They must be configurable and reviewed using production traffic and abuse signals.

Additional requirements:

- Apply limits to relevant authentication and email operations.
- Return `429 Too Many Requests` when a limit is exceeded.
- Use trusted proxy configuration when determining client IP addresses; do not blindly trust arbitrary forwarded headers.
- Avoid relying only on IP-based limits where account- or token-based controls are also practical.
- Redis is used for transient rate-limit state, not as the source of truth for sessions or token revocation.

## 13. Application Security

### 13.1 Input Validation and Injection

- Validate all request data using backend schemas.
- Use SQLAlchemy parameterized queries and ORM operations.
- Do not construct SQL by concatenating untrusted input.
- Validate UUIDs, enum values, lengths, numeric ranges and resource relationships.
- Enforce authorization and ownership checks after identifying the requested resource.

### 13.2 XSS

- Rely on React's default output escaping.
- Avoid rendering untrusted HTML.
- If rich HTML rendering becomes necessary, sanitize it with a maintained sanitizer and a strict allowlist.
- Configure an appropriate Content Security Policy (CSP) at the web server/application layer.
- Do not store authentication tokens in browser persistent storage.

### 13.3 HTTPS and Transport

- Require HTTPS in production.
- Terminate TLS at Nginx or the selected trusted ingress.
- Redirect HTTP to HTTPS.
- Use secure Cookie attributes in production.
- Configure trusted proxy headers correctly so FastAPI understands the original request scheme and client information.

### 13.4 Secrets and Environment Configuration

Secrets include:

- JWT signing secret.
- Resend API key.
- Database credentials.
- Redis credentials, where configured.
- Object-storage credentials.

Requirements:

- Load secrets from environment or a deployment secret manager.
- Keep local environment files out of source control.
- Provide safe example environment files containing placeholders only.
- Never expose secrets in frontend bundles, API responses, logs or error messages.
- Rotate secrets when exposure is suspected.

### 13.5 Logging and Monitoring

Log security-relevant events, including:

- Successful and failed authentication attempts.
- Email verification completion.
- Password reset completion.
- Session creation and revocation.
- Refresh Token reuse detection.
- Authorization failures.
- Rate-limit events.

Never log:

- Plaintext passwords.
- Access Tokens or Refresh Tokens.
- Cookie values.
- Password-reset or verification tokens.
- API keys, signing secrets or database credentials.

Logs should include useful event metadata without recording sensitive credential material.

### 13.6 Error Handling

- Return generic authentication failure messages where detailed responses could enable account enumeration.
- Do not expose stack traces or internal exception details to clients.
- Use the common API error response structure defined in `API_DESIGN.md`.
- Record diagnostic details only in appropriately protected server logs.

## 14. Account and Credential Lifecycle

- Registration creates an account that must complete email verification before accessing protected application functionality.
- Password changes require the current authenticated session and appropriate verification controls.
- Password reset uses the single-use reset flow in Section 7.
- Password reset and password change revoke all active Refresh Sessions.
- Email changes require a separate verified account-security flow; they are not ordinary profile updates.
- Users cannot grant themselves administrative privileges.

The exact account deletion and data-retention policy remains a separate product/security decision and is not defined by this document.

## 15. Security Configuration Summary

| Setting | MVP Decision |
|---|---|
| Password hashing | Argon2id |
| Password length | 8–128 characters |
| Access Token | JWT, HS256 |
| Access Token lifetime | 15 minutes |
| Refresh Token | Opaque random token |
| Refresh Token lifetime | 30 days |
| Refresh Token storage | Hash in PostgreSQL |
| Refresh Token rotation | Every successful refresh |
| Refresh Token reuse detection | Revoke token family |
| Refresh Token transport | HttpOnly, Secure, SameSite=Lax Cookie |
| Access Token transport | Bearer header; frontend memory only |
| Email provider | Resend |
| Email verification token lifetime | 15 minutes |
| Password reset token lifetime | 15 minutes |
| Session model | Multiple concurrent sessions |
| Roles | USER, ADMIN |
| CSRF | Origin validation + CSRF token |
| CORS | Explicit origin allowlist |
| Rate limiting | SlowAPI + Redis |

## 16. Remaining Decisions

The following items remain environment-, product- or deployment-specific:

| Decision | Status |
|---|---|
| Argon2id cost parameters | Tune for production hardware |
| JWT issuer and audience values | Set per environment |
| Production cookie domain and exact path | Set during deployment |
| Production frontend origin allowlist | Set during deployment |
| Resend domain verification and DNS records | Set during deployment |
| Exact MIME types and email templates | Define during implementation |
| Exact rate-limit thresholds | Review against production usage |
| Account deletion and data-retention policy | Separate product/security decision |
| Password-change re-authentication UX | Define during implementation |

## 17. Related Documents

- `SYSTEM_ARCHITECTURE.md`
- `BACKEND_ARCHITECTURE.md`
- `DOMAIN_AND_DATABASE.md`
- `API_DESIGN.md`
- `INFRASTRUCTURE_AND_DEVOPS.md`
- `README.md`
