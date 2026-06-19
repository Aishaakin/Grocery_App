#!/bin/bash
echo "🛒 Starting RecipeCart..."
echo ""
echo "Make sure GEMINI_API_KEY is set:"
echo "  export GEMINI_API_KEY=your_key_here"
echo ""
cd backend
pip install -r requirements.txt -q
uvicorn main:app --reload --port 8000
