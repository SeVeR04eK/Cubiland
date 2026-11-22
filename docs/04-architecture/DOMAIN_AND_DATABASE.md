# Domain and Database

**Project:** Cubiland  
**Document:** Domain and Database  
**Status:** Proposed Design  
**Scope:** MVP

## 1. Overview

This document describes the core domain model and database design for Cubiland.

The application uses PostgreSQL as its primary relational database.

The database model is designed around the MVP capabilities:

- User accounts and profiles.
- Courses, sections and lessons.
- Learning progress.
- Solve records and solve history.
- Basic statistics.
- Administrative content management.
- Essential user settings.

The design follows the Modular Monolith architecture and keeps business ownership of data within the corresponding backend modules.

## 2. Database Technology

| Technology | Responsibility |
|---|---|
| PostgreSQL | Primary relational database |
| SQLAlchemy 2.0 AsyncIO | ORM and asynchronous database access |
| Alembic | Database schema migrations |
| Redis | Caching, not persistent source of truth |
| S3-compatible Object Storage | Images and learning materials |

All persistent application data must be stored in PostgreSQL unless an explicitly documented external storage requirement applies.

## 3. Domain Overview

The core domain is divided into the following areas:

| Domain | Main Entities |
|---|---|
| Identity & Access | User, Role, UserSession |
| User Profiles | UserProfile, UserSettings |
| Learning | Course, CourseSection, Lesson, UserLessonProgress |
| Content Management | Course, CourseSection, Lesson, MediaAsset |
| Solving | Solve |
| Statistics | Derived statistics based on Solve records |

## 4. Core Entities

### 4.1 User

Represents a registered Cubiland account.

Responsibilities:

- Account identity.
- Authentication-related account data.
- Ownership of private application data.
- Association with a user profile.
- Association with user roles.

The User entity is the owner of user-specific resources, including solve records and learning progress.

Candidate attributes:

- `id`
- `email`
- `password_hash`
- `is_active`
- `created_at`
- `updated_at`

For the MVP, email is the account identifier. Email addresses must be normalized before storage and compared case-insensitively. A unique database constraint must enforce one account per normalized email address.

Email verification and account recovery requirements are defined separately in the authentication and security design.

### 4.2 Role

Represents an authorization role assigned to a user.

Initial roles:

- `USER`
- `ADMIN`

Roles determine access to protected application functionality.

The MVP uses role-based access control with the `USER` and `ADMIN` roles. Roles are stored separately and assigned through a many-to-many user-role relationship. The backend enforces permissions on every protected operation; the frontend is not an authorization boundary.

A separate granular permission entity is not required for the MVP. The model can be extended if finer-grained permissions become necessary.

### 4.3 UserProfile

Stores user-facing profile information.

Responsibilities:

- Display information.
- Approved editable profile fields.
- Profile-related preferences where applicable.

MVP attributes:

- `id`
- `user_id`
- `username` (unique, normalized)
- `display_name`
- `avatar_media_id` (nullable reference to `MediaAsset`)
- `bio` (nullable)
- `created_at`
- `updated_at`

The profile is private by default. Public profile visibility and additional profile fields are outside the MVP scope unless separately approved.

### 4.4 UserSettings

Stores user-specific application preferences.

Settings are limited to the features approved for the MVP.

MVP settings are stored as structured JSONB in `settings_data`, validated by the backend against a defined settings schema. The initial settings cover:

- Timer inspection: `OFF`, `15_SECONDS`, or `17_SECONDS`.
- Inspection alerts: enabled or disabled.
- Timer sound: enabled or disabled.
- Theme preference.

The settings record has a one-to-one relationship with `User`. New settings must receive documented defaults. Additional settings can be added through schema evolution without treating Redis as persistent storage.

### 4.5 Course

Represents a learning course.

Responsibilities:

- Course information.
- Course description.
- Publication status.
- Course ordering.
- Association with course sections.

Candidate attributes:

- `id`
- `title`
- `description`
- `thumbnail_url`
- `status`
- `position`
- `created_at`
- `updated_at`
- `published_at`

A course may contain multiple ordered sections.

Only published courses available to the user may be displayed through normal learning flows.

### 4.6 CourseSection

Represents an ordered section within a course.

Responsibilities:

- Section information.
- Association with a parent course.
- Ordering of sections.

Candidate attributes:

- `id`
- `course_id`
- `title`
- `description`
- `position`
- `created_at`
- `updated_at`

A course section belongs to exactly one course.

