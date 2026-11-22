# API Design

**Project:** Cubiland  
**Document:** API Design  
**Status:** Defined for MVP  
**Scope:** MVP

## 1. Overview

This document defines the REST API contract between the React frontend and the FastAPI backend.

The API exposes application capabilities, validates requests, enforces authentication and authorization, and returns consistent responses.

### 1.1 API Principles

- REST architectural style.
- JSON request and response formats, except file-upload operations.
- HTTPS in production.
- URL-based API versioning.
- Consistent resource naming and response conventions.
- Centralized error response structure.
- Backend-side validation, ownership checks and authorization.
- Explicit separation of public, authenticated and administrative endpoints.

### 1.2 Base URL

All endpoints use the prefix:

`/api/v1`

Example:

`https://<domain>/api/v1/courses`

The production domain is deployment-specific and is not part of the API contract.

## 2. HTTP Conventions

### 2.1 HTTP Methods

| Method | Purpose |
|---|---|
| GET | Retrieve resources |
| POST | Create a resource or execute an operation |
| PATCH | Partially update a resource |
| PUT | Create or fully replace a resource representation where appropriate |
| DELETE | Delete a resource |

### 2.2 Status Codes

| Status Code | Meaning |
|---|---|
| 200 OK | Request completed successfully |
| 201 Created | Resource created successfully |
| 204 No Content | Request completed successfully without a response body |
| 400 Bad Request | Request cannot be processed |
| 401 Unauthorized | Authentication is missing, invalid or expired |
| 403 Forbidden | Authenticated user lacks permission |
| 404 Not Found | Resource does not exist or is not visible to the caller |
| 409 Conflict | Request conflicts with the current resource state |
| 422 Unprocessable Entity | Request schema or field validation failed |
| 429 Too Many Requests | Rate limit exceeded |
| 500 Internal Server Error | Unexpected server error |

### 2.3 Naming Conventions

- Use lowercase plural nouns for collection paths.
- Use `snake_case` for JSON fields and query parameters.
- Use UUID identifiers in resource paths.
- Use ISO 8601 timestamps in UTC for API date-time values.
- Use explicit action endpoints for state transitions that represent business operations.

Examples:

- `/users/me`
- `/courses`
- `/courses/{course_id}`
- `/solves`
- `/statistics/overview`

## 3. Request and Response Format

### 3.1 Request Format

Requests containing structured data use JSON unless the operation requires file upload.

Example:

```json
{
  "display_name": "CubingUser"
}
```

### 3.2 Resource Responses

Successful resource requests return the resource representation directly.

Example:

```json
{
  "id": "uuid",
  "display_name": "CubingUser",
  "created_at": "2026-11-22T12:00:00Z"
}
```

### 3.3 Collection Responses and Pagination

Paginated collection endpoints use a consistent response structure:

```json
{
  "items": [],
  "pagination": {
    "limit": 20,
    "offset": 0,
    "total": 0
  }
}
```

MVP pagination uses offset-based pagination:

- `limit`: number of items to return; default `20`, maximum `100`.
- `offset`: number of items to skip; default `0`.
- `total`: total number of matching records.

Collection endpoints that return bounded, small nested collections may omit pagination when pagination provides no practical value.

### 3.4 Error Response

All API errors use the following structure:

```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "The request contains invalid data.",
    "details": [
      {
        "field": "display_name",
        "message": "Field is required."
      }
    ]
  }
}
```

`details` may be an empty array when no field-level details apply.

Error responses must not expose stack traces, SQL statements, database details, credentials, tokens or other sensitive internal information.

## 4. Authentication

Authentication uses JWT Access Tokens and Refresh Tokens.

### 4.1 Authentication Endpoints

| Method | Endpoint | Description | Access |
|---|---|---|---|
| POST | `/auth/register` | Register an account | Public |
| POST | `/auth/login` | Authenticate a user | Public |
| POST | `/auth/refresh` | Rotate and refresh authentication tokens | Valid refresh session |
| POST | `/auth/logout` | Revoke the current session | Authenticated session |

### 4.2 Registration and Login

The registration request contains:

- `email`
- `password`
- `username`
- `display_name` (optional; may default to the username)

The login request contains:

- `email`
- `password`

The API returns the authenticated user's public account/profile representation and establishes the authentication session using the token transport defined in `AUTHENTICATION_AND_SECURITY.md`.

The API must not return password hashes or stored refresh-token hashes.

### 4.3 Refresh and Logout

Refresh uses Refresh Token Rotation. A successful refresh invalidates the presented refresh token and issues a replacement. Reuse of an already rotated token triggers revocation of the associated token family/session chain.

