# Git Workflow

This document describes the Git branching strategy and pull request workflow for Cubiland.

## Branching Strategy

### Main Branches

- **main** — Stable branch for production releases. Only merged after testing and approval.
- **develop** — Primary development integration branch. All feature branches merge here.

### Supporting Branches

- **feature/*** — New features and functionality.
- **fix/*** — Bug fixes.
- **docs/*** — Documentation changes.
- **refactor/*** — Code refactoring without functional changes.

## Workflow

### 1. Create a Branch

Create a new branch from `develop`:

```bash
git checkout develop
git pull origin develop
git checkout -b feature/your-feature-name
```

Use appropriate prefixes:
- `feature/` for new features
- `fix/` for bug fixes
- `docs/` for documentation
- `refactor/` for refactoring

### 2. Implement Changes

Make your changes and commit using conventional commit messages:

```bash
git add .
git commit -m "feat: add user registration endpoint"
```

Commit message format:
- `feat:` — New feature
- `fix:` — Bug fix
- `docs:` — Documentation changes
- `refactor:` — Code refactoring
- `test:` — Adding or updating tests
- `chore:` — Maintenance tasks

Examples:
- `feat: add email verification flow`
- `fix: resolve token expiration issue`
- `docs: update API documentation`
- `refactor: extract email service abstraction`

### 3. Push Branch

Push your branch to the remote repository:

```bash
git push -u origin feature/your-feature-name
```

### 4. Open Pull Request

Open a Pull Request targeting `develop`:

1. Go to GitHub and create a Pull Request.
2. Use the provided [Pull Request Template](../../.github/PULL_REQUEST_TEMPLATE.md).
3. Fill in the Summary, Changes, Type of Change, Testing, and Checklist.

### 5. Review and Merge

- Independent code review is optional for the solo-developer workflow.
- Merge the PR into `develop` after all required CI checks pass; no approving review or conversation resolution is required.
- Use "Squash and merge" to keep history clean.

### 6. Release to Main

When `develop` is stable and ready for release:

**Option A: Direct Pull Request (No Release Branch)**

If no release branch is needed:
1. Open a Pull Request from `develop` to `main`.
2. Merge it after the required CI checks pass.
3. Tag the release:
   ```bash
   git tag -a v1.0.0 -m "Release version 1.0.0"
   git push origin v1.0.0
   ```

**Option B: Release Branch (Formal Process)**

1. Create a release branch from `develop`:
   ```bash
   git checkout develop
   git pull origin develop
   git checkout -b release/v1.0.0
   ```

2. Perform final testing and version bumping.

3. Open a Pull Request from `release/v1.0.0` to `main` and merge after all required CI checks pass.

4. Tag the release:
   ```bash
   git tag -a v1.0.0 -m "Release version 1.0.0"
   git push origin v1.0.0
   ```

5. Open a Pull Request from `release/v1.0.0` back to `develop` and merge after review.

6. Delete the release branch:
   ```bash
   git branch -d release/v1.0.0
   git push origin --delete release/v1.0.0
   ```

## Branch Protection Rules

Configure branch protection manually in GitHub repository settings for both branches.

### Required Settings

- Require a Pull Request before merging into `main` or `develop`.
- Require the `Backend CI / Backend checks` status check to pass. This single required job covers Ruff lint and format checks, mypy, pytest, Alembic migration validation, and the Docker build; every check must pass for the job to succeed.
- Block direct pushes and bypasses so protected-branch changes go through a Pull Request and successful CI.
- Do not require approving reviews or enable `Require conversation resolution`. Independent code review is not required, and open conversation threads must not block a merge.

These settings allow the solo developer to merge their own Pull Request once CI succeeds.

### Optional Settings

Other branch-protection settings are optional. Enable them only when they remain compatible with merging a solo-authored Pull Request after required CI passes.

### main Branch
- Require Pull Requests and the `Backend CI / Backend checks` status check.
- Block direct pushes and bypasses.

### develop Branch
- Require Pull Requests and the `Backend CI / Backend checks` status check.
- Block direct pushes and bypasses.

## Pull Request Guidelines

### Before Opening a PR

- Ensure your code follows project conventions.
- Run tests locally if applicable.
- Update documentation if your changes affect it.
- Review your own changes for unrelated modifications.

### During Review

- Respond to review feedback promptly.
- Keep PRs focused on a single concern.
- If a PR becomes too large, consider splitting it.

### After Merge

- Delete your feature branch:
  ```bash
  git branch -d feature/your-feature-name
  git push origin --delete feature/your-feature-name
  ```

## Conventional Commits

Use conventional commit messages for better traceability:

```
<type>[optional scope]: <description>

[optional body]

[optional footer]
```

Types:
- `feat`: A new feature
- `fix`: A bug fix
- `docs`: Documentation only changes
- `style`: Changes that do not affect code meaning (formatting, etc.)
- `refactor`: Code change that neither fixes a bug nor adds a feature
- `perf`: Performance improvement
- `test`: Adding or updating tests
- `chore`: Maintenance tasks
- `ci`: CI/CD changes

Examples:
```
feat(auth): add refresh token rotation
fix(database): resolve connection pool exhaustion
docs(api): update authentication endpoint documentation
refactor(email): extract email service interface
```

## Conflict Resolution

When merging conflicts occur:

1. Pull latest changes from the target branch:
   ```bash
   git checkout develop
   git pull origin develop
   ```

2. Checkout your branch and rebase:
   ```bash
   git checkout feature/your-feature-name
   git rebase develop
   ```

3. Resolve conflicts and continue:
   ```bash
   git add <resolved-files>
   git rebase --continue
   ```

4. Force push your branch:
   ```bash
   git push --force-with-lease origin feature/your-feature-name
   ```

## Related Documents

- [Development Setup](DEVELOPMENT_SETUP.md)
- [Pull Request Template](../../.github/PULL_REQUEST_TEMPLATE.md)
- [ADR-0009: GitHub Actions CI and Deferred Production CD](../04-architecture/decisions/ADR-0009-github-actions-ci-and-deferred-cd.md)
