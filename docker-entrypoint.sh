#!/bin/bash
set -e

# Create necessary directories
mkdir -p /app/logs
mkdir -p /app/workspace
mkdir -p ~/.metagpt

# Load environment variables if .env exists
if [ -f /app/.env ]; then
    export $(cat /app/.env | grep -v '^#' | xargs)
fi

echo "Starting MetaGPT application..."
echo "OpenAI API Key: ${OPENAI_API_KEY:0:10}..."
echo "Google API Key: ${GOOGLE_API_KEY:0:10}..."

# Run the application
python /app/app.py
