#!/bin/bash
set -e

echo "🚀 Starting build process..." | tee /dev/stderr
echo "Python version: $(python --version)" | tee /dev/stderr

# Install dependencies
echo "📦 Installing Python dependencies..." | tee /dev/stderr
pip install --no-cache-dir -r requirements.txt

# Create vector database
echo "🗄️ Building vector database..." | tee /dev/stderr
python -c "
import sys
sys.path.insert(0, '.')
from app.vector_store import create_vector_db
create_vector_db()
" 2>&1

echo "✅ Build completed successfully!" | tee /dev/stderr