A section may contain multiple lessons.

### 4.7 Lesson

Represents an individual learning unit.

Responsibilities:

- Lesson title and content.
- Ordering within a section.
- Publication availability.
- Association with learning materials.

Candidate attributes:

- `id`
- `section_id`
- `title`
- `content`
- `position`
- `status`
- `created_at`
- `updated_at`
- `published_at`

Lesson content is stored as structured JSONB. The payload supports ordered content blocks, such as headings, paragraphs, lists, images, and embedded media references. The backend validates the payload against a versioned content schema before saving or publishing it.

Binary media files are stored in Object Storage and referenced by `MediaAsset` identifiers. Video delivery/provider details are not part of the database model and may be decided separately.

### 4.8 UserLessonProgress

Represents a user's progress through an individual lesson.

Responsibilities:

- Persisting lesson progress.
- Tracking lesson completion.
- Supporting course resumption.

Candidate attributes:

- `id`
- `user_id`
- `lesson_id`
- `status`
- `completed_at`
- `created_at`
- `updated_at`

A user may have only one progress record for a particular lesson.

Course progress can be derived from the user's lesson progress records.

For the MVP, a lesson is marked complete through an explicit user action after the user has accessed the lesson. Completion is persisted in `UserLessonProgress`; the initial states are `NOT_STARTED`, `IN_PROGRESS`, and `COMPLETED`. A unique constraint on (`user_id`, `lesson_id`) prevents duplicate progress records. More complex completion rules, such as quizzes or required video watch time, are out of MVP scope.

### 4.9 Solve

Represents a completed solving attempt saved by a user.

Responsibilities:

- Storing solve duration.
- Associating the solve with its owner.
- Providing data for solve history.
- Serving as the source for statistics calculations.

Candidate attributes:

- `id`
- `user_id`
- `duration`
- `solved_at`
- `created_at`
- `updated_at`

The solve duration is stored as an integer number of milliseconds (`duration_ms`, BIGINT). Floating-point values are not used for elapsed-time storage.

Penalty is represented by a dedicated enum with `NONE`, `PLUS_TWO`, and `DNF` values. The raw measured duration remains unchanged; the penalty is applied by statistics calculations rather than by overwriting the measured duration.

Optional solve metadata may include scramble and solving method. A `SolveSession` entity groups solves into user-owned practice sessions. Device metadata is not required for the MVP. Exact statistics eligibility and calculation rules are defined in the Statistics domain logic.

### 4.10 MediaAsset

Represents metadata for a file stored in Object Storage.

Responsibilities:

- Identifying uploaded media.
- Maintaining storage references.
- Associating media with learning content.

Candidate attributes:

- `id`
- `owner_user_id` (nullable for system/admin-managed assets, subject to authorization policy)
- `storage_key`
- `original_filename`
- `media_type`
- `file_size`
- `created_at`

The actual file is stored in S3-compatible Object Storage, not directly in PostgreSQL. PostgreSQL stores the storage key and metadata. User-uploaded assets are associated with their owner; administrative course assets are associated with the creating/admin account or an explicitly defined system owner. Access to upload, read, replace, and delete assets is checked by the backend. Allowed MIME types, size limits, and upload transport are implementation/security configuration.

### 4.11 SolveSession

Represents a user-owned grouping of solve attempts.

Candidate attributes:

- `id`
- `user_id`
- `name` (nullable)
- `started_at`
- `created_at`
- `updated_at`

A session belongs to exactly one user and may contain multiple solves. A solve may reference a session optionally.

### 4.12 UserSession

Represents an authenticated login session and supports refresh-token rotation and revocation.

Candidate attributes:

- `id`
- `user_id`
- `refresh_token_hash`
- `token_family_id`
- `created_at`
- `expires_at`
- `last_used_at`
- `revoked_at`
- `replaced_by_session_token_id` (nullable, where applicable)

Refresh tokens are never stored in plaintext. Only a cryptographic hash is persisted in PostgreSQL. Each successful refresh rotates the token: the presented token is invalidated and a new token hash is stored. Reuse of a previously rotated token is treated as a potential compromise and causes the associated token family/session chain to be revoked.

Logout revokes the current session. The database update and token rotation must be performed transactionally. Redis is not the source of truth for session validity.

### 4.13 Authentication Token Persistence

The `UserSession` records are persisted in PostgreSQL and indexed by user, token family, expiry, and revocation state as appropriate. Expired/revoked records may be cleaned up according to a retention policy, while retaining sufficient information for refresh-token reuse detection.

