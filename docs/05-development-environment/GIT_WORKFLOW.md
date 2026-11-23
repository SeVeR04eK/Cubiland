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
4. Request review from team members (if applicable).

### 5. Review and Merge

- If working with a team, reviewers provide feedback and request changes if needed.
- Address feedback and push additional commits.
- Once approved (or self-reviewed for solo development), merge the PR into `develop`.
- Use "Squash and merge" to keep history clean.

### 6. Release to Main

When `develop` is stable and ready for release:

**Option A: Direct Merge (Solo Development)**

If no release branch is needed:
1. Merge `develop` into `main`:
   ```bash
   git checkout main
   git merge develop
   git push origin main
   ```
2. Tag the release:
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

3. Merge `release/v1.0.0` into `main`:
   ```bash
   git checkout main
   git merge release/v1.0.0
   git push origin main
   ```

4. Tag the release:
   ```bash
   git tag -a v1.0.0 -m "Release version 1.0.0"
   git push origin v1.0.0
   ```

5. Merge back to `develop`:
   ```bash
   git checkout develop
   git merge release/v1.0.0
   git push origin develop
   ```

6. Delete the release branch:
   ```bash
   git branch -d release/v1.0.0
   git push origin --delete release/v1.0.0
   ```

## Branch Protection Rules

Configure branch protection on GitHub when the project has a team or CI workflows:

### For Solo Development (Current Phase)

- No mandatory reviewers required
- No CI status checks required (CI not yet implemented)
- Optional: Require pull request before merging to main

### For Team Development (Future)

### main Branch
- Require pull request before merging
- Require status checks to pass before merging (when CI is implemented)
- Require approval from at least 1 reviewer
- Do not allow bypassing the above settings

### develop Branch
- Require pull request before merging
- Require status checks to pass before merging (when CI is implemented)
- Require approval from at least 1 reviewer

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