Refresh-token records are persisted in PostgreSQL. Only token hashes are stored.

The exact cookie/header transport and token lifetime values are specified in `AUTHENTICATION_AND_SECURITY.md`.

## 5. User Profiles and Settings

### 5.1 Profile Endpoints

| Method | Endpoint | Description | Access |
|---|---|---|---|
| GET | `/users/me` | Retrieve the authenticated user's profile | Authenticated |
| PATCH | `/users/me` | Update the authenticated user's profile | Authenticated |

The profile representation may include:

- `id`
- `username`
- `display_name`
- `avatar_media_id`
- `bio`
- `created_at`
- `updated_at`

Email changes, if supported later, must use a separate verified account-security flow rather than an ordinary profile update.

### 5.2 Settings Endpoints

| Method | Endpoint | Description | Access |
|---|---|---|---|
| GET | `/users/me/settings` | Retrieve the user's settings | Authenticated |
| PATCH | `/users/me/settings` | Update the user's settings | Authenticated |

MVP settings include the approved timer and appearance preferences, including:

- WCA inspection: `OFF`, `15S` or `17S`.
- Inspection alerts.
- Timer sound.
- Theme.

The backend validates allowed values. The frontend must not be treated as the source of truth for validation.

## 6. Learning API

The Learning API exposes published courses, sections, lessons and the authenticated user's learning progress.

### 6.1 Course and Section Endpoints

| Method | Endpoint | Description | Access |
|---|---|---|---|
| GET | `/courses` | List published courses | Public |
| GET | `/courses/{course_id}` | Retrieve a published course | Public |
| GET | `/courses/{course_id}/sections` | List sections of a published course | Public |
| GET | `/sections/{section_id}/lessons` | List published lessons in a section | Public |

Public learning endpoints return only content with a `PUBLISHED` status. Draft and archived content is not exposed through these endpoints.

A lesson is available only when both the lesson and its parent course are published.

### 6.2 Lesson Endpoints

| Method | Endpoint | Description | Access |
|---|---|---|---|
| GET | `/lessons/{lesson_id}` | Retrieve published lesson content | Public |
| GET | `/lessons/{lesson_id}/progress` | Retrieve the user's progress for a lesson | Authenticated |
| PUT | `/lessons/{lesson_id}/progress` | Create or update lesson progress | Authenticated |
| POST | `/lessons/{lesson_id}/complete` | Explicitly mark a lesson as completed | Authenticated |

Lesson progress uses these states:

- `NOT_STARTED`
- `IN_PROGRESS`
- `COMPLETED`

The completion endpoint performs the explicit completion action. Repeating the completion request must be safe and must not create duplicate progress records.

Progress belongs to the authenticated user. A client cannot read or modify another user's progress.

### 6.3 Course Progress

| Method | Endpoint | Description | Access |
|---|---|---|---|
| GET | `/courses/{course_id}/progress` | Retrieve the user's progress for a course | Authenticated |

Course progress is derived from the progress records of lessons belonging to the course. It is not independently editable through the API.

## 7. Timer and Solve Records API

The timer runs on the frontend. The backend stores completed solves and provides solve history and statistics inputs.

### 7.1 Solve Endpoints

| Method | Endpoint | Description | Access |
|---|---|---|---|
| POST | `/solves` | Save a completed solve | Authenticated |
| GET | `/solves` | Retrieve the user's solve history | Authenticated |
| GET | `/solves/{solve_id}` | Retrieve a specific solve | Owner |
| PATCH | `/solves/{solve_id}` | Update an existing solve | Owner |
| DELETE | `/solves/{solve_id}` | Delete an existing solve | Owner |

All solve operations enforce ownership on the backend.

### 7.2 Create Solve Request

The solve duration is represented as an integer number of milliseconds in `duration_ms`.

Example:

```json
{
  "duration_ms": 12500,
  "penalty": "NONE",
  "scramble": "R U R' U'",
  "solving_method": "CFOP",
  "solved_at": "2026-11-22T12:30:00Z"
}
```

Fields:

| Field | Type | Required | Description |
|---|---|---|---|
| `duration_ms` | Integer | Yes | Raw measured solve duration in milliseconds |
| `penalty` | Enum | No | `NONE`, `PLUS_TWO` or `DNF`; defaults to `NONE` |
| `scramble` | String or null | No | Scramble used for the solve |
| `solving_method` | String or null | No | Method metadata, for example `CFOP` |
| `solved_at` | Date-time | Yes | Time when the solve was completed |

The raw measured duration is preserved independently of the penalty. The API must not overwrite `duration_ms` with a penalty-adjusted value.

