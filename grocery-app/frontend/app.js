const API = 'http://localhost:8000';

let selectedCategory = null;
let servings = 2;
let currentIngredients = [];
let currentRecipeName = '';
let cart = [];

// ─── INIT ────────────────────────────────────────────────────────────────────
async function init() {
  try {
    const res = await fetch(`${API}/categories`);
    const data = await res.json();
    renderCategoryPills(data.categories);
  } catch (e) {
    renderCategoryPills(["Breakfast","Lunch","Dinner","Snacks","Desserts","Drinks"]);
  }
}

// ─── CATEGORY PILLS ──────────────────────────────────────────────────────────
function renderCategoryPills(cats) {
  const row = document.getElementById('categoryPills');
  row.innerHTML = '';
  cats.forEach(cat => {
    const pill = document.createElement('button');
    pill.className = 'pill';
    pill.textContent = cat;
    pill.onclick = () => {
      document.querySelectorAll('.pill').forEach(p => p.classList.remove('active'));
      pill.classList.add('active');
      selectedCategory = cat;
      filterRecipes();
    };
    row.appendChild(pill);
  });
}

// ─── SERVINGS ────────────────────────────────────────────────────────────────
document.getElementById('servUp').onclick = () => {
  if (servings < 12) servings++;
  document.getElementById('servCount').textContent = servings;
};
document.getElementById('servDown').onclick = () => {
  if (servings > 1) servings--;
  document.getElementById('servCount').textContent = servings;
};


// ─── FIND RECIPES ────────────────────────────────────────────────────────────
document.getElementById('findRecipesBtn').onclick = async () => {
  if (!selectedCategory) { showToast('Please pick a category first'); return; }
  showLoader('Finding recipes...');
  try {
    const res = await fetch(`${API}/generate-recipes`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ category: selectedCategory, servings })
    });
    const data = await res.json();
    allRecipes = data.recipes;
    document.getElementById('searchInput').value = '';
    renderRecipeCards(allRecipes);
    document.getElementById('recipesSection').style.display = 'block';
    document.getElementById('ingredientsSection').style.display = 'none';
    document.getElementById('recipesSection').scrollIntoView({ behavior: 'smooth' });
  } catch (e) {
    showToast('Failed to load recipes. Is the server running?');
  } finally {
    hideLoader();
  }
};

// ─── RENDER RECIPES ──────────────────────────────────────────────────────────
function renderRecipeCards(recipes) {
  const grid = document.getElementById('recipeGrid');
  grid.innerHTML = '';
  if (recipes.length === 0) {
    grid.innerHTML = '<p style="color:var(--muted);grid-column:1/-1">No recipes found. Try a different search.</p>';
    return;
  }
  recipes.forEach(recipe => {
    const card = document.createElement('div');
    card.className = 'recipe-card';
    const diffClass = recipe.difficulty === 'Medium' ? 'diff-medium' : recipe.difficulty === 'Hard' ? 'diff-hard' : '';
    card.innerHTML = `
      <div class="recipe-emoji">${recipe.emoji}</div>
      <div class="recipe-name">${recipe.name}</div>
      <div class="recipe-desc">${recipe.description}</div>
      <div class="recipe-meta">
        <span class="tag">⏱ ${recipe.cook_time}</span>
        <span class="tag ${diffClass}">${recipe.difficulty}</span>
      </div>
    `;
    card.onclick = () => {
      document.querySelectorAll('.recipe-card').forEach(c => c.classList.remove('selected'));
      card.classList.add('selected');
      loadIngredients(recipe);
    };
    grid.appendChild(card);
  });
}

// ─── LOAD INGREDIENTS ────────────────────────────────────────────────────────
let baseIngredients = [];

async function loadIngredients(recipe) {
  showLoader('Building your shopping list...');
  try {
    const res = await fetch(`${API}/generate-ingredients`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(recipe)
    });
    const data = await res.json();
    baseIngredients = data.ingredients;
    currentRecipeName = data.recipe_name;
    currentIngredients = scaleIngredients(baseIngredients, servings);
    renderIngredients(currentIngredients, data.recipe_name);
    document.getElementById('ingredientsSection').style.display = 'block';
    document.getElementById('ingredientsSection').scrollIntoView({ behavior: 'smooth' });
  } catch (e) {
    showToast('Failed to load ingredients.');
  } finally {
    hideLoader();
  }
}

// ─── SERVING PRICE SCALING ───────────────────────────────────────────────────
function scaleIngredients(base, newServings) {
  const baseServings = 2;
  const ratio = newServings / baseServings;
  return base.map(ing => ({
    ...ing,
    quantity: +(ing.quantity * ratio).toFixed(1),
    total_price: Math.round(ing.total_price * ratio)
  }));
}

