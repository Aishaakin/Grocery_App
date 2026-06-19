🛒 RecipeCart Smart Grocery List Calculator

A grocery shopping tool. Pick a recipe category, choose a dish, and instantly get a full ingredient list with Nigerian Naira prices then add items to your cart and checkout.
Tech Stack
Layer 	Tech
Frontend 	HTML, CSS, JavaScript
Backend 	Python + FastAPI
AI 	Fast AP
Project Structure

grocery-app/
├── backend/
│   ├── main.py              # FastAPI server
│   └── requirements.txt     # Python dependencies
├── frontend/
│   ├── index.html           # App UI
│   ├── style.css            # Styling
│   └── app.js               # Frontend logic
└── README.md

Setup & Run

cd backend
pip install -r requirements.txt
uvicorn main:app --reload --port 8000

3. Open the frontend

Open frontend/index.html in the browser (or use Live Server in VS Code).
Features

    Food recipes by category (Breakfast, Lunch, Dinner, etc.)
    🛒 Ingredient shopping list with estimated NGN prices
    💰 Real-time cart total calculation
    ✅ Checkout confirmation modal
    📱 Responsive design

API Endpoints
Method 	Endpoint 	Description
GET 	/categories 	Returns available meal categories
POST 	/recipes 	Send 6 recipes
POST 	/ingredients 	Send ingredient list + prices
