# ADR-0009: GitHub Actions CI and Deferred Production CD

- **Status:** Accepted
- **Date:** 2026-11-22
- **Scope:** MVP and post-release

## Context

Cubiland needs automated quality checks during development. Automatic production deployment is not necessary before the initial release and would add deployment risk while the product is still changing.

## Decision

Use **GitHub Actions** for CI on Pull Requests targeting `main`. Protect `main` and require successful checks before merge. Use a controlled manual production deployment for the initial release; defer automatic CD until after release.

## Alternatives Considered

- **Checks only after pushing to main:** not selected because Pull Request checks provide feedback before merge.
- **Automatic production deployment on every merge during pre-release development:** deferred to avoid premature production automation.

## Consequences

**Benefits**
- Problems are detected before code is merged.
- The main branch remains protected by required checks.
- Production release remains deliberate during MVP development.

**Trade-offs**
- Production deployment is manual before the initial release.
- A post-release deployment pipeline still needs to be implemented and secured.

## Implementation Notes

CI should include lint/format checks, type checking, tests, migration validation and Docker build validation as applicable. Do not expose deployment secrets to untrusted Pull Request workflows. After release, consider versioned images in GHCR and controlled VPS deployment over restricted SSH.

## Related Documents

- `../INFRASTRUCTURE_AND_DEVOPS.md`
