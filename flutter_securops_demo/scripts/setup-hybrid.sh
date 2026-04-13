#!/bin/bash
# setup-hybrid.sh - Single-command bootstrap for SecurOps Approach C
# Support: Android, iOS, Flutter, Web, .NET, PHP
set -e

echo "🚀 Bootstrapping SecurOps Hybrid Tier (Approach C)..."

# 1. Define Standard Files
FILES=(
    "semgrep-hybrid.yml"
    ".pre-commit-config-hybrid.yaml"
    "README.md"
    "SecurOps_Comparative_Strategy_Matrix_v2.md"
)

# 2. Fetch configurations
echo "📁 Copying security configurations..."
SOURCE_DIR="../securops-config-approch-c"

# Create target directories if they don't exist
mkdir -p .github/workflows

for file in "${FILES[@]}"; do
    if [ -f "$SOURCE_DIR/$file" ]; then
        cp "$SOURCE_DIR/$file" "./$file"
        echo "  ✅ $file copied."
    else
        echo "  ❌ Warning: $file not found in $SOURCE_DIR."
    fi
done

# Copy GitHub Workflow
if [ -f "$SOURCE_DIR/.github/workflows/securops-hybrid.yml" ]; then
    cp "$SOURCE_DIR/.github/workflows/securops-hybrid.yml" "./.github/workflows/securops-hybrid.yml"
    echo "  ✅ GitHub Workflow copied to .github/workflows/"
fi

# 3. Check / Install Native Tools
echo "🔍 Checking native dependencies..."

# Function to check tool
check_tool() {
    if command -v $1 &> /dev/null; then
        echo "  ✅ $1 found."
    else
        echo "  ⚠️ $1 NOT found. Please install it:"
        echo "     $2"
    fi
}

# Python for Semgrep
check_tool "semgrep" "pip install semgrep"

# TruffleHog (Client Requirement: Verified Secrets)
check_tool "trufflehog" "brew install trufflehog (macOS) or download from https://github.com/trufflesecurity/trufflehog"

# Trivy (Dependency Scanning)
check_tool "trivy" "brew install trivy (macOS) or download from https://github.com/aquasecurity/trivy"

# 4. Initialize Pre-Commit
if command -v pre-commit &> /dev/null; then
    echo "🪝 Initializing pre-commit..."
    # Backup existing config if any
    [ -f .pre-commit-config.yaml ] && mv .pre-commit-config.yaml .pre-commit-config.yaml.bak
    cp .pre-commit-config-hybrid.yaml .pre-commit-config.yaml
    pre-commit install
    echo "  ✅ Pre-commit hooks installed."
else
    echo "  ❌ pre-commit not found. Please install it first: pip install pre-commit"
fi

echo "--------------------------------------------------"
echo "✅ SecurOps Approach C Integrated!"
echo "Next Steps:"
echo "1. Run full scan: pre-commit run --all-files"
echo "2. Review rules: cat semgrep-hybrid.yml"
echo "--------------------------------------------------"