// Update ingredients when servings change
document.getElementById('servUp').addEventListener('click', refreshIngredients);
document.getElementById('servDown').addEventListener('click', refreshIngredients);

function refreshIngredients() {
  if (!baseIngredients.length) return;
  currentIngredients = scaleIngredients(baseIngredients, servings);
  renderIngredients(currentIngredients, currentRecipeName);
  // Sync cart items for this recipe
  cart = cart.filter(c => !baseIngredients.find(b => b.id === c.id));
  updateCartUI();
}

// ─── RENDER INGREDIENTS ──────────────────────────────────────────────────────
function renderIngredients(ingredients, recipeName) {
  document.getElementById('ingredientTitle').textContent = recipeName;
  document.getElementById('ingredientSubtitle').textContent =
    `${ingredients.length} ingredients · ${servings} servings`;
  const total = ingredients.reduce((s, i) => s + i.total_price, 0);
  document.getElementById('totalDisplay').textContent = formatNGN(total);

  const grid = document.getElementById('ingredientsGrid');
  grid.innerHTML = '';
  ingredients.forEach(ing => {
    const card = document.createElement('div');
    card.className = 'ingredient-card';
    card.id = `ing-${ing.id}`;
    const inCart = cart.some(c => c.id === ing.id);
    if (inCart) card.classList.add('in-cart');
    card.innerHTML = `
      <div class="ingredient-info">
        <div class="ingredient-name">${ing.name}</div>
        <div class="ingredient-qty">${ing.quantity} ${ing.unit}</div>
        <div class="ingredient-cat">${ing.category}</div>
      </div>
      <div style="display:flex;align-items:center;gap:10px">
        <div class="ingredient-price">${formatNGN(ing.total_price)}</div>
        <button class="add-btn ${inCart ? 'added' : ''}" id="btn-${ing.id}" onclick="toggleCartItem('${ing.id}')">
          ${inCart ? '✓' : '+'}
        </button>
      </div>
    `;
    grid.appendChild(card);
  });
}

// ─── CART LOGIC ─────────────
function toggleCartItem(id) {
  const ing = currentIngredients.find(i => i.id == id);
  if (!ing) return;
  const idx = cart.findIndex(c => c.id === id);
  if (idx >= 0) {
    cart.splice(idx, 1);
    showToast(`Removed ${ing.name}`);
  } else {
    cart.push({...ing});
    showToast(`Added ${ing.name} to cart`);
  }
  updateCartUI();
  const card = document.getElementById(`ing-${id}`);
  const btn = document.getElementById(`btn-${id}`);
  if (card && btn) {
    const inCart = cart.some(c => c.id === id);
    card.classList.toggle('in-cart', inCart);
    btn.classList.toggle('added', inCart);
    btn.textContent = inCart ? '✓' : '+';
  }
}

document.getElementById('addAllBtn').onclick = () => {
  currentIngredients.forEach(ing => {
    if (!cart.find(c => c.id === ing.id)) cart.push({...ing});
  });
  renderIngredients(currentIngredients, currentRecipeName);
  updateCartUI();
  showToast('All ingredients added to cart!');
};

function updateCartUI() {
  document.getElementById('cartCount').textContent = cart.length;
  const total = cart.reduce((s, i) => s + i.total_price, 0);
  document.getElementById('cartTotal').textContent = formatNGN(total);

  const container = document.getElementById('cartItems');
  if (cart.length === 0) {
    container.innerHTML = '<div class="cart-empty">Your cart is empty.<br>Add some ingredients!</div>';
    return;
  }
  container.innerHTML = '';
  cart.forEach(item => {
    const el = document.createElement('div');
    el.className = 'cart-item';
    el.innerHTML = `
      <div>
        <div class="cart-item-name">${item.name}</div>
        <div class="cart-item-qty">${item.quantity} ${item.unit}</div>
      </div>
      <div class="cart-item-right">
        <div class="cart-item-price">${formatNGN(item.total_price)}</div>
        <button class="remove-btn" onclick="removeFromCart('${item.id}')">✕</button>
      </div>
    `;
    container.appendChild(el);
  });
}

function removeFromCart(id) {
  cart = cart.filter(c => c.id !== id);
  updateCartUI();
  const card = document.getElementById(`ing-${id}`);
  const btn = document.getElementById(`btn-${id}`);
  if (card && btn) {
    card.classList.remove('in-cart');
    btn.classList.remove('added');
    btn.textContent = '+';
  }
}

// ─── CART SIDEBAR ───────────────────
document.getElementById('cartToggle').onclick = () => {
  document.getElementById('cartSidebar').classList.add('open');
  document.getElementById('cartOverlay').classList.add('open');
};
document.getElementById('closeCart').onclick = closeCart;
document.getElementById('cartOverlay').onclick = closeCart;
function closeCart() {
  document.getElementById('cartSidebar').classList.remove('open');
  document.getElementById('cartOverlay').classList.remove('open');
}

