#!/bin/bash

# Function to check if a command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Install Gitleaks
if command_exists gitleaks; then
    echo "✅ Gitleaks already installed."
else
    echo "Installing Gitleaks..."
    if [[ "$OSTYPE" == "darwin"* ]]; then
        brew install gitleaks
    else
        curl -sSL https://github.com/gitleaks/gitleaks/releases/download/v8.18.2/gitleaks_8.18.2_linux_x64.tar.gz | tar xz
        sudo mv gitleaks /usr/local/bin/
    fi
fi

# Semgrep is now installed via requirements.txt in the virtual environment.

# Install Trivy
if command_exists trivy; then
    echo "✅ Trivy already installed."
else
    echo "Installing Trivy..."
    if [[ "$OSTYPE" == "darwin"* ]]; then
        brew install aquasecurity/trivy/trivy
    else
        curl -sfL https://raw.githubusercontent.com/aquasecurity/trivy/main/contrib/install.sh | sh -s -- -b /usr/local/bin v0.49.1
    fi
fi