The effective time used for display or statistics is derived from `duration_ms` and `penalty` according to the statistics/business rules. A `DNF` remains represented as a penalty value, not as a fabricated duration.

The database stores duration as a `BIGINT`. API validation rejects negative durations and invalid enum values.

### 7.3 Solve History

`GET /solves` supports:

- `limit`
- `offset`
- `from`
- `to`
- `sort_by`
- `sort_order`

For MVP:

- Default ordering is `solved_at` descending.
- `sort_by` supports `solved_at` and `duration_ms`.
- `sort_order` supports `asc` and `desc`.
- `from` and `to` are inclusive ISO 8601 date-time boundaries.
- The API validates limits and filter values.

## 8. Statistics API

Statistics are calculated from the authenticated user's solve records.

### 8.1 Statistics Endpoints

| Method | Endpoint | Description | Access |
|---|---|---|---|
| GET | `/statistics/overview` | Retrieve the user's main statistics | Authenticated |
| GET | `/statistics/times` | Retrieve solve-time statistics | Authenticated |
| GET | `/statistics/trends` | Retrieve performance trends | Authenticated |

The planned statistics include:

- Single.
- Personal best.
- Average of 5.
- Average of 12.
- Average of 50.
- Average of 100.
- Current and best averages.

The exact calculation formulas, DNF trimming rules, rounding and minimum sample requirements are product/statistics rules and must be specified before those calculations are implemented. This API document does not define or assume those formulas.

All statistics are scoped to the authenticated user.

## 9. Admin API

Administrative endpoints manage course content and media.

Every administrative endpoint requires authentication and server-side authorization for the `ADMIN` role. Frontend route protection alone is insufficient.

### 9.1 Course Management

| Method | Endpoint | Description |
|---|---|---|
| POST | `/admin/courses` | Create a course |
| PATCH | `/admin/courses/{course_id}` | Update a course |
| DELETE | `/admin/courses/{course_id}` | Delete a course when deletion rules allow |
| POST | `/admin/courses/{course_id}/publish` | Publish a course |
| POST | `/admin/courses/{course_id}/unpublish` | Return a published course to draft |
| POST | `/admin/courses/{course_id}/archive` | Archive a course |

### 9.2 Section Management

| Method | Endpoint | Description |
|---|---|---|
| POST | `/admin/courses/{course_id}/sections` | Create a section |
| PATCH | `/admin/sections/{section_id}` | Update a section |
| DELETE | `/admin/sections/{section_id}` | Delete a section when deletion rules allow |
| PATCH | `/admin/courses/{course_id}/sections/order` | Update section ordering |

Sections do not have an independent publication status. Their visibility follows the parent course's publication status.

### 9.3 Lesson Management

| Method | Endpoint | Description |
|---|---|---|
| POST | `/admin/sections/{section_id}/lessons` | Create a lesson |
| PATCH | `/admin/lessons/{lesson_id}` | Update a lesson |
| DELETE | `/admin/lessons/{lesson_id}` | Delete a lesson when deletion rules allow |
| POST | `/admin/lessons/{lesson_id}/publish` | Publish a lesson |
| POST | `/admin/lessons/{lesson_id}/unpublish` | Return a published lesson to draft |
| POST | `/admin/lessons/{lesson_id}/archive` | Archive a lesson |
| PATCH | `/admin/sections/{section_id}/lessons/order` | Update lesson ordering |

A lesson may be published only when its parent course is published. Publishing a course does not implicitly publish its draft lessons.

### 9.4 Publication and Deletion Rules

Content uses the statuses `DRAFT`, `PUBLISHED` and `ARCHIVED`.

- `unpublish` changes `PUBLISHED` content to `DRAFT`.
- `archive` changes content to `ARCHIVED`.
- Archived content is excluded from public learning endpoints.
- `DELETE` is a permanent deletion operation, not an alias for archive.
- Deletion is rejected with `409 Conflict` when dependent records or references prevent safe deletion.
- Admin endpoints must validate parent-child relationships and publication constraints.

## 10. Media API

Media files are stored in S3-compatible Object Storage. PostgreSQL stores media metadata and references, not the binary file itself.

### 10.1 Media Endpoints

| Method | Endpoint | Description | Access |
|---|---|---|---|
| POST | `/admin/media/upload-url` | Request a presigned upload URL | Admin |
| POST | `/admin/media` | Register metadata after upload | Admin |
| DELETE | `/admin/media/{media_id}` | Delete a media reference and eligible stored object | Admin |

### 10.2 Upload Flow

The MVP uses direct-to-object-storage uploads with a backend-issued presigned URL:

