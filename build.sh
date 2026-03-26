#!/bin/bash
echo "🚀 Starting build process..."

# Install dependencies
echo "📦 Installing Python dependencies..."
pip install -r requirements.txt

# Create vector database
echo "🗄️ Building vector database..."
python -c "from app.vector_store import create_vector_db; create_vector_db()"

echo "✅ Build completed successfully!"