## 5. Entity Relationships

The main relationships are:

| Relationship | Cardinality |
|---|---|
| User → UserProfile | One-to-One |
| User → UserSettings | One-to-One |
| User → Roles | Many-to-Many |
| User → UserSession | One-to-Many |
| User → Solve | One-to-Many |
| User → SolveSession | One-to-Many |
| SolveSession → Solve | One-to-Many (optional from Solve) |
| User → UserLessonProgress | One-to-Many |
| Course → CourseSection | One-to-Many |
| CourseSection → Lesson | One-to-Many |
| Lesson → UserLessonProgress | One-to-Many |
| Course/Lesson → MediaAsset | Many-to-Many or explicit content-block references, depending on usage |
| User → MediaAsset | One-to-Many (for user-owned uploads) |

### 5.1 Learning Hierarchy

The learning content follows this hierarchy:

`Course → CourseSection → Lesson`

Each level has an explicit ordering attribute.

### 5.2 User Learning Progress

A user can have progress records for multiple lessons.

Each progress record connects one user with one lesson.

A unique constraint must prevent duplicate progress records for the same user and lesson.

### 5.3 Solve Ownership

Each solve belongs to exactly one user.

A user can access and modify only their own solve records, subject to the approved operation policies.

## 6. Database Constraints and Integrity

The database must enforce data integrity wherever possible.

### 6.1 Primary Keys

Every persistent entity must have a primary key.

All persistent entities use UUID v4 primary keys. UUIDs are generated by the application or database using a cryptographically secure UUID implementation. Foreign keys use the same UUID type.

### 6.2 Foreign Keys

Relationships between entities must be represented through foreign keys.

Foreign-key constraints must prevent invalid references.

### 6.3 Unique Constraints

The following uniqueness requirements apply:

- Normalized account email must be unique (case-insensitive).
- Username must be unique after normalization.
- A user must have at most one profile record.
- A user must have at most one settings record.
- A user must have at most one progress record per lesson.
- Role identifiers must be unique.
- Refresh-token hashes must be unique.
- A session must belong to exactly one user.
- Revoked or expired sessions must not be accepted for token refresh.
- Token rotation must invalidate the previous refresh-token hash atomically before the replacement token is accepted.

### 6.4 Not Null Constraints

Required attributes must use database-level NOT NULL constraints.

Optional profile fields and metadata may remain nullable where appropriate.

### 6.5 Ownership and Data Isolation

Every user-owned resource must be associated with its owner.

The backend must enforce ownership checks before returning, updating or deleting private user data.

Database queries must be scoped to the authenticated user where applicable.

## 7. Course Content Management

Course content is managed through the Admin Panel.

Administrative operations include:

- Creating courses.
- Editing course information.
- Creating and editing sections.
- Creating and editing lessons.
- Changing content ordering.
- Uploading learning materials.
- Publishing and unpublishing content.

### 7.1 Publication Status

Courses and lessons must support publication availability.

Unpublished content must not be accessible through ordinary user-facing learning flows.

Courses and lessons use the states `DRAFT`, `PUBLISHED`, and `ARCHIVED`. Only `PUBLISHED` courses and lessons are available through ordinary user-facing learning flows. A lesson is not accessible if its parent course is not published. Sections do not have an independent publication state in the MVP; their availability follows the parent course.

### 7.2 Content Ordering

Courses, sections and lessons must support explicit ordering.

Ordering must not depend on database retrieval order.

### 7.3 Content Validation

Required content fields must be validated before publication.

Administrative operations must enforce server-side authorization.

## 8. Solve Records and Statistics

### 8.1 Solve Records as Source Data

Solve records are the source data for solve history and performance statistics.

The database must preserve the relationship between each solve and its owner.

### 8.2 Statistics Calculation

Statistics are derived from eligible solve records.

The initial architecture should calculate statistics from persisted solve data rather than treating manually maintained aggregate values as the source of truth.

Redis may be used for caching selected statistics when appropriate.

### 8.3 Data Consistency

When a solve is created, edited or deleted, affected statistics must reflect the updated dataset.

Derived statistics must be reproducible from the underlying eligible solve records and approved calculation rules.

Statistics formulas are implemented in the Statistics module and are derived from persisted solve records. The MVP exposes the agreed timer statistics (Single, PB, Ao5, Ao12, Ao50, Ao100) where applicable. DNF and +2 handling must follow the relevant metric's calculation rules; DNF is not treated as a numeric duration. The exact WCA-style trimming, rounding/display precision, eligibility filters, and time-window/session filters must be specified in the Statistics implementation contract before those metrics are released. These rules do not change the underlying solve records.

