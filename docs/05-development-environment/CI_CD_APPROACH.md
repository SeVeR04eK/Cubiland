# CI/CD Approach

This document describes the planned CI/CD approach for Cubiland. The project is currently in the architecture phase, so CI workflows will be implemented when functional code and tests exist.

## Current Status

**No CI workflows are currently implemented.**

The project is in the Architecture & Technical Design phase. Functional Backend and Frontend applications and tests are not yet implemented. CI workflows will be added when:

- Backend has functional code to test
- Frontend has functional code to test
- Test suites are established
- Build processes are defined

## Planned CI Architecture

### Backend CI Workflow

When implemented, the Backend CI workflow will run on:

- Pull Requests targeting `main` or `develop`
- Pushes to `main` or `develop`

**Checks:**
- Ruff (linting and formatting)
- Type checking (mypy)
- pytest (unit and integration tests)
- Alembic migration validation
- Docker build validation

**Workflow Location:** `.github/workflows/backend-ci.yml`

### Frontend CI Workflow

When implemented, the Frontend CI workflow will run on:

- Pull Requests targeting `main` or `develop`
- Pushes to `main` or `develop`

**Checks:**
- ESLint (linting)
- Prettier (formatting)
- TypeScript type checking
- Vitest (unit tests)
- Production build verification

**Workflow Location:** `.github/workflows/frontend-ci.yml`

## Branch Protection Rules

When CI is implemented, configure branch protection:

### main Branch
- Require pull request before merging
- Require status checks to pass before merging
- Require approval from at least 1 reviewer
- Do not allow bypassing the above settings

### develop Branch
- Require pull request before merging
- Require status checks to pass before merging
- Require approval from at least 1 reviewer

## Deployment Strategy

### Current Phase (Architecture & Design)

- No automated deployment
- Manual local development with Docker Compose

### MVP Development Phase

- Continue manual local development
- No production deployment until MVP is complete

### Post-Release (Planned)

Per [ADR-0009: GitHub Actions CI and Deferred Production CD](../04-architecture/decisions/ADR-0009-github-actions-ci-and-deferred-cd.md):

- **CI:** Automated quality checks on Pull Requests
- **CD:** Manual controlled deployment for initial release
- **Future CD:** Automated deployment via GHCR and restricted SSH after release

### Planned Deployment Pipeline

After initial release, consider:

1. **Build and Publish:**
   - Build Docker images on merge to `main`
   - Publish to GitHub Container Registry (GHCR)
   - Tag images with version numbers

2. **Deploy:**
   - Manual trigger or automated on tag
   - SSH to production VPS
   - Pull new images
   - Run database migrations
   - Restart services with Docker Compose

3. **Rollback:**
   - Keep previous image versions
   - Quick rollback by switching to previous image tag

## Security Considerations

- Do not expose deployment secrets to untrusted Pull Request workflows
- Use GitHub Secrets for sensitive data (API keys, credentials)
- Use environment-specific secrets for staging and production
- Rotate credentials regularly
- Review and audit workflow permissions

## Related Documents

- [ADR-0009: GitHub Actions CI and Deferred Production CD](../04-architecture/decisions/ADR-0009-github-actions-ci-and-deferred-cd.md)
- [Infrastructure and DevOps](../04-architecture/INFRASTRUCTURE_AND_DEVOPS.md)
- [Git Workflow](GIT_WORKFLOW.md)
