#!/bin/bash
echo "🛒 Starting RecipeCart..."
cd backend
pip install -r requirements.txt -q
uvicorn main:app --reload --port 8000
