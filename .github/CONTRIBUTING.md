# Contributing to DiffPriv-Gateway

Thank you for your interest in contributing to DiffPriv-Gateway. This project is an open-source Python differential privacy middleware prototype for SME analytics, with a focus on privacy-aware data processing, automated validation, and clear documentation.

Please keep contributions practical, focused, and aligned with the repository scope.

## Ways to Contribute

Useful contributions include:

- Bug reports with clear reproduction steps.
- Documentation improvements.
- Tests for existing behavior.
- Privacy mechanism validation.
- Code quality improvements that keep behavior stable.
- Small refactors that improve readability without changing project scope.

## Before Contributing

Before opening a pull request:

1. Check existing issues and pull requests for related work.
2. Create a focused issue when a discussion or design decision is needed.
3. Keep one logical change per pull request.
4. Avoid unrelated formatting, workflow, asset, notebook, or license changes.
5. Do not commit real personal data, secrets, or private credentials.

## Branch Naming

Use short, descriptive branch names:

- `feature/short-description`
- `fix/short-description`
- `docs/short-description`
- `test/short-description`
- `refactor/short-description`

Examples:

```bash
feature/add-query-validation
fix/handle-invalid-epsilon
docs/readme-quick-start
test/privacy-engine-validation
refactor/privacy-engine-helpers
```

## Local Setup

Create and activate a virtual environment.

Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Linux and macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

## Validation Commands

Run tests:

```bash
python -m pytest -v
```

Run linting:

```bash
python -m flake8 --exclude=.venv,__pycache__ main.py src tests
```

Both commands should pass before opening a pull request.

## Commit Messages

Use concise commit messages that describe the change:

```bash
feat: add gaussian mechanism support
fix: handle invalid epsilon values
docs: improve README quick start
test: extend privacy engine validation
```

## Pull Request Checklist

Before requesting review, confirm that:

- The scope is focused.
- Tests pass locally.
- Linting passes locally.
- Documentation is updated if behavior changed.
- No real or sensitive data is committed.
- No secrets, API keys, private credentials, or local environment files are included.
- The pull request explains the reason for the change and any validation performed.

## Privacy and Data Rules

DiffPriv-Gateway is a privacy-engineering project, so data handling matters even in examples and tests.

- Do not commit real personal data.
- Use synthetic or demo data only.
- Do not include private customer, employee, financial, health, or operational datasets.
- Do not expose secrets, API keys, access tokens, passwords, or private credentials.
- Keep proof-of-concept examples safe and minimal.
- Report security or privacy vulnerabilities privately, not through public issues.

## Code Style

Please keep code changes readable and maintainable:

- Write clear Python with explicit validation.
- Prefer small functions with focused responsibilities.
- Keep privacy parameters and assumptions visible.
- Add meaningful tests for behavior changes.
- Avoid unnecessary abstractions or unrelated rewrites.
- Follow the existing project structure.

## Community and Security

All participants are expected to follow the [Code of Conduct](CODE_OF_CONDUCT.md).

For security and privacy vulnerability reporting, see the [Security Policy](SECURITY.md).
