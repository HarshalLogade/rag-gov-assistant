#!/bin/bash
set -e

echo "🚀 Starting build process..."
echo "Python version: $(python --version)"
echo "Pip version: $(pip --version)"

# Verify Python version is 3.11
python_version=$(python -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")')
if [[ "$python_version" != "3.11" ]]; then
    echo "⚠️  Warning: Expected Python 3.11 but got $python_version"
    echo "This may cause compatibility issues with faiss-cpu"
fi

# Install dependencies
echo "📦 Installing Python dependencies..."
pip install --no-cache-dir -r requirements.txt

# Verify critical packages
echo "✅ Verifying installations..."
python -c "import fastapi; print(f'FastAPI: {fastapi.__version__}')"
python -c "import langchain; print(f'LangChain: {langchain.__version__}')"
python -c "import sentence_transformers; print('Sentence Transformers OK')"

# Create vector database
echo "🗄️ Building vector database..."
python -c "import sys; sys.path.insert(0, '.'); from app.vector_store import create_vector_db; create_vector_db()"

echo "✅ Build completed successfully!"