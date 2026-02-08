// Global state
let currentStage = 'brief';
let shoppingSpec = null;
let allProducts = {};
let selectedCart = {};
let retailers = {};

// Initialize
document.addEventListener('DOMContentLoaded', async () => {
    // Fetch retailers data
    const response = await fetch('/api/retailers');
    retailers = await response.json();
});

// Quick start scenarios
const scenarios = {
    skiing: "I need a complete downhill skiing outfit - jacket, pants, gloves, and goggles. Size M, warm and waterproof. Budget $400, delivery within 5 days.",
    football: "Super Bowl party outfit, team colors, head to toe, budget $150, delivered by Friday.",
    hackathon: "Hosting a hackathon for 60 people - need snacks, badges, adapters, decorations, and prizes. Best prices."
};

function quickStart(type) {
    document.getElementById('user-input').value = scenarios[type];
    sendMessage();
}

function handleKeyPress(event) {
    if (event.key === 'Enter') {
        sendMessage();
    }
}

function addMessage(role, content) {
    const messagesDiv = document.getElementById('messages');
    const messageDiv = document.createElement('div');
    messageDiv.className = `message ${role}`;
    
    const contentDiv = document.createElement('div');
    contentDiv.className = 'message-content';
    
    // Handle multi-line content
    const lines = content.split('\n');
    lines.forEach(line => {
        const lineDiv = document.createElement('div');
        lineDiv.textContent = line;
        contentDiv.appendChild(lineDiv);
    });
    
    messageDiv.appendChild(contentDiv);
    messagesDiv.appendChild(messageDiv);
    messagesDiv.scrollTop = messagesDiv.scrollHeight;
}

function showLoading() {
    const messagesDiv = document.getElementById('messages');
    const loadingDiv = document.createElement('div');
    loadingDiv.className = 'message agent';
    loadingDiv.id = 'loading-message';
    loadingDiv.innerHTML = '<div class="message-content"><div class="loading"></div></div>';
    messagesDiv.appendChild(loadingDiv);
    messagesDiv.scrollTop = messagesDiv.scrollHeight;
}

function hideLoading() {
    const loadingDiv = document.getElementById('loading-message');
    if (loadingDiv) {
        loadingDiv.remove();
    }
}

function updateStage(stage) {
    currentStage = stage;
    
    const stages = ['brief', 'discovery', 'ranking', 'cart', 'checkout'];
    const currentIndex = stages.indexOf(stage);
    
    stages.forEach((s, index) => {
        const elem = document.getElementById(`stage-${s}`);
        elem.classList.remove('active', 'completed');
        
        if (index < currentIndex) {
            elem.classList.add('completed');
        } else if (index === currentIndex) {
            elem.classList.add('active');
        }
    });
}

async function sendMessage() {
    const input = document.getElementById('user-input');
    const message = input.value.trim();
    
    if (!message) return;
    
    input.value = '';
    addMessage('user', message);
    showLoading();
    
    try {
        if (currentStage === 'brief') {
            // Parse brief
            const response = await fetch('/api/parse-brief', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ message })
            });
            
            shoppingSpec = await response.json();
            hideLoading();
            
            addMessage('agent', 
                `Perfect! I understand you need:\n\n` +
                `✓ Budget: $${shoppingSpec.budget}\n` +
                `✓ Delivery: Within ${shoppingSpec.delivery_days} days\n` +
                `✓ Size: ${shoppingSpec.size}\n` +
                `✓ Items: ${shoppingSpec.items.join(', ')}\n` +
                `✓ Preferences: ${shoppingSpec.preferences.warmth} warmth, waterproof\n\n` +
                `Let me search across multiple retailers for the best options...`
            );
            
            // Hide quick start
            document.getElementById('quick-start').style.display = 'none';
            
            setTimeout(() => {
                updateStage('discovery');
                discoverProducts();
            }, 1500);
        }
    } catch (error) {
        console.error('Error:', error);
        hideLoading();
        addMessage('agent', 'Sorry, I encountered an error. Please try again.');
    }
}

async function discoverProducts() {
    addMessage('agent', '🔍 Searching Amazon, REI, Backcountry, and Evo...');
    showLoading();
    
    try {
        const response = await fetch('/api/discover-products', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ spec: shoppingSpec })
        });
        
        const data = await response.json();
        allProducts = data.products;
        selectedCart = data.auto_cart;
        
        hideLoading();
        
        const totalItems = Object.values(allProducts).reduce((sum, cat) => sum + cat.length, 0);
        addMessage('agent', 
            `Found ${totalItems} products across ${Object.keys(retailers).length} retailers! ` +
            `I've ranked them based on your budget, delivery needs, and preferences. ` +
            `The top choices are already in your cart.`
        );
        
        updateStage('ranking');
        displayProducts();
    } catch (error) {
        console.error('Error:', error);
        hideLoading();
        addMessage('agent', 'Error discovering products. Please try again.');
    }
}

