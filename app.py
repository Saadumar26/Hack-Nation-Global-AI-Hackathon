from flask import Flask, render_template, request, jsonify
import json
from datetime import datetime, timedelta
import os
import re
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Configure Gemini API
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
USE_AI_PARSING = os.getenv('USE_AI_PARSING', 'false').lower() == 'true'

if GEMINI_API_KEY and USE_AI_PARSING:
    genai.configure(api_key=GEMINI_API_KEY)
    # Use fastest free model: gemini-2.0-flash-lite
    gemini_model = genai.GenerativeModel('gemini-2.0-flash-lite')
    print("✅ Gemini API Enabled - Using AI-powered parsing")
else:
    gemini_model = None
    print("ℹ️  Using regex-based parsing (no API key needed)")

# Mock retailer data
RETAILERS = {
    'amazon': {'name': 'Amazon', 'base_delivery': 2},
    'rei': {'name': 'REI', 'base_delivery': 3},
    'backcountry': {'name': 'Backcountry', 'base_delivery': 4},
    'evo': {'name': 'Evo', 'base_delivery': 3}
}

# Mock product database
PRODUCT_DATABASE = {
    'jacket': [
        {'id': 'j1', 'name': 'Arc\'teryx Rush Jacket', 'price': 189, 'retailer': 'rei', 'rating': 4.8, 'waterproof': True, 'warmth': 'high', 'emoji': '🧥'},
        {'id': 'j2', 'name': 'Patagonia Powder Bowl Jacket', 'price': 179, 'retailer': 'backcountry', 'rating': 4.7, 'waterproof': True, 'warmth': 'high', 'emoji': '🧥'},
        {'id': 'j3', 'name': 'North Face Freedom Insulated', 'price': 159, 'retailer': 'amazon', 'rating': 4.6, 'waterproof': True, 'warmth': 'medium', 'emoji': '🧥'},
        {'id': 'j4', 'name': 'Columbia Wildside Jacket', 'price': 129, 'retailer': 'evo', 'rating': 4.5, 'waterproof': True, 'warmth': 'medium', 'emoji': '🧥'}
    ],
    'pants': [
        {'id': 'p1', 'name': 'Arc\'teryx Sabre AR Pants', 'price': 149, 'retailer': 'rei', 'rating': 4.8, 'waterproof': True, 'warmth': 'high', 'emoji': '👖'},
        {'id': 'p2', 'name': 'Patagonia Snowshot Pants', 'price': 139, 'retailer': 'backcountry', 'rating': 4.7, 'waterproof': True, 'warmth': 'high', 'emoji': '👖'},
        {'id': 'p3', 'name': 'North Face Freedom Insulated Pants', 'price': 119, 'retailer': 'amazon', 'rating': 4.6, 'waterproof': True, 'warmth': 'medium', 'emoji': '👖'},
        {'id': 'p4', 'name': 'Burton Cargo Pants', 'price': 99, 'retailer': 'evo', 'rating': 4.5, 'waterproof': True, 'warmth': 'medium', 'emoji': '👖'}
    ],
    'gloves': [
        {'id': 'g1', 'name': 'Black Diamond Guide Gloves', 'price': 69, 'retailer': 'rei', 'rating': 4.7, 'waterproof': True, 'warmth': 'high', 'emoji': '🧤'},
        {'id': 'g2', 'name': 'Hestra Army Leather Heli Ski', 'price': 79, 'retailer': 'backcountry', 'rating': 4.9, 'waterproof': True, 'warmth': 'high', 'emoji': '🧤'},
        {'id': 'g3', 'name': 'The North Face Montana Gloves', 'price': 49, 'retailer': 'amazon', 'rating': 4.5, 'waterproof': True, 'warmth': 'medium', 'emoji': '🧤'},
        {'id': 'g4', 'name': 'Burton Gore-Tex Gloves', 'price': 59, 'retailer': 'evo', 'rating': 4.6, 'waterproof': True, 'warmth': 'medium', 'emoji': '🧤'}
    ],
    'goggles': [
        {'id': 'go1', 'name': 'Smith I/O Mag Goggles', 'price': 89, 'retailer': 'rei', 'rating': 4.8, 'features': ['interchangeable'], 'emoji': '🥽'},
        {'id': 'go2', 'name': 'Oakley Flight Deck Goggles', 'price': 99, 'retailer': 'backcountry', 'rating': 4.7, 'features': ['prizm'], 'emoji': '🥽'},
        {'id': 'go3', 'name': 'Anon M4 Goggles', 'price': 79, 'retailer': 'amazon', 'rating': 4.6, 'features': ['magnetic'], 'emoji': '🥽'},
        {'id': 'go4', 'name': 'Dragon NFX2 Goggles', 'price': 69, 'retailer': 'evo', 'rating': 4.5, 'features': ['frameless'], 'emoji': '🥽'}
    ],
    'helmet': [
        {'id': 'h1', 'name': 'Smith Vantage MIPS Helmet', 'price': 99, 'retailer': 'rei', 'rating': 4.8, 'safety': 'MIPS', 'emoji': '⛑️'},
        {'id': 'h2', 'name': 'Giro Range MIPS Helmet', 'price': 89, 'retailer': 'backcountry', 'rating': 4.7, 'safety': 'MIPS', 'emoji': '⛑️'},
        {'id': 'h3', 'name': 'POC Fornix Helmet', 'price': 79, 'retailer': 'amazon', 'rating': 4.6, 'safety': 'Standard', 'emoji': '⛑️'},
        {'id': 'h4', 'name': 'Anon Raider Helmet', 'price': 69, 'retailer': 'evo', 'rating': 4.5, 'safety': 'Standard', 'emoji': '⛑️'}
    ]
}