## 9. Data Types and Storage Conventions

The following conventions apply:

- Timestamps must use a canonical storage format.
- User-facing date and time formatting must be handled according to the selected locale and timezone policy.
- Elapsed solve time is stored as integer milliseconds in a BIGINT column (`duration_ms`).
- Primary and foreign keys use UUID.
- Structured lesson content and user settings use JSONB with backend schema validation.
- Refresh-token values are stored only as cryptographic hashes in PostgreSQL.
- File contents must be stored in Object Storage.
- PostgreSQL must store media metadata and references rather than binary file contents where possible.
- JSON fields should be used only where flexible structured data is justified.

Exact SQL column types and precision are to be finalized during implementation.

## 10. Database Migrations

Alembic is used to manage database schema changes.

Requirements:

- Every schema change must be represented by a versioned migration.
- Migrations must be reviewed before production deployment.
- Migrations must preserve existing data where required.
- Destructive changes must be handled carefully.
- Database schema changes must be reproducible across environments.

Manual production schema changes outside the migration process should be avoided.

## 10.1 Account and Session Data Lifecycle

Account deletion must remove or anonymize user-owned data according to an approved retention policy. The exact retention periods and legal basis are not yet defined and must be reviewed before production launch.

Refresh-token session records must be revocable immediately. Expired/revoked session cleanup must not remove evidence required to detect refresh-token reuse before the configured security retention window has elapsed.

## 11. Redis and Caching

Redis is used as a supporting cache.

It may store:

- Frequently accessed course data.
- Selected statistics results.
- Other temporary data where caching provides measurable benefits.

Redis must not become the source of truth for persistent entities.

Cache invalidation must be considered when underlying data changes.

## 12. Future Domain Extensions

The database design should allow future expansion without introducing unnecessary MVP complexity.

Potential future entities include:

- Algorithm.
- Exercise.
- TrainingSession.
- Challenge.
- Achievement.
- UserAchievement.
- CurrencyTransaction.
- CosmeticItem.
- UserCosmeticItem.
- Subscription.
- Competition.
- Leaderboard.

These entities are not part of the initial MVP database scope unless explicitly approved later.

## 13. Open Database Decisions

The following decisions are resolved at the domain-design level. Remaining implementation or product details are explicitly listed as open items.

| Decision | Status |
|---|---|
| Primary key strategy | UUID v4 — decided |
| Account identity and uniqueness policy | Normalized, case-insensitive unique email — decided |
| Exact profile fields | Username, display name, avatar media reference, optional bio — proposed MVP schema |
| Exact MVP settings | Inspection mode, inspection alerts, timer sound, theme — proposed MVP scope |
| Lesson content representation | Versioned structured JSONB content blocks — decided |
| Lesson completion conditions | Explicit completion action; `NOT_STARTED`, `IN_PROGRESS`, `COMPLETED` — decided |
| Course and lesson publication states | `DRAFT`, `PUBLISHED`, `ARCHIVED`; lesson availability also depends on parent course — decided |
| Solve duration storage precision | Integer milliseconds (`BIGINT`) — decided |
| Solve penalties and DNF representation | `NONE`, `PLUS_TWO`, `DNF` enum; raw duration preserved — decided |
| Solve metadata and session model | Optional scramble/method metadata; separate `SolveSession` — decided for domain model |
| Statistics formulas and inclusion rules | Statistics derived in Statistics module; exact formulas, DNF trimming and rounding rules remain to be specified |
| Media upload and ownership model | Object Storage for files; PostgreSQL metadata and ownership reference — decided |
| Data deletion and retention policies | Account deletion workflow, retention periods and anonymization requirements — open |
| Exact role and permission model | `USER` and `ADMIN`; backend RBAC, no separate permission entity for MVP — decided |
| Refresh-token persistence and lifecycle | PostgreSQL hashed-token records, rotation and revocation — decided |
| Refresh-token transport | Secure transport mechanism (cookie/header) — to be finalized in Authentication and Security design |

## 14. Related Documents

- `SYSTEM_ARCHITECTURE.md`
- `BACKEND_ARCHITECTURE.md`
- `API_DESIGN.md`
- `AUTHENTICATION_AND_SECURITY.md`
- `INFRASTRUCTURE_AND_DEVOPS.md`
- `README.md`