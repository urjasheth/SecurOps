#!/bin/bash

# Define project root and .git hooks path
PROJECT_ROOT=$(git rev-parse --show-toplevel 2>/dev/null)
if [ -z "$PROJECT_ROOT" ]; then
    echo "❌ Error: Not a git repository. Please run this inside a git project."
    exit 1
fi

HOOKS_PATH="$PROJECT_ROOT/.git/hooks"
PRE_COMMIT_HOOK="$HOOKS_PATH/pre-commit"

# Copy hook script
cp hooks/pre-commit.sh "$PRE_COMMIT_HOOK"

# Make hook executable
chmod +x "$PRE_COMMIT_HOOK"

echo "✅ Git pre-commit hook installed at $PRE_COMMIT_HOOK"