class ShoppingAgent:
    """AI Shopping Agent - Works with OR without Gemini API"""
    
    def __init__(self):
        self.spec = None
        self.products = []
        self.use_ai = gemini_model is not None
        
    def parse_brief_with_gemini(self, message):
        """
        AI-powered parsing using FREE Gemini API
        Uses gemini-2.0-flash-lite (fastest free model)
        """
        prompt = f"""You are a shopping assistant. Parse this shopping request into JSON.

User request: "{message}"

Extract the following information and return ONLY valid JSON (no markdown, no explanations):

{{
    "budget": <number or 400 if not specified>,
    "delivery_days": <number or 5 if not specified>,
    "size": "<size like M, L, XL or M if not specified>",
    "preferences": {{
        "warmth": "<high/medium/low or empty>",
        "waterproof": <true/false>,
        "brand": "<brand name or empty>",
        "color": "<color or empty>"
    }},
    "items": [<list of items like "jacket", "pants", "gloves", "goggles", "helmet">],
    "scenario": "<skiing/party/hackathon/custom>"
}}

Rules:
- If request mentions skiing/snow: include jacket, pants, gloves, goggles, helmet
- If request mentions party/game: include jacket, pants
- If request mentions hackathon: include jacket, pants
- Extract budget from phrases like "$400", "400 dollars", "budget 400"
- Extract delivery from "5 days", "within 3 days", "in 2 days"
- Extract size from "size M", "medium", "large"
- Detect warmth need from "warm", "cold weather", "insulated"
- Detect waterproof from "waterproof", "water resistant", "rain"

Return ONLY the JSON object, nothing else."""

        try:
            response = gemini_model.generate_content(prompt)
            
            # Clean response - remove markdown code blocks if present
            response_text = response.text.strip()
            if response_text.startswith('```'):
                # Remove ```json and ``` markers
                response_text = response_text.split('```')[1]
                if response_text.startswith('json'):
                    response_text = response_text[4:]
            
            spec = json.loads(response_text.strip())
            
            # Validate and set defaults
            spec.setdefault('budget', 400)
            spec.setdefault('delivery_days', 5)
            spec.setdefault('size', 'M')
            spec.setdefault('preferences', {})
            spec.setdefault('items', ['jacket', 'pants', 'gloves', 'goggles'])
            spec.setdefault('scenario', 'custom')
            
            return spec
            
        except Exception as e:
            print(f"Gemini parsing error: {e}")
            # Fallback to regex parsing
            return self.parse_brief_with_regex(message)
    
    def parse_brief_with_regex(self, message):
        """
        Regex-based parsing - NO API REQUIRED
        Fast and reliable for structured inputs
        """
        spec = {
            'budget': 400,
            'delivery_days': 5,
            'size': 'M',
            'preferences': {},
            'items': [],
            'scenario': 'custom'
        }
        
        message_lower = message.lower()
        
        # ====== SCENARIO DETECTION ======
        if 'ski' in message_lower or 'skiing' in message_lower or 'snow' in message_lower:
            spec['scenario'] = 'skiing'
            spec['items'] = ['jacket', 'pants', 'gloves', 'goggles', 'helmet']
            spec['preferences'] = {'warmth': 'high', 'waterproof': True}
        elif 'party' in message_lower or 'game' in message_lower or 'superbowl' in message_lower:
            spec['scenario'] = 'party'
            spec['items'] = ['jacket', 'pants']
            spec['budget'] = 150
        elif 'hackathon' in message_lower or 'event' in message_lower:
            spec['scenario'] = 'hackathon'
            spec['items'] = ['jacket', 'pants']
            spec['budget'] = 200
        
        # ====== BUDGET EXTRACTION ======
        budget_patterns = [
            r'\$\s*(\d+)',
            r'(\d+)\s*dollars?',
            r'budget\s*:?\s*\$?\s*(\d+)',
            r'\$?\s*(\d+)\s*budget'
        ]
        for pattern in budget_patterns:
            match = re.search(pattern, message_lower)
            if match:
                spec['budget'] = int(match.group(1))
                break
        
        # ====== DELIVERY DAYS ======
        delivery_patterns = [
            r'(\d+)\s*[-]?days?',
            r'within\s+(\d+)',
            r'in\s+(\d+)\s*days?',
            r'(\d+)\s*day\s+delivery'
        ]
        for pattern in delivery_patterns:
            match = re.search(pattern, message_lower)
            if match:
                spec['delivery_days'] = int(match.group(1))
                break
        
        # ====== SIZE EXTRACTION ======
        size_patterns = [
            r'size\s*:?\s*([A-Z]{1,3})',
            r'\b([XS|S|M|L|XL|XXL]{1,3})\b',
        ]
        for pattern in size_patterns:
            match = re.search(pattern, message, re.IGNORECASE)
            if match:
                spec['size'] = match.group(1).upper()
                break
        
        size_map = {
            'small': 'S', 'medium': 'M', 'large': 'L',
            'extra small': 'XS', 'extra large': 'XL'
        }
        for word, letter in size_map.items():
            if word in message_lower:
                spec['size'] = letter
                break
        
        # ====== PREFERENCES ======
        if any(word in message_lower for word in ['warm', 'hot', 'insulated', 'thermal', 'cold', 'frigid']):
            spec['preferences']['warmth'] = 'high'
        elif any(word in message_lower for word in ['moderate', 'medium', 'mild']):
            spec['preferences']['warmth'] = 'medium'
        
        if any(word in message_lower for word in ['waterproof', 'water-proof', 'water resistant', 'rain']):
            spec['preferences']['waterproof'] = True
        
        brands = ['arcteryx', 'arc\'teryx', 'patagonia', 'north face', 'columbia', 'burton']
        for brand in brands:
            if brand in message_lower:
                spec['preferences']['brand'] = brand.title()
                break
        
        colors = ['black', 'blue', 'red', 'green', 'white', 'gray', 'yellow']
        for color in colors:
            if color in message_lower:
                spec['preferences']['color'] = color
                break
        
        # ====== ITEM EXTRACTION ======
        if not spec['items']:
            item_keywords = {
                'jacket': ['jacket', 'coat', 'parka'],
                'pants': ['pants', 'trousers', 'bottoms'],
                'gloves': ['gloves', 'mittens'],
                'goggles': ['goggles', 'glasses', 'eyewear'],
                'helmet': ['helmet', 'headgear']
            }
            
            for item, keywords in item_keywords.items():
                if any(keyword in message_lower for keyword in keywords):
                    spec['items'].append(item)
        
        if not spec['items']:
            spec['items'] = ['jacket', 'pants', 'gloves', 'goggles']
        
        return spec
    
    def parse_brief(self, message):
        """
        Main parsing function - Uses AI if available, regex otherwise
        """
        if self.use_ai:
            print("🤖 Using Gemini AI for parsing...")
            spec = self.parse_brief_with_gemini(message)
        else:
            print("📝 Using regex-based parsing...")
            spec = self.parse_brief_with_regex(message)
        
        self.spec = spec
        return spec
    
    def rank_products(self, product_list, spec):
        """
        Transparent ranking algorithm - Pure Python
        NO AI NEEDED - Deterministic scoring
        """
        ranked_products = []
        
        for product in product_list:
            score = 0
            reasoning = []
            
            # PRICE SCORING (40 points)
            if product['price'] <= spec['budget']:
                price_ratio = product['price'] / spec['budget']
                price_score = (1 - price_ratio) * 40
                score += price_score
                reasoning.append(f"Price: ${product['price']} ({round(price_score)}pts)")
            else:
                reasoning.append(f"Price: ${product['price']} (OVER BUDGET, 0pts)")
            
            # DELIVERY SCORING (30 points)
            delivery_days = RETAILERS[product['retailer']]['base_delivery']
            if delivery_days <= spec['delivery_days']:
                time_ratio = delivery_days / spec['delivery_days']
                delivery_score = 30 * (1 - time_ratio * 0.5)
                score += delivery_score
                reasoning.append(f"Delivery: {delivery_days}d ({round(delivery_score)}pts)")
            else:
                score += 5
                reasoning.append(f"Delivery: {delivery_days}d (LATE, 5pts)")
            
            # QUALITY SCORING (25 points)
            quality_score = product['rating'] * 5
            score += quality_score
            reasoning.append(f"Rating: {product['rating']}⭐ ({round(quality_score)}pts)")
            
            # PREFERENCE BONUSES (25 points max)
            bonus_points = 0
            
            if spec['preferences'].get('warmth') and product.get('warmth') == spec['preferences']['warmth']:
                bonus_points += 15
                reasoning.append('Warmth match (+15pts)')
            
            if spec['preferences'].get('waterproof') and product.get('waterproof'):
                bonus_points += 10
                reasoning.append('Waterproof (+10pts)')
            
            if spec['preferences'].get('brand'):
                if spec['preferences']['brand'].lower() in product['name'].lower():
                    bonus_points += 10
                    reasoning.append(f"Brand match (+10pts)")
            
            score += bonus_points
            reasoning.append(f"Retailer: {RETAILERS[product['retailer']]['name']}")
            
            ranked_product = product.copy()
            ranked_product['score'] = round(score, 1)
            ranked_product['reasoning'] = ' | '.join(reasoning)
            ranked_product['delivery_days'] = delivery_days
            ranked_products.append(ranked_product)
        
        ranked_products.sort(key=lambda x: x['score'], reverse=True)
        return ranked_products
    
    def discover_products(self, spec):
        """Discover and rank products"""
        all_products = {}
        
        for item_type in spec['items']:
            if item_type in PRODUCT_DATABASE:
                ranked = self.rank_products(PRODUCT_DATABASE[item_type], spec)
                all_products[item_type] = ranked
        
        self.products = all_products
        return all_products
    
    def get_auto_selected_cart(self):
        """Get top-ranked products"""
        cart = {}
        for category, products in self.products.items():
            if products:
                cart[category] = products[0]
        return cart
    
    def optimize_cart_for_retailers(self, cart):
        """Analyze retailer distribution"""
        retailers_used = {}
        for category, product in cart.items():
            retailer = product['retailer']
            if retailer not in retailers_used:
                retailers_used[retailer] = []
            retailers_used[retailer].append(category)
        
        return {
            'num_retailers': len(retailers_used),
            'breakdown': retailers_used,
            'shipping_estimate': len(retailers_used) * 5
        }
    
    def calculate_total(self, cart):
        """Calculate cart total"""
        return sum(product['price'] for product in cart.values() if product)
    
    def get_budget_breakdown(self, cart, spec):
        """Budget analysis"""
        total = self.calculate_total(cart)
        return {
            'total': total,
            'budget': spec['budget'],
            'remaining': spec['budget'] - total,
            'percentage_used': round((total / spec['budget']) * 100, 1),
            'over_budget': total > spec['budget'],
            'by_category': {cat: prod['price'] for cat, prod in cart.items()}
        }
    
    def get_delivery_timeline(self, cart):
        """Calculate delivery dates"""
        timelines = {}
        latest_delivery = 0
        
        for category, product in cart.items():
            days = product.get('delivery_days', RETAILERS[product['retailer']]['base_delivery'])
            delivery_date = datetime.now() + timedelta(days=days)
            timelines[category] = {
                'days': days,
                'date': delivery_date.strftime('%B %d, %Y'),
                'retailer': RETAILERS[product['retailer']]['name']
            }
            latest_delivery = max(latest_delivery, days)
        
        return {
            'by_item': timelines,
            'latest_delivery_days': latest_delivery,
            'latest_delivery_date': (datetime.now() + timedelta(days=latest_delivery)).strftime('%B %d, %Y'),
            'meets_deadline': latest_delivery <= self.spec['delivery_days']
        }
    
    def simulate_checkout(self, cart):
        """Simulate checkout flow"""
        retailers = list(set(product['retailer'] for product in cart.values()))
        
        steps = [
            {'id': 1, 'title': 'Collecting Payment Information', 'status': 'pending', 'retailer': 'all'},
            {'id': 2, 'title': 'Collecting Shipping Address', 'status': 'pending', 'retailer': 'all'},
        ]
        
        for idx, retailer in enumerate(retailers):
            steps.append({
                'id': idx + 3,
                'title': f"Processing {RETAILERS[retailer]['name']} Order",
                'status': 'pending',
                'retailer': retailer,
                'items': [p['name'] for p in cart.values() if p['retailer'] == retailer]
            })
        
        steps.append({
            'id': len(retailers) + 3,
            'title': 'Confirming All Orders',
            'status': 'pending',
            'retailer': 'all'
        })
        
        return steps


