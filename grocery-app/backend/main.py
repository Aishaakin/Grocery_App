from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Smart Grocery API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

RECIPES = {
    "Breakfast": [
        {"id":"1","name":"Scrambled Eggs & Toast","description":"Fluffy scrambled eggs served with buttered toast.","cook_time":"10 mins","difficulty":"Easy","emoji":"🍳","servings":2},
        {"id":"2","name":"Pancakes","description":"Golden fluffy pancakes with syrup and fresh fruit.","cook_time":"20 mins","difficulty":"Easy","emoji":"🥞","servings":2},
        {"id":"3","name":"Avocado Toast","description":"Toasted bread topped with smashed avocado and seasoning.","cook_time":"10 mins","difficulty":"Easy","emoji":"🥑","servings":2},
        {"id":"4","name":"Oatmeal Porridge","description":"Creamy oats cooked with milk and topped with banana.","cook_time":"15 mins","difficulty":"Easy","emoji":"🥣","servings":2},
        {"id":"5","name":"French Toast","description":"Egg-dipped bread fried golden and dusted with sugar.","cook_time":"15 mins","difficulty":"Easy","emoji":"🍞","servings":2},
        {"id":"6","name":"Vegetable Omelette","description":"Fluffy omelette filled with peppers, onions, and tomatoes.","cook_time":"15 mins","difficulty":"Medium","emoji":"🍳","servings":2},
    ],
    "Lunch": [
        {"id":"1","name":"Jollof Rice","description":"Nigerian spiced tomato rice cooked to perfection.","cook_time":"45 mins","difficulty":"Medium","emoji":"🍚","servings":2},
        {"id":"2","name":"Chicken Sandwich","description":"Grilled chicken breast with lettuce and mayo in a bun.","cook_time":"20 mins","difficulty":"Easy","emoji":"🥪","servings":2},
        {"id":"3","name":"Fried Rice","description":"Stir-fried rice with vegetables, eggs and soy sauce.","cook_time":"30 mins","difficulty":"Medium","emoji":"🍳","servings":2},
        {"id":"4","name":"Egusi Soup & Pounded Yam","description":"Rich melon seed soup served with smooth pounded yam.","cook_time":"60 mins","difficulty":"Hard","emoji":"🍲","servings":2},
        {"id":"5","name":"Pasta Salad","description":"Cold pasta tossed with vegetables and Italian dressing.","cook_time":"20 mins","difficulty":"Easy","emoji":"🍝","servings":2},
        {"id":"6","name":"Moi Moi","description":"Steamed bean pudding with eggs and peppers.","cook_time":"50 mins","difficulty":"Medium","emoji":"🫘","servings":2},
    ],
    "Dinner": [
        {"id":"1","name":"Pepper Soup","description":"Spicy Nigerian broth with assorted meat and herbs.","cook_time":"45 mins","difficulty":"Medium","emoji":"🍵","servings":2},
        {"id":"2","name":"Grilled Chicken & Rice","description":"Marinated grilled chicken thighs served with white rice.","cook_time":"40 mins","difficulty":"Medium","emoji":"🍗","servings":2},
        {"id":"3","name":"Spaghetti Bolognese","description":"Classic pasta with rich minced meat tomato sauce.","cook_time":"35 mins","difficulty":"Medium","emoji":"🍝","servings":2},
        {"id":"4","name":"Banga Soup & Starch","description":"Palm fruit soup served with smooth starch.","cook_time":"60 mins","difficulty":"Hard","emoji":"🌴","servings":2},
        {"id":"5","name":"Beef Stew & Yam","description":"Rich tomato beef stew served over boiled yam.","cook_time":"50 mins","difficulty":"Medium","emoji":"🥘","servings":2},
        {"id":"6","name":"Okra Soup","description":"Smooth okra soup with fish and assorted meat.","cook_time":"40 mins","difficulty":"Medium","emoji":"🌿","servings":2},
    ],
    "Snacks": [
        {"id":"1","name":"Puff Puff","description":"Deep-fried fluffy dough balls lightly sweetened.","cook_time":"25 mins","difficulty":"Easy","emoji":"🟡","servings":2},
        {"id":"2","name":"Spring Rolls","description":"Crispy rolls stuffed with vegetables and ground beef.","cook_time":"30 mins","difficulty":"Medium","emoji":"🥢","servings":2},
        {"id":"3","name":"Chin Chin","description":"Crunchy fried dough snack with a hint of nutmeg.","cook_time":"40 mins","difficulty":"Medium","emoji":"🍪","servings":2},
        {"id":"4","name":"Akara","description":"Crispy fried bean cakes with peppers and onions.","cook_time":"30 mins","difficulty":"Medium","emoji":"🫘","servings":2},
        {"id":"5","name":"Plantain Chips","description":"Thinly sliced plantain fried until crispy and golden.","cook_time":"20 mins","difficulty":"Easy","emoji":"🍌","servings":2},
        {"id":"6","name":"Meat Pie","description":"Flaky pastry filled with seasoned minced meat and potatoes.","cook_time":"50 mins","difficulty":"Hard","emoji":"🥧","servings":2},
    ],
    "Desserts": [
        {"id":"1","name":"Banana Pudding","description":"Creamy vanilla pudding layered with banana slices.","cook_time":"20 mins","difficulty":"Easy","emoji":"🍌","servings":2},
        {"id":"2","name":"Chocolate Cake","description":"Moist chocolate sponge with rich chocolate frosting.","cook_time":"60 mins","difficulty":"Hard","emoji":"🎂","servings":2},
        {"id":"3","name":"Fruit Salad","description":"Fresh seasonal fruits tossed in a light honey dressing.","cook_time":"10 mins","difficulty":"Easy","emoji":"🍓","servings":2},
        {"id":"4","name":"Ice Cream Sundae","description":"Vanilla ice cream topped with chocolate sauce and nuts.","cook_time":"5 mins","difficulty":"Easy","emoji":"🍨","servings":2},
        {"id":"5","name":"Pineapple Upside-Down Cake","description":"Caramelised pineapple rings baked into golden sponge.","cook_time":"50 mins","difficulty":"Medium","emoji":"🍍","servings":2},
        {"id":"6","name":"Biscuit Pudding","description":"No-bake layered biscuit and custard dessert.","cook_time":"15 mins","difficulty":"Easy","emoji":"🍮","servings":2},
    ],
    "Drinks": [
        {"id":"1","name":"Chapman","description":"Nigerian fruity cocktail with Fanta, Grenadine and cucumber.","cook_time":"10 mins","difficulty":"Easy","emoji":"🍹","servings":2},
        {"id":"2","name":"Zobo Drink","description":"Chilled hibiscus tea sweetened with pineapple and ginger.","cook_time":"30 mins","difficulty":"Easy","emoji":"🌺","servings":2},
        {"id":"3","name":"Kunu","description":"Creamy millet drink spiced with ginger and pepper.","cook_time":"40 mins","difficulty":"Medium","emoji":"🥛","servings":2},
        {"id":"4","name":"Mango Smoothie","description":"Blended fresh mango with milk and a hint of vanilla.","cook_time":"5 mins","difficulty":"Easy","emoji":"🥭","servings":2},
        {"id":"5","name":"Ginger Lemonade","description":"Fresh lemon juice blended with ginger and honey.","cook_time":"15 mins","difficulty":"Easy","emoji":"🍋","servings":2},
        {"id":"6","name":"Tigernut Milk","description":"Creamy plant-based milk made from tigernuts and dates.","cook_time":"20 mins","difficulty":"Easy","emoji":"🌰","servings":2},
    ],
}

