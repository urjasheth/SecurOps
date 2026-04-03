# SecurOps Local Security Toolkit

SecurOps is a developer-friendly, one-command installable security toolkit that runs locally without Docker and integrates into any project.

## Overview

Aims for:
- Fast local scanning (< 10 seconds in fast mode)
- Secret detection (Gitleaks)
- Static code analysis (Semgrep)
- Dependency scanning (Trivy)
- Automated Git pre-commit hook integration
- **CI/CD Pipeline Integration**
- **Mobile Security Rules (Flutter, iOS, Android)**

## Installation

Run the main setup script in your project root:

```bash
chmod +x scripts/setup.sh scripts/install_tools.sh scripts/setup_hooks.sh
./scripts/setup.sh
```

This will:
1. Install Gitleaks, Semgrep, and Trivy binaries.
2. Set up a Python virtual environment.
3. Install the `securop` CLI tool.
4. Configure a Git pre-commit hook to run scans before every commit.

## Usage

### Local Scan

```bash
# Fast mode (default, for local dev)
securop scan

# CI mode (full scan, strict exit codes)
securop scan --ci

# Verbose mode
securop scan --verbose
```

### CI/CD Integration

SecurOps supports automated scanning in CI pipelines.

#### GitHub Actions
A workflow is provided in `.github/workflows/securop.yml`. It uploads SARIF results to the GitHub Security tab.

#### Azure DevOps
A pipeline configuration is provided in `azure-pipelines.yml`.

## Mobile Security Rules

The toolkit includes specialized Semgrep rules for mobile development:
- **Flutter (Dart)**: Insecure HTTP, hardcoded Firebase Keys, debug banner detection.
- **iOS (Swift/XML)**: Insecure HTTP, hardcoded secrets, ATS (App Transport Security) monitoring.
- **Android (Kotlin/Java/XML)**: Insecure HTTP, hardcoded Firebase Keys, debuggable flag detection.

## Features

- **Fast Mode**: Specifically designed for developer speed. Gitleaks checks only staged changes, Trivy only checks High/Critical vulnerabilities.
- **Git Hook**: Automatically blocks commits if security issues are found.
- **Full CI Scans**: High-fidelity scans for build pipelines that fail on any high/critical finding.

## Troubleshooting

- Ensure you have `python3` and `pip` installed.
- On macOS, make sure `brew` is available.
- If you encounter permission errors, consider running scripts with `sudo` if necessary (though not recommended for everything).
