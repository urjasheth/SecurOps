#!/bin/bash

# Run tool installation
echo "📦 Installing security tools..."
./scripts/install_tools.sh

# Set up Python virtual environment
if [ ! -d "venv" ]; then
    echo "🐍 Creating virtual environment..."
    python3 -m venv venv
fi

# Install Python dependencies
echo "🐍 Installing Python dependencies..."
source venv/bin/activate
pip install -r requirements.txt
pip install -e .

# Configure Git hooks
echo "🔧 Configuring Git hooks..."
./scripts/setup_hooks.sh

echo "🚀 SecurOps setup complete! You can now run 'securop scan'."