INGREDIENTS = {
    "Scrambled Eggs & Toast": [
        {"id":"1","name":"Eggs","quantity":4,"unit":"pieces","price_per_unit":200,"total_price":800,"category":"Dairy"},
        {"id":"2","name":"Bread loaf","quantity":1,"unit":"loaf","price_per_unit":800,"total_price":800,"category":"Bakery"},
        {"id":"3","name":"Butter","quantity":2,"unit":"tbsp","price_per_unit":150,"total_price":300,"category":"Dairy"},
        {"id":"4","name":"Salt","quantity":1,"unit":"tsp","price_per_unit":50,"total_price":50,"category":"Spices"},
        {"id":"5","name":"Black pepper","quantity":0.5,"unit":"tsp","price_per_unit":100,"total_price":50,"category":"Spices"},
        {"id":"6","name":"Milk","quantity":2,"unit":"tbsp","price_per_unit":100,"total_price":200,"category":"Dairy"},
    ],
    "Pancakes": [
        {"id":"1","name":"All-purpose flour","quantity":2,"unit":"cups","price_per_unit":400,"total_price":800,"category":"Pantry"},
        {"id":"2","name":"Eggs","quantity":2,"unit":"pieces","price_per_unit":200,"total_price":400,"category":"Dairy"},
        {"id":"3","name":"Milk","quantity":1,"unit":"cup","price_per_unit":300,"total_price":300,"category":"Dairy"},
        {"id":"4","name":"Sugar","quantity":2,"unit":"tbsp","price_per_unit":100,"total_price":200,"category":"Pantry"},
        {"id":"5","name":"Butter","quantity":2,"unit":"tbsp","price_per_unit":150,"total_price":300,"category":"Dairy"},
        {"id":"6","name":"Baking powder","quantity":1,"unit":"tsp","price_per_unit":100,"total_price":100,"category":"Pantry"},
        {"id":"7","name":"Maple syrup","quantity":4,"unit":"tbsp","price_per_unit":500,"total_price":2000,"category":"Pantry"},
    ],
    "Avocado Toast": [
        {"id":"1","name":"Bread loaf","quantity":1,"unit":"loaf","price_per_unit":800,"total_price":800,"category":"Bakery"},
        {"id":"2","name":"Avocado","quantity":2,"unit":"pieces","price_per_unit":500,"total_price":1000,"category":"Produce"},
        {"id":"3","name":"Lemon","quantity":1,"unit":"piece","price_per_unit":100,"total_price":100,"category":"Produce"},
        {"id":"4","name":"Salt","quantity":1,"unit":"tsp","price_per_unit":50,"total_price":50,"category":"Spices"},
        {"id":"5","name":"Red pepper flakes","quantity":0.5,"unit":"tsp","price_per_unit":150,"total_price":75,"category":"Spices"},
        {"id":"6","name":"Olive oil","quantity":1,"unit":"tbsp","price_per_unit":300,"total_price":300,"category":"Pantry"},
    ],
    "Oatmeal Porridge": [
        {"id":"1","name":"Rolled oats","quantity":2,"unit":"cups","price_per_unit":600,"total_price":1200,"category":"Pantry"},
        {"id":"2","name":"Milk","quantity":2,"unit":"cups","price_per_unit":300,"total_price":600,"category":"Dairy"},
        {"id":"3","name":"Banana","quantity":2,"unit":"pieces","price_per_unit":150,"total_price":300,"category":"Produce"},
        {"id":"4","name":"Honey","quantity":2,"unit":"tbsp","price_per_unit":400,"total_price":800,"category":"Pantry"},
        {"id":"5","name":"Cinnamon","quantity":0.5,"unit":"tsp","price_per_unit":200,"total_price":100,"category":"Spices"},
        {"id":"6","name":"Salt","quantity":1,"unit":"pinch","price_per_unit":50,"total_price":50,"category":"Spices"},
    ],
    "French Toast": [
        {"id":"1","name":"Bread loaf","quantity":1,"unit":"loaf","price_per_unit":800,"total_price":800,"category":"Bakery"},
        {"id":"2","name":"Eggs","quantity":3,"unit":"pieces","price_per_unit":200,"total_price":600,"category":"Dairy"},
        {"id":"3","name":"Milk","quantity":0.5,"unit":"cup","price_per_unit":300,"total_price":150,"category":"Dairy"},
        {"id":"4","name":"Sugar","quantity":2,"unit":"tbsp","price_per_unit":100,"total_price":200,"category":"Pantry"},
        {"id":"5","name":"Cinnamon","quantity":1,"unit":"tsp","price_per_unit":200,"total_price":200,"category":"Spices"},
        {"id":"6","name":"Butter","quantity":2,"unit":"tbsp","price_per_unit":150,"total_price":300,"category":"Dairy"},
        {"id":"7","name":"Vanilla extract","quantity":1,"unit":"tsp","price_per_unit":300,"total_price":300,"category":"Pantry"},
    ],
    "Vegetable Omelette": [
        {"id":"1","name":"Eggs","quantity":4,"unit":"pieces","price_per_unit":200,"total_price":800,"category":"Dairy"},
        {"id":"2","name":"Bell pepper","quantity":1,"unit":"piece","price_per_unit":200,"total_price":200,"category":"Produce"},
        {"id":"3","name":"Onion","quantity":1,"unit":"piece","price_per_unit":150,"total_price":150,"category":"Produce"},
        {"id":"4","name":"Tomato","quantity":1,"unit":"piece","price_per_unit":100,"total_price":100,"category":"Produce"},
        {"id":"5","name":"Butter","quantity":1,"unit":"tbsp","price_per_unit":150,"total_price":150,"category":"Dairy"},
        {"id":"6","name":"Salt & pepper","quantity":1,"unit":"tsp","price_per_unit":50,"total_price":50,"category":"Spices"},
    ],
    "Jollof Rice": [
        {"id":"1","name":"Long grain rice","quantity":2,"unit":"cups","price_per_unit":800,"total_price":1600,"category":"Pantry"},
        {"id":"2","name":"Tomatoes","quantity":4,"unit":"pieces","price_per_unit":100,"total_price":400,"category":"Produce"},
        {"id":"3","name":"Tomato paste","quantity":2,"unit":"tbsp","price_per_unit":200,"total_price":400,"category":"Pantry"},
        {"id":"4","name":"Onion","quantity":1,"unit":"piece","price_per_unit":150,"total_price":150,"category":"Produce"},
        {"id":"5","name":"Chicken stock","quantity":2,"unit":"cups","price_per_unit":300,"total_price":600,"category":"Pantry"},
        {"id":"6","name":"Vegetable oil","quantity":3,"unit":"tbsp","price_per_unit":200,"total_price":600,"category":"Pantry"},
        {"id":"7","name":"Seasoning cubes","quantity":2,"unit":"pieces","price_per_unit":50,"total_price":100,"category":"Spices"},
        {"id":"8","name":"Curry powder","quantity":1,"unit":"tsp","price_per_unit":100,"total_price":100,"category":"Spices"},
    ],
    "Chicken Sandwich": [
        {"id":"1","name":"Chicken breast","quantity":2,"unit":"pieces","price_per_unit":1200,"total_price":2400,"category":"Meat & Seafood"},
        {"id":"2","name":"Burger buns","quantity":2,"unit":"pieces","price_per_unit":200,"total_price":400,"category":"Bakery"},
        {"id":"3","name":"Lettuce","quantity":4,"unit":"leaves","price_per_unit":50,"total_price":200,"category":"Produce"},
        {"id":"4","name":"Tomato","quantity":1,"unit":"piece","price_per_unit":100,"total_price":100,"category":"Produce"},
        {"id":"5","name":"Mayonnaise","quantity":2,"unit":"tbsp","price_per_unit":200,"total_price":400,"category":"Pantry"},
        {"id":"6","name":"Salt & pepper","quantity":1,"unit":"tsp","price_per_unit":50,"total_price":50,"category":"Spices"},
    ],
    "Fried Rice": [
        {"id":"1","name":"Long grain rice","quantity":2,"unit":"cups","price_per_unit":800,"total_price":1600,"category":"Pantry"},
        {"id":"2","name":"Eggs","quantity":2,"unit":"pieces","price_per_unit":200,"total_price":400,"category":"Dairy"},
        {"id":"3","name":"Carrots","quantity":2,"unit":"pieces","price_per_unit":100,"total_price":200,"category":"Produce"},
        {"id":"4","name":"Green peas","quantity":0.5,"unit":"cup","price_per_unit":300,"total_price":150,"category":"Frozen"},
        {"id":"5","name":"Soy sauce","quantity":2,"unit":"tbsp","price_per_unit":400,"total_price":800,"category":"Pantry"},
        {"id":"6","name":"Vegetable oil","quantity":2,"unit":"tbsp","price_per_unit":200,"total_price":400,"category":"Pantry"},
        {"id":"7","name":"Onion","quantity":1,"unit":"piece","price_per_unit":150,"total_price":150,"category":"Produce"},
        {"id":"8","name":"Seasoning cube","quantity":1,"unit":"piece","price_per_unit":50,"total_price":50,"category":"Spices"},
    ],
    "Egusi Soup & Pounded Yam": [
        {"id":"1","name":"Egusi (melon seeds)","quantity":2,"unit":"cups","price_per_unit":1200,"total_price":2400,"category":"Pantry"},
        {"id":"2","name":"Yam tuber","quantity":1,"unit":"piece","price_per_unit":1500,"total_price":1500,"category":"Produce"},
        {"id":"3","name":"Assorted meat","quantity":500,"unit":"g","price_per_unit":2500,"total_price":2500,"category":"Meat & Seafood"},
        {"id":"4","name":"Palm oil","quantity":3,"unit":"tbsp","price_per_unit":300,"total_price":900,"category":"Pantry"},
        {"id":"5","name":"Crayfish","quantity":2,"unit":"tbsp","price_per_unit":400,"total_price":800,"category":"Pantry"},
        {"id":"6","name":"Ugu leaves","quantity":1,"unit":"bunch","price_per_unit":200,"total_price":200,"category":"Produce"},
        {"id":"7","name":"Seasoning cubes","quantity":2,"unit":"pieces","price_per_unit":50,"total_price":100,"category":"Spices"},
        {"id":"8","name":"Salt & pepper","quantity":1,"unit":"tsp","price_per_unit":50,"total_price":50,"category":"Spices"},
    ],
    "Pasta Salad": [
        {"id":"1","name":"Pasta (penne)","quantity":2,"unit":"cups","price_per_unit":600,"total_price":1200,"category":"Pantry"},
        {"id":"2","name":"Bell pepper","quantity":1,"unit":"piece","price_per_unit":200,"total_price":200,"category":"Produce"},
        {"id":"3","name":"Cucumber","quantity":1,"unit":"piece","price_per_unit":200,"total_price":200,"category":"Produce"},
        {"id":"4","name":"Cherry tomatoes","quantity":10,"unit":"pieces","price_per_unit":50,"total_price":500,"category":"Produce"},
        {"id":"5","name":"Italian dressing","quantity":3,"unit":"tbsp","price_per_unit":500,"total_price":1500,"category":"Pantry"},
        {"id":"6","name":"Olives","quantity":0.5,"unit":"cup","price_per_unit":800,"total_price":400,"category":"Pantry"},
        {"id":"7","name":"Salt & pepper","quantity":1,"unit":"tsp","price_per_unit":50,"total_price":50,"category":"Spices"},
    ],
    "Moi Moi": [
        {"id":"1","name":"Black-eyed beans","quantity":2,"unit":"cups","price_per_unit":600,"total_price":1200,"category":"Pantry"},
        {"id":"2","name":"Eggs","quantity":2,"unit":"pieces","price_per_unit":200,"total_price":400,"category":"Dairy"},
        {"id":"3","name":"Bell pepper","quantity":2,"unit":"pieces","price_per_unit":200,"total_price":400,"category":"Produce"},
        {"id":"4","name":"Onion","quantity":1,"unit":"piece","price_per_unit":150,"total_price":150,"category":"Produce"},
        {"id":"5","name":"Vegetable oil","quantity":2,"unit":"tbsp","price_per_unit":200,"total_price":400,"category":"Pantry"},
        {"id":"6","name":"Crayfish","quantity":1,"unit":"tbsp","price_per_unit":400,"total_price":400,"category":"Pantry"},
        {"id":"7","name":"Seasoning cubes","quantity":2,"unit":"pieces","price_per_unit":50,"total_price":100,"category":"Spices"},
    ],
    "Pepper Soup": [
        {"id":"1","name":"Assorted meat (goat/chicken)","quantity":500,"unit":"g","price_per_unit":2500,"total_price":2500,"category":"Meat & Seafood"},
        {"id":"2","name":"Pepper soup spice mix","quantity":2,"unit":"tbsp","price_per_unit":300,"total_price":600,"category":"Spices"},
        {"id":"3","name":"Onion","quantity":1,"unit":"piece","price_per_unit":150,"total_price":150,"category":"Produce"},
        {"id":"4","name":"Uziza leaves","quantity":1,"unit":"bunch","price_per_unit":200,"total_price":200,"category":"Produce"},
        {"id":"5","name":"Crayfish","quantity":1,"unit":"tbsp","price_per_unit":400,"total_price":400,"category":"Pantry"},
        {"id":"6","name":"Seasoning cubes","quantity":2,"unit":"pieces","price_per_unit":50,"total_price":100,"category":"Spices"},
        {"id":"7","name":"Salt","quantity":1,"unit":"tsp","price_per_unit":50,"total_price":50,"category":"Spices"},
    ],
    "Grilled Chicken & Rice": [
        {"id":"1","name":"Chicken thighs","quantity":4,"unit":"pieces","price_per_unit":700,"total_price":2800,"category":"Meat & Seafood"},
        {"id":"2","name":"White rice","quantity":2,"unit":"cups","price_per_unit":800,"total_price":1600,"category":"Pantry"},
        {"id":"3","name":"Garlic","quantity":3,"unit":"cloves","price_per_unit":50,"total_price":150,"category":"Produce"},
        {"id":"4","name":"Lemon","quantity":1,"unit":"piece","price_per_unit":100,"total_price":100,"category":"Produce"},
        {"id":"5","name":"Olive oil","quantity":2,"unit":"tbsp","price_per_unit":300,"total_price":600,"category":"Pantry"},
        {"id":"6","name":"Paprika","quantity":1,"unit":"tsp","price_per_unit":150,"total_price":150,"category":"Spices"},
        {"id":"7","name":"Salt & pepper","quantity":1,"unit":"tsp","price_per_unit":50,"total_price":50,"category":"Spices"},
    ],
    "Spaghetti Bolognese": [
        {"id":"1","name":"Spaghetti","quantity":250,"unit":"g","price_per_unit":800,"total_price":800,"category":"Pantry"},
        {"id":"2","name":"Minced beef","quantity":300,"unit":"g","price_per_unit":2000,"total_price":2000,"category":"Meat & Seafood"},
        {"id":"3","name":"Tomato paste","quantity":3,"unit":"tbsp","price_per_unit":200,"total_price":600,"category":"Pantry"},
        {"id":"4","name":"Tomatoes","quantity":3,"unit":"pieces","price_per_unit":100,"total_price":300,"category":"Produce"},
        {"id":"5","name":"Onion","quantity":1,"unit":"piece","price_per_unit":150,"total_price":150,"category":"Produce"},
        {"id":"6","name":"Garlic","quantity":3,"unit":"cloves","price_per_unit":50,"total_price":150,"category":"Produce"},
        {"id":"7","name":"Olive oil","quantity":2,"unit":"tbsp","price_per_unit":300,"total_price":600,"category":"Pantry"},
        {"id":"8","name":"Italian seasoning","quantity":1,"unit":"tsp","price_per_unit":200,"total_price":200,"category":"Spices"},
    ],
    "Banga Soup & Starch": [
        {"id":"1","name":"Palm fruits","quantity":1,"unit":"bunch","price_per_unit":800,"total_price":800,"category":"Produce"},
        {"id":"2","name":"Starch (cocoyam)","quantity":2,"unit":"cups","price_per_unit":600,"total_price":1200,"category":"Pantry"},
        {"id":"3","name":"Assorted fish","quantity":300,"unit":"g","price_per_unit":1500,"total_price":1500,"category":"Meat & Seafood"},
        {"id":"4","name":"Banga spice","quantity":1,"unit":"pack","price_per_unit":300,"total_price":300,"category":"Spices"},
        {"id":"5","name":"Onion","quantity":1,"unit":"piece","price_per_unit":150,"total_price":150,"category":"Produce"},
        {"id":"6","name":"Crayfish","quantity":2,"unit":"tbsp","price_per_unit":400,"total_price":800,"category":"Pantry"},
        {"id":"7","name":"Salt","quantity":1,"unit":"tsp","price_per_unit":50,"total_price":50,"category":"Spices"},
    ],
    "Beef Stew & Yam": [
        {"id":"1","name":"Beef","quantity":400,"unit":"g","price_per_unit":2200,"total_price":2200,"category":"Meat & Seafood"},
        {"id":"2","name":"Yam tuber","quantity":1,"unit":"piece","price_per_unit":1500,"total_price":1500,"category":"Produce"},
        {"id":"3","name":"Tomatoes","quantity":4,"unit":"pieces","price_per_unit":100,"total_price":400,"category":"Produce"},
        {"id":"4","name":"Tomato paste","quantity":2,"unit":"tbsp","price_per_unit":200,"total_price":400,"category":"Pantry"},
        {"id":"5","name":"Onion","quantity":1,"unit":"piece","price_per_unit":150,"total_price":150,"category":"Produce"},
        {"id":"6","name":"Vegetable oil","quantity":3,"unit":"tbsp","price_per_unit":200,"total_price":600,"category":"Pantry"},
        {"id":"7","name":"Seasoning cubes","quantity":2,"unit":"pieces","price_per_unit":50,"total_price":100,"category":"Spices"},
    ],
    "Okra Soup": [
        {"id":"1","name":"Okra","quantity":300,"unit":"g","price_per_unit":400,"total_price":400,"category":"Produce"},
        {"id":"2","name":"Assorted fish & meat","quantity":400,"unit":"g","price_per_unit":2000,"total_price":2000,"category":"Meat & Seafood"},
        {"id":"3","name":"Palm oil","quantity":2,"unit":"tbsp","price_per_unit":300,"total_price":600,"category":"Pantry"},
        {"id":"4","name":"Crayfish","quantity":2,"unit":"tbsp","price_per_unit":400,"total_price":800,"category":"Pantry"},
        {"id":"5","name":"Onion","quantity":1,"unit":"piece","price_per_unit":150,"total_price":150,"category":"Produce"},
        {"id":"6","name":"Seasoning cubes","quantity":2,"unit":"pieces","price_per_unit":50,"total_price":100,"category":"Spices"},
        {"id":"7","name":"Salt","quantity":1,"unit":"tsp","price_per_unit":50,"total_price":50,"category":"Spices"},
    ],
    "Puff Puff": [
        {"id":"1","name":"All-purpose flour","quantity":3,"unit":"cups","price_per_unit":400,"total_price":1200,"category":"Pantry"},
        {"id":"2","name":"Dry yeast","quantity":1,"unit":"tsp","price_per_unit":200,"total_price":200,"category":"Pantry"},
        {"id":"3","name":"Sugar","quantity":4,"unit":"tbsp","price_per_unit":100,"total_price":400,"category":"Pantry"},
        {"id":"4","name":"Salt","quantity":0.5,"unit":"tsp","price_per_unit":50,"total_price":25,"category":"Spices"},
        {"id":"5","name":"Vegetable oil (for frying)","quantity":2,"unit":"cups","price_per_unit":600,"total_price":1200,"category":"Pantry"},
        {"id":"6","name":"Warm water","quantity":1,"unit":"cup","price_per_unit":0,"total_price":0,"category":"Pantry"},
        {"id":"7","name":"Nutmeg","quantity":0.5,"unit":"tsp","price_per_unit":150,"total_price":75,"category":"Spices"},
    ],
    "Spring Rolls": [
        {"id":"1","name":"Spring roll wrappers","quantity":10,"unit":"pieces","price_per_unit":100,"total_price":1000,"category":"Pantry"},
        {"id":"2","name":"Ground beef","quantity":200,"unit":"g","price_per_unit":2000,"total_price":2000,"category":"Meat & Seafood"},
        {"id":"3","name":"Cabbage","quantity":1,"unit":"cup","price_per_unit":300,"total_price":300,"category":"Produce"},
        {"id":"4","name":"Carrots","quantity":2,"unit":"pieces","price_per_unit":100,"total_price":200,"category":"Produce"},
        {"id":"5","name":"Vegetable oil (for frying)","quantity":2,"unit":"cups","price_per_unit":600,"total_price":1200,"category":"Pantry"},
        {"id":"6","name":"Soy sauce","quantity":1,"unit":"tbsp","price_per_unit":400,"total_price":400,"category":"Pantry"},
        {"id":"7","name":"Seasoning cube","quantity":1,"unit":"piece","price_per_unit":50,"total_price":50,"category":"Spices"},
    ],
    "Chin Chin": [
        {"id":"1","name":"All-purpose flour","quantity":3,"unit":"cups","price_per_unit":400,"total_price":1200,"category":"Pantry"},
        {"id":"2","name":"Eggs","quantity":2,"unit":"pieces","price_per_unit":200,"total_price":400,"category":"Dairy"},
        {"id":"3","name":"Sugar","quantity":3,"unit":"tbsp","price_per_unit":100,"total_price":300,"category":"Pantry"},
        {"id":"4","name":"Butter","quantity":2,"unit":"tbsp","price_per_unit":150,"total_price":300,"category":"Dairy"},
        {"id":"5","name":"Nutmeg","quantity":0.5,"unit":"tsp","price_per_unit":150,"total_price":75,"category":"Spices"},
        {"id":"6","name":"Milk","quantity":3,"unit":"tbsp","price_per_unit":100,"total_price":300,"category":"Dairy"},
        {"id":"7","name":"Vegetable oil (for frying)","quantity":2,"unit":"cups","price_per_unit":600,"total_price":1200,"category":"Pantry"},
    ],
    "Akara": [
        {"id":"1","name":"Black-eyed beans","quantity":2,"unit":"cups","price_per_unit":600,"total_price":1200,"category":"Pantry"},
        {"id":"2","name":"Onion","quantity":1,"unit":"piece","price_per_unit":150,"total_price":150,"category":"Produce"},
        {"id":"3","name":"Scotch bonnet pepper","quantity":2,"unit":"pieces","price_per_unit":50,"total_price":100,"category":"Produce"},
        {"id":"4","name":"Salt","quantity":1,"unit":"tsp","price_per_unit":50,"total_price":50,"category":"Spices"},
        {"id":"5","name":"Vegetable oil (for frying)","quantity":2,"unit":"cups","price_per_unit":600,"total_price":1200,"category":"Pantry"},
    ],
    "Plantain Chips": [
        {"id":"1","name":"Unripe plantain","quantity":3,"unit":"pieces","price_per_unit":300,"total_price":900,"category":"Produce"},
        {"id":"2","name":"Vegetable oil (for frying)","quantity":2,"unit":"cups","price_per_unit":600,"total_price":1200,"category":"Pantry"},
        {"id":"3","name":"Salt","quantity":1,"unit":"tsp","price_per_unit":50,"total_price":50,"category":"Spices"},
        {"id":"4","name":"Pepper (optional)","quantity":0.5,"unit":"tsp","price_per_unit":100,"total_price":50,"category":"Spices"},
    ],
    "Meat Pie": [
        {"id":"1","name":"All-purpose flour","quantity":3,"unit":"cups","price_per_unit":400,"total_price":1200,"category":"Pantry"},
        {"id":"2","name":"Minced beef","quantity":300,"unit":"g","price_per_unit":2000,"total_price":2000,"category":"Meat & Seafood"},
        {"id":"3","name":"Butter","quantity":100,"unit":"g","price_per_unit":800,"total_price":800,"category":"Dairy"},
        {"id":"4","name":"Potatoes","quantity":2,"unit":"pieces","price_per_unit":200,"total_price":400,"category":"Produce"},
        {"id":"5","name":"Carrots","quantity":2,"unit":"pieces","price_per_unit":100,"total_price":200,"category":"Produce"},
        {"id":"6","name":"Onion","quantity":1,"unit":"piece","price_per_unit":150,"total_price":150,"category":"Produce"},
        {"id":"7","name":"Seasoning cube","quantity":1,"unit":"piece","price_per_unit":50,"total_price":50,"category":"Spices"},
        {"id":"8","name":"Egg (for egg wash)","quantity":1,"unit":"piece","price_per_unit":200,"total_price":200,"category":"Dairy"},
    ],
    "Banana Pudding": [
        {"id":"1","name":"Bananas","quantity":3,"unit":"pieces","price_per_unit":150,"total_price":450,"category":"Produce"},
        {"id":"2","name":"Vanilla custard powder","quantity":3,"unit":"tbsp","price_per_unit":200,"total_price":600,"category":"Pantry"},
        {"id":"3","name":"Milk","quantity":2,"unit":"cups","price_per_unit":300,"total_price":600,"category":"Dairy"},
        {"id":"4","name":"Sugar","quantity":3,"unit":"tbsp","price_per_unit":100,"total_price":300,"category":"Pantry"},
        {"id":"5","name":"Digestive biscuits","quantity":1,"unit":"pack","price_per_unit":500,"total_price":500,"category":"Bakery"},
        {"id":"6","name":"Whipped cream","quantity":1,"unit":"cup","price_per_unit":800,"total_price":800,"category":"Dairy"},
    ],
    "Chocolate Cake": [
        {"id":"1","name":"All-purpose flour","quantity":2,"unit":"cups","price_per_unit":400,"total_price":800,"category":"Pantry"},
        {"id":"2","name":"Cocoa powder","quantity":0.75,"unit":"cup","price_per_unit":800,"total_price":600,"category":"Pantry"},
        {"id":"3","name":"Sugar","quantity":2,"unit":"cups","price_per_unit":400,"total_price":800,"category":"Pantry"},
        {"id":"4","name":"Eggs","quantity":3,"unit":"pieces","price_per_unit":200,"total_price":600,"category":"Dairy"},
        {"id":"5","name":"Butter","quantity":150,"unit":"g","price_per_unit":800,"total_price":800,"category":"Dairy"},
        {"id":"6","name":"Milk","quantity":1,"unit":"cup","price_per_unit":300,"total_price":300,"category":"Dairy"},
        {"id":"7","name":"Baking powder","quantity":2,"unit":"tsp","price_per_unit":100,"total_price":200,"category":"Pantry"},
        {"id":"8","name":"Chocolate frosting","quantity":1,"unit":"pack","price_per_unit":1200,"total_price":1200,"category":"Pantry"},
    ],
    "Fruit Salad": [
        {"id":"1","name":"Watermelon","quantity":0.5,"unit":"piece","price_per_unit":1500,"total_price":750,"category":"Produce"},
        {"id":"2","name":"Pineapple","quantity":0.5,"unit":"piece","price_per_unit":800,"total_price":400,"category":"Produce"},
        {"id":"3","name":"Banana","quantity":2,"unit":"pieces","price_per_unit":150,"total_price":300,"category":"Produce"},
        {"id":"4","name":"Strawberries","quantity":10,"unit":"pieces","price_per_unit":100,"total_price":1000,"category":"Produce"},
        {"id":"5","name":"Honey","quantity":2,"unit":"tbsp","price_per_unit":400,"total_price":800,"category":"Pantry"},
        {"id":"6","name":"Lemon juice","quantity":1,"unit":"tbsp","price_per_unit":100,"total_price":100,"category":"Produce"},
    ],
    "Ice Cream Sundae": [
        {"id":"1","name":"Vanilla ice cream","quantity":4,"unit":"scoops","price_per_unit":400,"total_price":1600,"category":"Frozen"},
        {"id":"2","name":"Chocolate sauce","quantity":4,"unit":"tbsp","price_per_unit":300,"total_price":1200,"category":"Pantry"},
        {"id":"3","name":"Crushed peanuts","quantity":2,"unit":"tbsp","price_per_unit":200,"total_price":400,"category":"Pantry"},
        {"id":"4","name":"Whipped cream","quantity":0.5,"unit":"cup","price_per_unit":800,"total_price":400,"category":"Dairy"},
        {"id":"5","name":"Cherries","quantity":4,"unit":"pieces","price_per_unit":100,"total_price":400,"category":"Produce"},
    ],
    "Pineapple Upside-Down Cake": [
        {"id":"1","name":"All-purpose flour","quantity":1.5,"unit":"cups","price_per_unit":400,"total_price":600,"category":"Pantry"},
        {"id":"2","name":"Pineapple rings","quantity":1,"unit":"can","price_per_unit":1200,"total_price":1200,"category":"Pantry"},
        {"id":"3","name":"Butter","quantity":100,"unit":"g","price_per_unit":800,"total_price":800,"category":"Dairy"},
        {"id":"4","name":"Brown sugar","quantity":0.5,"unit":"cup","price_per_unit":500,"total_price":250,"category":"Pantry"},
        {"id":"5","name":"Eggs","quantity":2,"unit":"pieces","price_per_unit":200,"total_price":400,"category":"Dairy"},
        {"id":"6","name":"Milk","quantity":0.5,"unit":"cup","price_per_unit":300,"total_price":150,"category":"Dairy"},
        {"id":"7","name":"Baking powder","quantity":1.5,"unit":"tsp","price_per_unit":100,"total_price":150,"category":"Pantry"},
    ],
    "Biscuit Pudding": [
        {"id":"1","name":"Digestive biscuits","quantity":2,"unit":"packs","price_per_unit":500,"total_price":1000,"category":"Bakery"},
        {"id":"2","name":"Milk","quantity":2,"unit":"cups","price_per_unit":300,"total_price":600,"category":"Dairy"},
        {"id":"3","name":"Custard powder","quantity":3,"unit":"tbsp","price_per_unit":200,"total_price":600,"category":"Pantry"},
        {"id":"4","name":"Sugar","quantity":3,"unit":"tbsp","price_per_unit":100,"total_price":300,"category":"Pantry"},
        {"id":"5","name":"Vanilla extract","quantity":1,"unit":"tsp","price_per_unit":300,"total_price":300,"category":"Pantry"},
        {"id":"6","name":"Whipped cream","quantity":1,"unit":"cup","price_per_unit":800,"total_price":800,"category":"Dairy"},
    ],
    "Chapman": [
        {"id":"1","name":"Fanta Orange","quantity":1,"unit":"bottle","price_per_unit":300,"total_price":300,"category":"Beverages"},
        {"id":"2","name":"Sprite","quantity":1,"unit":"bottle","price_per_unit":300,"total_price":300,"category":"Beverages"},
        {"id":"3","name":"Grenadine syrup","quantity":2,"unit":"tbsp","price_per_unit":400,"total_price":800,"category":"Beverages"},
        {"id":"4","name":"Cucumber","quantity":0.5,"unit":"piece","price_per_unit":200,"total_price":100,"category":"Produce"},
        {"id":"5","name":"Lemon","quantity":1,"unit":"piece","price_per_unit":100,"total_price":100,"category":"Produce"},
        {"id":"6","name":"Ice cubes","quantity":10,"unit":"pieces","price_per_unit":0,"total_price":0,"category":"Frozen"},
        {"id":"7","name":"Angostura bitters","quantity":2,"unit":"drops","price_per_unit":500,"total_price":500,"category":"Beverages"},
    ],
    "Zobo Drink": [
        {"id":"1","name":"Dried hibiscus flowers (zobo)","quantity":2,"unit":"cups","price_per_unit":500,"total_price":1000,"category":"Pantry"},
        {"id":"2","name":"Pineapple","quantity":0.5,"unit":"piece","price_per_unit":800,"total_price":400,"category":"Produce"},
        {"id":"3","name":"Fresh ginger","quantity":1,"unit":"piece","price_per_unit":100,"total_price":100,"category":"Produce"},
        {"id":"4","name":"Cloves","quantity":5,"unit":"pieces","price_per_unit":20,"total_price":100,"category":"Spices"},
        {"id":"5","name":"Sugar","quantity":4,"unit":"tbsp","price_per_unit":100,"total_price":400,"category":"Pantry"},
        {"id":"6","name":"Water","quantity":4,"unit":"cups","price_per_unit":0,"total_price":0,"category":"Pantry"},
    ],
    "Kunu": [
        {"id":"1","name":"Millet","quantity":2,"unit":"cups","price_per_unit":500,"total_price":1000,"category":"Pantry"},
        {"id":"2","name":"Fresh ginger","quantity":1,"unit":"piece","price_per_unit":100,"total_price":100,"category":"Produce"},
        {"id":"3","name":"Cloves","quantity":4,"unit":"pieces","price_per_unit":20,"total_price":80,"category":"Spices"},
        {"id":"4","name":"Sugar","quantity":4,"unit":"tbsp","price_per_unit":100,"total_price":400,"category":"Pantry"},
        {"id":"5","name":"Water","quantity":4,"unit":"cups","price_per_unit":0,"total_price":0,"category":"Pantry"},
        {"id":"6","name":"Dates (optional)","quantity":5,"unit":"pieces","price_per_unit":100,"total_price":500,"category":"Pantry"},
    ],
    "Mango Smoothie": [
        {"id":"1","name":"Ripe mangoes","quantity":2,"unit":"pieces","price_per_unit":400,"total_price":800,"category":"Produce"},
        {"id":"2","name":"Milk","quantity":1,"unit":"cup","price_per_unit":300,"total_price":300,"category":"Dairy"},
        {"id":"3","name":"Vanilla extract","quantity":0.5,"unit":"tsp","price_per_unit":300,"total_price":150,"category":"Pantry"},
        {"id":"4","name":"Sugar","quantity":1,"unit":"tbsp","price_per_unit":100,"total_price":100,"category":"Pantry"},
        {"id":"5","name":"Ice cubes","quantity":6,"unit":"pieces","price_per_unit":0,"total_price":0,"category":"Frozen"},
    ],
    "Ginger Lemonade": [
        {"id":"1","name":"Lemons","quantity":4,"unit":"pieces","price_per_unit":100,"total_price":400,"category":"Produce"},
        {"id":"2","name":"Fresh ginger","quantity":1,"unit":"piece","price_per_unit":100,"total_price":100,"category":"Produce"},
        {"id":"3","name":"Honey","quantity":3,"unit":"tbsp","price_per_unit":400,"total_price":1200,"category":"Pantry"},
        {"id":"4","name":"Water","quantity":4,"unit":"cups","price_per_unit":0,"total_price":0,"category":"Pantry"},
        {"id":"5","name":"Ice cubes","quantity":8,"unit":"pieces","price_per_unit":0,"total_price":0,"category":"Frozen"},
        {"id":"6","name":"Mint leaves","quantity":5,"unit":"leaves","price_per_unit":50,"total_price":250,"category":"Produce"},
    ],
    "Tigernut Milk": [
        {"id":"1","name":"Tigernuts","quantity":2,"unit":"cups","price_per_unit":600,"total_price":1200,"category":"Pantry"},
        {"id":"2","name":"Dates","quantity":6,"unit":"pieces","price_per_unit":100,"total_price":600,"category":"Pantry"},
        {"id":"3","name":"Water","quantity":3,"unit":"cups","price_per_unit":0,"total_price":0,"category":"Pantry"},
        {"id":"4","name":"Vanilla extract","quantity":0.5,"unit":"tsp","price_per_unit":300,"total_price":150,"category":"Pantry"},
        {"id":"5","name":"Cinnamon","quantity":0.5,"unit":"tsp","price_per_unit":200,"total_price":100,"category":"Spices"},
    ],
}

@app.get("/")
def root():
    return {"message": "Smart Grocery API is running"}

@app.get("/categories")
def get_categories():
    return {"categories": list(RECIPES.keys())}

@app.post("/generate-recipes")
def generate_recipes(req: dict):
    category = req.get("category", "Dinner")
    servings = req.get("servings", 2)
    recipes = RECIPES.get(category, RECIPES["Dinner"])
    for r in recipes:
        r["servings"] = servings
    return {"recipes": recipes}

@app.post("/generate-ingredients")
def generate_ingredients(recipe: dict):
    name = recipe.get("name", "")
    ingredients = INGREDIENTS.get(name, [])
    total = sum(item.get("total_price", 0) for item in ingredients)
    return {"ingredients": ingredients, "total": total, "recipe_name": name}
