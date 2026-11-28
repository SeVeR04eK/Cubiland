# CI/CD Approach

This document describes the CI/CD approach and current implementation status for Cubiland.

## Current Status

**Backend CI is implemented. Frontend CI is planned and not implemented.**

The backend workflow runs on pushes and Pull Requests targeting `main` or `develop`. It validates the existing backend code, tests, migration setup and Docker image build.

## CI Architecture

### Backend CI Workflow

The Backend CI workflow runs on:

- Pull Requests targeting `main` or `develop`
- Pushes to `main` or `develop`

**Checks:**
- Ruff (linting and formatting)
- Type checking (mypy)
- pytest (unit and integration tests)
- Alembic migration validation
- Docker build validation

**Workflow Location:** `.github/workflows/backend-ci.yml`

**Implemented checks:**
- Ruff linting and formatting checks using the backend configuration.
- mypy static type checking for `backend/src`.
- pytest using the backend's configured test suite.
- Alembic history, heads and upgrade validation against a disposable PostgreSQL service.
- Docker build validation using `backend/Dockerfile` and `backend/` as the build context.

The Alembic configuration is initialized, but no migration revisions exist yet. The workflow verifies the empty migration history and exercises the migration command against the temporary database; it cannot yet validate application schema changes.

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

Configure these rules manually in GitHub repository settings for both branches.

**Required settings:**
- Require a Pull Request before merging into `main` or `develop`.
- Require the `Backend CI / Backend checks` status check to pass before merging. This job includes Ruff lint and format checks, mypy, pytest, Alembic migration validation, and the Docker build; all must pass for the job to succeed.
- Prevent direct pushes and bypasses so changes can enter protected branches only through a Pull Request that passes CI.

Independent code review is not required for this solo-developer workflow. Do not require approving reviews or enable `Require conversation resolution`; a developer may merge their own Pull Request when required CI passes, even if conversations remain open.

**Optional settings:** GitHub's other branch-protection options may be enabled when useful, provided they do not prevent solo PR merges after successful CI. The workflow itself uses read-only `contents` permissions and does not change repository settings.

### main Branch
- Require Pull Requests and the `Backend CI / Backend checks` status check.
- Block direct pushes and bypasses.
- Do not require approving reviews or conversation resolution.

### develop Branch
- Require Pull Requests and the `Backend CI / Backend checks` status check.
- Block direct pushes and bypasses.
- Do not require approving reviews or conversation resolution.

Select the status check after the workflow has completed successfully at least once on GitHub.

## Deployment Strategy

### Current Phase (Backend Foundation / Early MVP)

- No automated deployment
- Manual local development with Docker Compose

### MVP Development Phase

- Continue manual local development
- No production deployment until MVP is complete

### Post-Release (Planned)

Per [ADR-0009: GitHub Actions CI and Deferred Production CD](../04-architecture/decisions/ADR-0009-github-actions-ci-and-deferred-cd.md):

- **CI:** Automated backend quality checks on Pull Requests and pushes to `main` and `develop`.
- **CD:** Deferred. This workflow does not deploy, publish images to GHCR, or use SSH.
- **Future CD:** Any post-release deployment pipeline remains a separate future decision and implementation.

### Planned Deployment Pipeline

After initial release, deployment automation may be considered separately:

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