// ─── CHECKOUT  ──────────────────────
document.getElementById('checkoutBtn').onclick = () => {
  if (cart.length === 0) { showToast('Your cart is empty!'); return; }
  const total = cart.reduce((s, i) => s + i.total_price, 0);
  const orderItems = document.getElementById('orderItems');
  orderItems.innerHTML = '';
  cart.forEach(item => {
    const el = document.createElement('div');
    el.className = 'order-item';
    el.innerHTML = `
      <div>
        <div class="order-item-name">${item.name}</div>
        <div class="order-item-qty">${item.quantity} ${item.unit}</div>
      </div>
      <div class="order-item-price">${formatNGN(item.total_price)}</div>
    `;
    orderItems.appendChild(el);
  });
  document.getElementById('modalTotal').textContent = formatNGN(total);
  document.getElementById('checkoutModal').style.display = 'flex';
  closeCart();
};

document.getElementById('closeModal').onclick = () => {
  location.reload();
};

// ─── print to pdf ──────────────
document.getElementById('printBtn').onclick = () => {
  if (cart.length === 0) { showToast('Add ingredients to cart first!'); return; }
  const total = cart.reduce((s, i) => s + i.total_price, 0);
  const rows = cart.map(i =>
    `<tr><td>${i.name}</td><td>${i.quantity} ${i.unit}</td><td>${i.category}</td><td style="text-align:right;font-weight:600;color:#1a7a4a">${formatNGN(i.total_price)}</td></tr>`
  ).join('');

  const win = window.open('', '_blank');
  win.document.write(`
    <!DOCTYPE html>
    <html>
    <head>
      <title>Shopping List  ${currentRecipeName}</title>
      <style>
        body { font-family: Arial, sans-serif; padding: 32px; color: #111; }
        h1 { color: #1a7a4a; margin-bottom: 4px; }
        p { color: #6b7c6e; margin-top: 0; margin-bottom: 24px; }
        table { width: 100%; border-collapse: collapse; }
        th { background: #1a7a4a; color: white; padding: 10px 12px; text-align: left; }
        td { padding: 9px 12px; border-bottom: 1px solid #e2ebe4; }
        tr:last-child td { border-bottom: none; }
        .total { margin-top: 20px; text-align: right; font-size: 1.2rem; font-weight: 700; }
        .total span { color: #1a7a4a; font-size: 1.4rem; }
        .footer { margin-top: 32px; font-size: 0.8rem; color: #aaa; }
        @media print { button { display: none; } }
      </style>
    </head>
    <body>
      <h1>🛒 Recipe-Cart Grocery List Calculator</h1>
      <p>Recipe: <strong>${currentRecipeName}</strong> &nbsp;|&nbsp; Servings: <strong>${servings}</strong> &nbsp;|&nbsp; Date: <strong>${new Date().toLocaleDateString()}</strong></p>
      <table>
        <thead><tr><th>Ingredient</th><th>Quantity</th><th>Category</th><th style="text-align:right">Price</th></tr></thead>
        <tbody>${rows}</tbody>
      </table>
      <div class="total">Estimated Total: <span>${formatNGN(total)}</span></div>
      <div class="footer">Recipe-Cart Grocery Calculator</div>
      <br>
      <button onclick="window.print()" style="padding:10px 24px;background:#1a7a4a;color:white;border:none;border-radius:8px;cursor:pointer;font-size:1rem">🖨️ Print / Save as PDF</button>
      <button onclick="window.close()" style="padding:10px 24px;background:white;color:#1a7a4a;border:2px solid #1a7a4a;border-radius:8px;cursor:pointer;font-size:1rem;margin-left:10px">← Back to Cart</button>
      <button onclick="window.opener.document.getElementById('cartToggle').click(); window.close();" style="padding:10px 24px;background:#1a7a4a;color:white;border:none;border-radius:8px;cursor:pointer;font-size:1rem;margin-left:10px">🛒 Go to Checkout</button>
    </body>
    </html>
  `);
  win.document.close();
};

// ─── HELPERS ─────────────────────────────────────────────────────────────────
function formatNGN(amount) {
  return '₦' + Number(amount).toLocaleString('en-NG', { maximumFractionDigits: 0 });
}
function showLoader(text) {
  document.getElementById('loaderText').textContent = text;
  document.getElementById('loaderOverlay').style.display = 'flex';
}
function hideLoader() {
  document.getElementById('loaderOverlay').style.display = 'none';
}
let toastTimer;
function showToast(msg) {
  const toast = document.getElementById('toast');
  toast.textContent = msg;
  toast.classList.add('show');
  clearTimeout(toastTimer);
  toastTimer = setTimeout(() => toast.classList.remove('show'), 2500);
}

init();