# Initialize agent
agent = ShoppingAgent()


@app.route('/')
def index():
    """Main page"""
    return render_template('index.html')


@app.route('/api/parse-brief', methods=['POST'])
def parse_brief():
    """Parse shopping request - AI or Regex"""
    try:
        data = request.json
        message = data.get('message', '')
        
        if not message:
            return jsonify({'error': 'No message provided'}), 400
        
        spec = agent.parse_brief(message)
        spec['parsing_method'] = 'gemini_ai' if agent.use_ai else 'regex'
        
        return jsonify(spec)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/discover-products', methods=['POST'])
def discover_products():
    """Discover and rank products"""
    try:
        data = request.json
        spec = data.get('spec')
        
        if not spec:
            return jsonify({'error': 'No specification provided'}), 400
        
        products = agent.discover_products(spec)
        cart = agent.get_auto_selected_cart()
        total = agent.calculate_total(cart)
        budget_info = agent.get_budget_breakdown(cart, spec)
        delivery_info = agent.get_delivery_timeline(cart)
        retailer_info = agent.optimize_cart_for_retailers(cart)
        
        return jsonify({
            'products': products,
            'auto_cart': cart,
            'total': total,
            'budget_breakdown': budget_info,
            'delivery_timeline': delivery_info,
            'retailer_optimization': retailer_info
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/checkout', methods=['POST'])
def checkout():
    """Checkout simulation"""
    try:
        data = request.json
        cart = data.get('cart', {})
        
        if not cart:
            return jsonify({'error': 'Empty cart'}), 400
        
        steps = agent.simulate_checkout(cart)
        return jsonify({'steps': steps})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/retailers')
def get_retailers():
    """Retailer info"""
    return jsonify(RETAILERS)


@app.route('/api/health')
def health_check():
    """Health check"""
    return jsonify({
        'status': 'healthy',
        'ai_parsing': agent.use_ai,
        'parsing_method': 'gemini_ai' if agent.use_ai else 'regex',
        'model': 'gemini-2.0-flash-lite' if agent.use_ai else 'N/A',
        'message': 'Agentic Commerce running!'
    })


if __name__ == '__main__':
    print("🚀 Agentic Commerce Server Starting...")
    print("📱 Visit: http://localhost:5000")
    print("🛍️  Ready for AI-powered shopping!")
    if agent.use_ai:
        print("🤖 Gemini AI Parsing: ENABLED (Free!)")
    else:
        print("📝 Regex Parsing: ENABLED (No API needed)")
    app.run(debug=True, host='0.0.0.0', port=5000)