function displayProducts() {
    const section = document.getElementById('products-section');
    section.style.display = 'block';
    section.innerHTML = '';
    
    for (const [category, products] of Object.entries(allProducts)) {
        const categoryDiv = document.createElement('div');
        
        // Category title
        const title = document.createElement('h2');
        title.className = 'category-title';
        title.textContent = category.charAt(0).toUpperCase() + category.slice(1);
        categoryDiv.appendChild(title);
        
        // Explanation box
        const explanation = document.createElement('div');
        explanation.className = 'explanation-box';
        explanation.innerHTML = '<strong>Why this ranking?</strong><br/>' +
            'Scored on: Price fit (40%), Delivery speed (30%), Quality rating (25%), Preference match (25% bonus)';
        categoryDiv.appendChild(explanation);
        
        // Products grid
        const grid = document.createElement('div');
        grid.className = 'products-grid';
        
        products.forEach((product, index) => {
            const card = createProductCard(product, index + 1, category);
            grid.appendChild(card);
        });
        
        categoryDiv.appendChild(grid);
        section.appendChild(categoryDiv);
    }
    
    // Add action buttons
    const actions = document.createElement('div');
    actions.className = 'actions';
    actions.innerHTML = `
        <button class="btn btn-primary" onclick="viewCart()">
            View Cart (${Object.keys(selectedCart).length} items)
        </button>
    `;
    section.appendChild(actions);
}

function createProductCard(product, rank, category) {
    const card = document.createElement('div');
    card.className = 'product-card';
    
    if (selectedCart[category]?.id === product.id) {
        card.classList.add('selected');
    }
    
    card.onclick = () => toggleProduct(category, product);
    
    card.innerHTML = `
        <div class="product-rank">#${rank}</div>
        <div class="product-image">${product.emoji || '🛍️'}</div>
        <div class="product-name">${product.name}</div>
        <div class="product-retailer">${retailers[product.retailer].name}</div>
        <div class="product-price">$${product.price}</div>
        <div class="product-delivery">
            📦 Delivers in ${retailers[product.retailer].base_delivery} days
        </div>
        <div class="product-score">
            Score: ${product.score}/100<br/>
            <small>${product.reasoning}</small>
        </div>
    `;
    
    return card;
}

function toggleProduct(category, product) {
    if (selectedCart[category]?.id === product.id) {
        selectedCart[category] = null;
    } else {
        selectedCart[category] = product;
    }
    displayProducts();
}

function viewCart() {
    updateStage('cart');
    
    const section = document.getElementById('cart-section');
    section.style.display = 'block';
    section.innerHTML = '';
    
    const container = document.createElement('div');
    container.className = 'cart-container';
    
    // Calculate total
    const total = Object.values(selectedCart)
        .filter(p => p)
        .reduce((sum, p) => sum + p.price, 0);
    
    // Header
    container.innerHTML = `
        <div class="cart-header">
            <h2>Your Combined Cart</h2>
            <div class="cart-total">$${total}</div>
        </div>
    `;
    
    // Cart items
    for (const [category, product] of Object.entries(selectedCart)) {
        if (product) {
            const item = document.createElement('div');
            item.className = 'cart-item';
            item.innerHTML = `
                <div class="cart-item-info">
                    <div class="cart-item-name">${product.name}</div>
                    <div class="cart-item-retailer">
                        ${retailers[product.retailer].name} • Delivers in ${retailers[product.retailer].base_delivery} days
                    </div>
                </div>
                <div class="cart-item-price">$${product.price}</div>
                <button class="btn btn-secondary" onclick="backToProducts()">Change</button>
            `;
            container.appendChild(item);
        }
    }
    
    // Explanation
    const uniqueRetailers = [...new Set(Object.values(selectedCart).filter(p => p).map(p => p.retailer))];
    const explanation = document.createElement('div');
    explanation.className = 'explanation-box';
    explanation.style.marginTop = '2rem';
    explanation.innerHTML = `
        <strong>Multi-Retailer Checkout:</strong><br/>
        I'll handle checkout across ${uniqueRetailers.length} different retailers automatically.
        You'll enter payment & shipping once, and I'll complete all purchases.
    `;
    container.appendChild(explanation);
    
    // Actions
    const actions = document.createElement('div');
    actions.className = 'actions';
    actions.innerHTML = `
        <button class="btn btn-primary" onclick="proceedToCheckout()">Proceed to Checkout</button>
        <button class="btn btn-secondary" onclick="backToProducts()">Continue Shopping</button>
    `;
    container.appendChild(actions);
    
    section.appendChild(container);
    
    // Scroll to cart
    section.scrollIntoView({ behavior: 'smooth' });
}