1. The admin requests an upload URL and supplies file metadata.
2. The backend validates the requested file type and size and returns a short-lived presigned URL plus the required upload method/headers.
3. The frontend uploads the file directly to object storage.
4. The frontend calls `POST /admin/media` to register the uploaded object.
5. The backend verifies the upload/object metadata and creates the media record.

The backend must not trust client-supplied object keys or metadata without validation.

Allowed file types and maximum sizes are configuration/business constraints and must be enforced server-side. A media object referenced by published content must not be deleted without first resolving those references.

## 11. Authorization Rules

The API uses role-based access control with the MVP roles `USER` and `ADMIN`.

| Resource | User | Admin |
|---|---|---|
| Own profile | Read / Update | Read / Update |
| Own settings | Read / Update | Read / Update |
| Published courses and lessons | Read | Read |
| Own learning progress | Read / Update | Read / Update |
| Own solve records | Read / Create / Update / Delete | Read / Create / Update / Delete |
| Own statistics | Read | Read |
| Course management | No access | Authorized management |
| Section management | No access | Authorized management |
| Lesson management | No access | Authorized management |
| Media management | No access | Authorized management |

All ownership and role checks are performed by the backend. Administrative permissions must never be inferred from frontend state or route visibility.

## 12. Pagination, Filtering and Sorting

Collection endpoints use offset pagination where the result set can grow.

| Parameter | Description |
|---|---|
| `limit` | Maximum number of returned records; default `20`, maximum `100` |
| `offset` | Number of records to skip; default `0` |
| `sort_by` | Supported field to sort by, where applicable |
| `sort_order` | `asc` or `desc` |
| `from` | Inclusive start of a date-time range, where applicable |
| `to` | Inclusive end of a date-time range, where applicable |

Each endpoint documents which filters and sorting fields it supports. Unsupported fields and invalid values return a validation error.

Cursor pagination is not required for the MVP and may be introduced later if scale or query performance requires it.

## 13. API Versioning

The API uses URL-based versioning.

Initial version:

`/api/v1`

Breaking changes that cannot be introduced compatibly require a new API version. Backward-compatible additions may be introduced within the current version.

## 14. Validation and Error Handling

All incoming requests are validated by the backend.

Validation includes:

- Required fields and data types.
- Field length and numeric boundaries.
- Allowed enum values.
- UUID and timestamp formats.
- Resource existence and parent-child relationships.
- Ownership and authorization.
- Publication and other domain business rules.
- Pagination, filtering and sorting parameters.

The API distinguishes validation, authentication, authorization, not-found, conflict, rate-limit and unexpected internal errors. The response format is defined in Section 3.4.

## 15. API Security Requirements

The API must:

- Require HTTPS in production.
- Validate authentication credentials and token state.
- Enforce server-side role and ownership checks.
- Prevent unauthorized access to user-owned resources.
- Validate all incoming data.
- Protect administrative endpoints.
- Avoid exposing sensitive internal information.
- Apply rate limits to authentication and other sensitive operations.
- Keep secrets and credentials outside API responses and source control.
- Validate media upload authorization, file metadata and object references.

Detailed token lifecycle, cookie/header transport, password policy and security controls are defined in `AUTHENTICATION_AND_SECURITY.md`.

## 16. API Documentation

FastAPI generates the OpenAPI schema and interactive API documentation.

The OpenAPI contract must describe:

- Endpoints and HTTP methods.
- Path and query parameters.
- Request and response schemas.
- Authentication requirements.
- Possible status codes.
- Error response formats.
- Enum values and validation constraints.

The documented API contract must remain consistent with implemented backend behavior.

## 17. Remaining Decisions

The following items are intentionally outside the scope of this API contract or require product/security policy decisions:

| Decision | Status |
|---|---|
| Access and refresh token lifetimes and refresh-token transport | Defined in `AUTHENTICATION_AND_SECURITY.md` |
| Password policy and account verification requirements | Defined in `AUTHENTICATION_AND_SECURITY.md` |
| Exact statistics formulas, DNF trimming and rounding | Requires statistics/business rules |
| Account deletion and data-retention policy | Requires product/security decision |
| Final allowed media MIME types and maximum file sizes | Deployment/product configuration |
| Exact rate-limit thresholds | Deployment/security configuration |
| Production domain and object-storage provider | Infrastructure configuration |

The API conventions, endpoint groups, pagination contract, solve payload conventions, learning progress states, content publication behavior and media upload flow are defined for the MVP.

## 18. Related Documents

- `SYSTEM_ARCHITECTURE.md`
- `BACKEND_ARCHITECTURE.md`
- `DOMAIN_AND_DATABASE.md`
- `AUTHENTICATION_AND_SECURITY.md`
- `INFRASTRUCTURE_AND_DEVOPS.md`
- `README.md`
