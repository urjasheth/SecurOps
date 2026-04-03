#!/bin/bash
# Pre-commit hook for SecurOps

# Run security scan
echo "🚀 Running SecurOps security scan..."
securop scan --fast

# Check exit code
if [ $? -ne 0 ]; then
    echo "❌ Security scan failed. Commit aborted."
    exit 1
fi

echo "✅ Security scan passed. Proceeding with commit."
exit 0