function backToProducts() {
    updateStage('ranking');
    document.getElementById('cart-section').style.display = 'none';
    document.getElementById('products-section').scrollIntoView({ behavior: 'smooth' });
}

async function proceedToCheckout() {
    updateStage('checkout');
    addMessage('agent', '🚀 Starting checkout orchestration across multiple retailers...');
    
    const section = document.getElementById('checkout-section');
    section.style.display = 'block';
    section.innerHTML = '';
    
    const container = document.createElement('div');
    container.className = 'checkout-section';
    
    container.innerHTML = '<h2 style="margin-bottom: 2rem; font-size: 2rem">Checkout Orchestration</h2>';
    
    const explanation = document.createElement('div');
    explanation.className = 'explanation-box';
    explanation.innerHTML = `
        <strong>DEMO MODE:</strong> This is a simulated checkout. 
        In production, this would integrate with real payment processors and retailer APIs.
    `;
    container.appendChild(explanation);
    
    try {
        const response = await fetch('/api/checkout', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ cart: selectedCart })
        });
        
        const data = await response.json();
        const steps = data.steps;
        
        // Display steps
        const stepsContainer = document.createElement('div');
        stepsContainer.id = 'checkout-steps';
        container.appendChild(stepsContainer);
        
        section.appendChild(container);
        
        // Animate steps
        for (let i = 0; i < steps.length; i++) {
            await new Promise(resolve => setTimeout(resolve, 2000));
            await animateStep(steps[i], selectedCart);
        }
        
        // Success message
        await new Promise(resolve => setTimeout(resolve, 500));
        const total = Object.values(selectedCart).filter(p => p).reduce((sum, p) => sum + p.price, 0);
        const uniqueRetailers = [...new Set(Object.values(selectedCart).filter(p => p).map(p => p.retailer))];
        
        const success = document.createElement('div');
        success.style.cssText = `
            margin-top: 2rem;
            padding: 2rem;
            background: linear-gradient(135deg, rgba(16, 185, 129, 0.2), rgba(247, 184, 1, 0.2));
            border-radius: 15px;
            text-align: center;
        `;
        success.innerHTML = `
            <h2 style="font-size: 2.5rem; margin-bottom: 1rem">🎉 All Done!</h2>
            <p style="font-size: 1.2rem; margin-bottom: 1rem">
                Your ${Object.keys(selectedCart).length} items are on their way from ${uniqueRetailers.length} retailers.
            </p>
            <p style="color: var(--text-dim)">
                Total: $${total} • Expected delivery: 3-5 days
            </p>
        `;
        container.appendChild(success);
        
        addMessage('agent', '✅ Checkout complete! All orders confirmed. You\'ll receive tracking numbers via email within 24 hours.');
        
    } catch (error) {
        console.error('Error:', error);
    }
}

async function animateStep(step, cart) {
    const container = document.getElementById('checkout-steps');
    
    const stepDiv = document.createElement('div');
    stepDiv.className = 'checkout-step';
    stepDiv.id = `step-${step.id}`;
    
    let itemsHtml = '';
    if (step.retailer !== 'all' && step.items) {
        itemsHtml = `<p style="color: var(--text-dim); font-size: 0.9rem">
            Items: ${step.items.join(', ')}
        </p>`;
    }
    
    stepDiv.innerHTML = `
        <h3>
            ${step.title}
            <span class="status-badge pending">pending</span>
        </h3>
        ${itemsHtml}
    `;
    
    container.appendChild(stepDiv);
    
    // Processing
    await new Promise(resolve => setTimeout(resolve, 100));
    stepDiv.classList.add('processing');
    stepDiv.querySelector('.status-badge').className = 'status-badge processing';
    stepDiv.querySelector('.status-badge').textContent = 'processing';
    
    // Completed
    await new Promise(resolve => setTimeout(resolve, 1500));
    stepDiv.classList.remove('processing');
    stepDiv.classList.add('completed');
    stepDiv.querySelector('.status-badge').className = 'status-badge completed';
    stepDiv.querySelector('.status-badge').textContent = 'completed';
}
