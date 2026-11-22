# ADR-0010: S3-Compatible Object Storage for Media

- **Status:** Accepted
- **Date:** 2026-11-22
- **Scope:** MVP

## Context

Cubiland includes course and lesson media. Binary assets should not be stored in PostgreSQL or depend on the lifecycle of an application container.

## Decision

Store media binaries in **S3-compatible Object Storage**. Store media metadata and references in PostgreSQL. Use backend-authorized presigned upload URLs for direct uploads from the frontend.

## Alternatives Considered

- **Store binary files in PostgreSQL:** not selected because object storage is a better fit for media assets.
- **Store files on the VPS filesystem:** not selected because it couples media durability and capacity to one application server.
- **Proxy every upload through FastAPI:** not selected for the planned MVP flow because direct presigned uploads reduce backend data transfer.

## Consequences

**Benefits**
- Separates binary storage from relational application data.
- Supports direct uploads without routing file bytes through FastAPI.
- Allows the storage provider to be selected independently.

**Trade-offs**
- Introduces an external storage dependency.
- Requires secure credential, upload and deletion handling.
- Provider, bucket configuration and exact file limits remain deployment decisions.

## Implementation Notes

The backend issues short-lived presigned URLs after validating authorization and requested metadata. The frontend uploads directly to object storage and then registers media metadata with the backend. The backend verifies object metadata before creating the media record. Do not delete an object while it is still referenced by published content.

## Related Documents

- `../SYSTEM_ARCHITECTURE.md`
- `../DOMAIN_AND_DATABASE.md`
- `../API_DESIGN.md`
- `../INFRASTRUCTURE_AND_DEVOPS.md`
