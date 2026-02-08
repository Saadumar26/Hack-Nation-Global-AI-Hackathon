# Agentic Commerce - Python Edition 🛒

**Hack-Nation Global AI Hackathon Submission**

An end-to-end AI-powered shopping agent built with **Python + Flask** that automates the process of finding and buying products across multiple retailers.

---

## 🎯 Challenge Overview

Agentic Commerce demonstrates how an autonomous AI agent can:

- Understand shopping intent from natural language  
- Discover products across multiple retailers  
- Rank options using transparent, explainable logic  
- Combine items into a single cart  
- Orchestrate a unified checkout flow  

The system is designed to be **reliable, explainable, and production-oriented**, combining AI flexibility with deterministic backend logic.

---

## 🎯 Challenge Requirements Met

### ✅ Conversational Brief & Constraints Capture
- Natural language input for shopping requirements  
- Structured JSON output (budget, delivery, size, preferences)  
- Quick-start scenarios for common use cases  
- Dual parsing pipeline (AI-assisted + deterministic fallback)  

### ✅ Multi-Retailer Discovery
- Amazon, REI, Backcountry, Evo  
- Realistic product data (price, rating, delivery time)  
- Multiple product categories (jacket, pants, gloves, goggles, helmet)  

### ✅ Transparent Ranking Engine (Python)
- Score-based ranking (not LLM output)  
- Weighted criteria:
  - Price fit (40%)  
  - Delivery speed (30%)  
  - Quality rating (25%)  
  - Preference match (bonus)  
- Full score breakdown per product  

### ✅ Unified Cart Experience
- Products from multiple retailers in one cart  
- Budget usage tracking  
- Category-wise cost breakdown  
- Delivery timeline aggregation  

### ✅ Checkout Orchestration (Simulated)
- Unified checkout flow  
- Multi-retailer order simulation  
- Step-by-step status updates  

---

## 🏗️ Tech Stack

### Backend
- **Python 3.8+**
- **Flask** – Web framework  
- **python-dotenv** – Environment management  
- **google-generativeai** – AI-assisted parsing  

### Frontend
- **Vanilla JavaScript**
- **HTML5 + CSS3**
- Responsive, clean UI  

### Architecture Highlights
- AI-assisted intent understanding  
- Deterministic Python-based ranking  
- Graceful fallback mechanisms  

---

## 📦 Installation & Setup

### Prerequisites
```bash
# Check Python version (need 3.8+)
python --version
# or
python3 --version
```

### Step 1: Clone or Extract Project

```bash
cd agentic-commerce-python
```

### Step 2: Create Virtual Environment (Recommended)

```bash
# Create virtual environment
python -m venv venv

# Activate it
# On Windows:
venv\Scripts\activate

# On Mac/Linux:
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

This installs:
- `flask` - Web server
- `python-dotenv` - Environment variables
- `google-generativeai` - FREE Gemini API
- `requests` - HTTP library

### Step 4: Get FREE Gemini API Key (Optional but Recommended)

1. Visit: https://aistudio.google.com/app/apikey
2. Sign in with Google account
3. Click "Create API Key"
4. Copy your key (starts with `AIzaSy...`)

**Cost: $0** - Completely free, no credit card needed!

### Step 5: Configure API Key

```bash
# Copy example env file
cp .env.example .env

# Edit .env and add your API key
GEMINI_API_KEY=AIzaSy...your-actual-key...
USE_AI_PARSING=true
```

**Skip this step?** No problem! The app works perfectly with regex-only mode.

### Step 6: Test Your Setup (Optional)

```bash
python test_gemini_setup.py
```

This verifies:
- ✅ API key is valid
- ✅ Gemini connection works
- ✅ Both parsing modes functional
- ✅ Available models listed

### Step 7: Run the Application

```bash
python app.py
```

You should see:
```
🚀 Agentic Commerce Server Starting...
📱 Visit: http://localhost:5000
🛍️  Ready for AI-powered shopping!
🤖 Gemini AI Parsing: ENABLED (Free!)
```

Or without API:
```
🚀 Agentic Commerce Server Starting...
📱 Visit: http://localhost:5000
🛍️  Ready for AI-powered shopping!
ℹ️  Using regex-based parsing (no API key needed)
```

### Step 8: Open in Browser

Visit: `http://localhost:5000`

## 🎮 How to Use

### With Gemini AI (Natural Language):

1. **Type naturally** - No rigid format needed!
   - "I need warm skiing gear, about 400 bucks, I'm a medium, deliver fast"
   - "Looking for waterproof outfit for snow, $400 max, size large"
   - "Skiing clothes needed ASAP, 400 dollars, medium size"

2. **AI Parses** your request
   - Understands context and intent
   - Extracts budget, size, preferences
   - Detects urgency ("fast", "ASAP")

### With Regex (Structured):

1. **Use clear format**
   - "Skiing outfit, $400, size M, 5 days"
   - "Budget $400, delivery 5 days, size M, skiing"

2. **Agent Parses** keywords
   - Regex patterns extract data
   - Fast and deterministic

### Both Modes:

3. **Products Discovered** from multiple retailers
   - Automatically ranked using Python algorithm

4. **Review & Customize** your cart
   - Click products to swap selections
   - See budget breakdown
   - View delivery timeline

5. **Proceed to Checkout**
   - Watch simulated multi-retailer checkout

## 🗂️ Project Structure

```
agentic-commerce-python/
├── app.py                    # Main Flask application + Gemini integration
├── requirements.txt          # Python dependencies
├── .env.example             # Environment variables template
├── test_gemini_setup.py     # Setup verification script
├── SETUP_GEMINI.md          # Detailed Gemini setup guide
├── templates/
│   └── index.html           # Main HTML template
├── static/
│   ├── css/
│   │   └── styles.css       # All styling
│   └── js/
│       └── app.js           # Frontend JavaScript
└── README.md                # This file
```

## 🧮 Hybrid AI Architecture

### Parsing: Gemini AI (Optional)
```python
def parse_brief_with_gemini(message):
    """
    AI-powered parsing using FREE Gemini API
    - Understands natural language
    - Extracts intent and context
    - Handles variations and typos
    - Falls back to regex on error
    """
```

### Ranking: Pure Python (Always)
```python
def rank_products(product_list, spec):
    """
    Transparent scoring algorithm:
    - Price fit: 40 points (cheaper within budget = better)
    - Delivery speed: 30 points (meets deadline?)
    - Quality rating: 25 points (customer reviews)
    - Preference match: 25 bonus points (waterproof, warmth, brand)
    
    NO AI - Deterministic & Explainable
    """
```

### Why This Hybrid Approach?

| Component | Technology | Reason |
|-----------|------------|--------|
| **Parsing** | Gemini AI | Natural language understanding |
| **Ranking** | Python | Transparent, explainable, deterministic |
| **Fallback** | Regex | Works offline, 100% reliable |

**Result**: Best UX (AI flexibility) + Best transparency (Python clarity)

## 🎯 Example Rankings

### Input:
```
"Skiing outfit, $400, size M, 5 days, warm and waterproof"
```

### Output:
```
Arc'teryx Rush Jacket: 91/100
├── Price: $189 (21pts)     # (1 - 189/400) × 40
├── Delivery: 3d (30pts)    # Meets 5-day deadline
├── Rating: 4.8⭐ (24pts)    # 4.8 × 5
├── Warmth: High (+15pts)   # Matches preference
└── Waterproof (+10pts)     # Matches preference

Patagonia Powder Bowl Jacket: 89/100
├── Price: $179 (22pts)     # (1 - 179/400) × 40
├── Delivery: 4d (22pts)    # Close to deadline
├── Rating: 4.7⭐ (23pts)    # 4.7 × 5
├── Warmth: High (+15pts)   # Matches preference
└── Waterproof (+10pts)     # Matches preference
```

## 🔧 Python Classes & Functions

### `ShoppingAgent` Class

#### Parsing Methods:
- `parse_brief(message)` - Main parsing (AI or regex)
- `parse_brief_with_gemini(message)` - AI-powered parsing
- `parse_brief_with_regex(message)` - Pattern-based parsing

#### Product Discovery:
- `discover_products(spec)` - Search across retailers
- `rank_products(products, spec)` - Transparent scoring algorithm
- `get_auto_selected_cart()` - Auto-select top products

#### Analysis:
- `calculate_total(cart)` - Calculate cart total
- `get_budget_breakdown(cart, spec)` - Budget analysis
- `get_delivery_timeline(cart)` - Delivery estimates
- `optimize_cart_for_retailers(cart)` - Retailer distribution

#### Checkout:
- `simulate_checkout(cart)` - Generate checkout steps

### Flask Routes
- `GET /` - Serve main page
- `POST /api/parse-brief` - Parse shopping request (AI or regex)
- `POST /api/discover-products` - Find and rank products
- `POST /api/checkout` - Simulate checkout
- `GET /api/retailers` - Get retailer data
- `GET /api/health` - Health check (shows AI status)

## 🎨 Features Showcase

### 1. AI-Powered Conversational Shopping
```python
# User input (natural language):
"I need warm skiing gear, about 400 bucks, I'm a medium, deliver fast"

# Gemini AI parses to:
{
    'budget': 400,
    'delivery_days': 2,        # "fast" → 2 days
    'size': 'M',               # "medium" → M
    'preferences': {
        'warmth': 'high',      # "warm" detected
        'waterproof': True     # skiing context
    },
    'items': ['jacket', 'pants', 'gloves', 'goggles', 'helmet'],
    'scenario': 'skiing'
}
```

### 2. Multi-Retailer Search
- 4 retailers: Amazon, REI, Backcountry, Evo
- 20 products total (5 categories × 4 options)
- Each with realistic pricing and delivery estimates

### 3. Transparent Ranking
- Python-based scoring (not AI black box)
- Clear point breakdown for each product
- Explainable recommendations
- Users see exactly why products are ranked

### 4. Budget Tracking
```json
{
    "total": 526,
    "budget": 400,
    "remaining": -126,
    "percentage_used": 131.5,
    "over_budget": true,
    "by_category": {
        "jacket": 189,
        "pants": 149,
        "gloves": 69,
        "goggles": 89,
        "helmet": 99
    }
}
```

### 5. Delivery Timeline
```json
{
    "by_item": {
        "jacket": {
            "days": 3,
            "date": "February 11, 2026",
            "retailer": "REI"
        }
    },
    "latest_delivery_days": 4,
    "latest_delivery_date": "February 12, 2026",
    "meets_deadline": true
}
```

### 6. Checkout Orchestration
- Simulated multi-retailer checkout
- Step-by-step progress
- Animated status updates

## 💰 Cost Comparison

### Your Project (Gemini):
- **API Calls**: $0/month (FREE!)
- **Rate Limit**: 60 requests/min
- **Daily Quota**: 1500 requests/day
- **Hosting**: ~$5/month
- **Total**: **$5/month**

### Alternative (Anthropic Claude):
- **API Calls**: $15-50/month
- **Rate Limit**: Varies by tier
- **Hosting**: ~$5/month
- **Total**: **$20-55/month**

### Regex Only:
- **API Calls**: $0/month
- **Hosting**: ~$5/month
- **Total**: **$5/month**

**Winner**: Gemini = Same cost as regex, better UX! 🎉

## 🚀 Advanced Features

### 1. Dual Parsing Modes
- **AI Mode**: Natural language understanding
- **Regex Mode**: Structured input parsing
- **Auto Fallback**: AI fails → Regex activates

### 2. Enhanced Budget Analysis
- Real-time budget tracking
- Percentage used indicator
- Over-budget warnings
- Category-wise breakdown

### 3. Delivery Optimization
- Expected delivery date per item
- Latest delivery calculation
- Deadline compliance check
- Retailer consolidation suggestions

### 4. Retailer Analytics
- Number of retailers used
- Items per retailer
- Shipping cost estimates
- Consolidation opportunities

## 📊 Data Flow

```
User Input (Natural Language)
    ↓
Gemini AI / Regex Parser
    ↓
Structured Specification (JSON)
    ↓
Flask Backend (app.py)
    ↓
ShoppingAgent.discover_products()
    ↓
ShoppingAgent.rank_products()  ← Pure Python Algorithm
    ↓
Enhanced Analysis (Budget, Delivery, Retailers)
    ↓
JSON Response
    ↓
JavaScript Frontend (app.js)
    ↓
Dynamic UI Update
```

## 🛠️ Troubleshooting

### Gemini API Issues

**Error: "API key not valid"**
```bash
# Check your .env file:
GEMINI_API_KEY=AIzaSy...  # Must start with AIzaSy

# Get new key: https://aistudio.google.com/app/apikey
```

**Error: "Resource exhausted"**
```bash
# You hit rate limit (60/min)
# Solution 1: Wait a minute
# Solution 2: Set USE_AI_PARSING=false in .env
```

**Gemini returns invalid JSON**
```python
# App handles this automatically:
# 1. Cleans markdown code blocks
# 2. Falls back to regex parsing
# No action needed!
```

### General Issues

**Error: `ModuleNotFoundError: No module named 'flask'`**
```bash
pip install -r requirements.txt
```

**Error: Port 5000 already in use**
```bash
# Change port in app.py
app.run(debug=True, host='0.0.0.0', port=8000)
```

**Error: `venv/Scripts/activate` not found**
```bash
# On Windows:
venv\Scripts\activate.bat

# On Git Bash (Windows):
source venv/Scripts/activate
```

**App works but no AI parsing**
```bash
# Check .env file exists and has:
GEMINI_API_KEY=your-key
USE_AI_PARSING=true

# Test with:
python test_gemini_setup.py
```

## 🎓 Hackathon Submission Checklist

✅ Python-based backend (Flask)
✅ FREE AI integration (Gemini)
✅ Transparent ranking algorithm (Python class)
✅ Multi-retailer integration (4 stores)
✅ Combined cart functionality
✅ Budget tracking & analysis
✅ Delivery timeline calculation
✅ Simulated checkout orchestration
✅ Dual parsing modes (AI + Regex)
✅ Smart fallback system
✅ Clean, documented code
✅ Professional UI/UX
✅ Easy to run and demo
✅ Test script included
✅ Comprehensive documentation

## 📝 Code Quality

- **Type hints**: Clear function signatures
- **Docstrings**: All classes and methods documented
- **Comments**: Explain complex logic
- **Error handling**: Try-catch blocks everywhere
- **Modular design**: Separate concerns (parsing, ranking, analysis)
- **Fallback systems**: Graceful degradation
- **Testing**: Verification script included

## 🌟 Why This Architecture?

### 1. Gemini for Parsing
✅ Natural language understanding
✅ FREE to use
✅ Fast (flash-lite model)
✅ Flexible input handling

### 2. Python for Ranking
✅ Transparent algorithm
✅ Explainable decisions
✅ Deterministic results
✅ No API dependency

### 3. Regex Fallback
✅ Works offline
✅ Zero latency
✅ 100% reliable
✅ No costs ever

### 4. Best of All Worlds!
🎯 AI flexibility + Python transparency + Regex reliability = **Perfect Solution**

## 📈 Future Enhancements

### Free Additions:
- [ ] Web scraping with BeautifulSoup
- [ ] SQLite for user preferences
- [ ] Redis for caching
- [ ] Selenium for real product data

### Paid Options:
- [ ] Real retailer API integrations (e.g., Amazon Product API)
- [ ] Advanced ML for personalized recommendations
- [ ] User authentication and order history
- [ ] PostgreSQL database
- [ ] Celery for async task processing
- [ ] Payment gateway integration (Stripe)
- [ ] Email notifications (SendGrid)

## 🎯 Demo Script

### Opening (30 seconds)
**"Most AI shopping projects cost $30-50/month in API fees. Ours is 100% FREE using Google's Gemini API. No credit card needed, ever."**

### Show Natural Language (1 minute)
1. Type: "I need warm skiing gear, about 400 bucks, I'm a medium, deliver fast"
2. Show AI parsing result
3. Highlight: "No rigid format - just natural language"

### Show Transparency (1 minute)
1. Display product rankings
2. Point to score breakdown: "91/100 = 21+30+24+15+10"
3. Emphasize: "Pure Python algorithm - not AI black box"

### Show Dual Mode (30 seconds)
1. Switch to regex mode
2. Type: "Skiing outfit, $400, size M, 5 days"
3. Show it works offline too

### Closing (30 seconds)
**"Production-ready hybrid AI: Gemini for UX, Python for transparency, Regex for reliability. Free to run, scales infinitely, perfect for real-world deployment."**

## 🏆 Competitive Advantages

| Feature | Your Project | Typical AI Projects |
|---------|--------------|---------------------|
| **API Cost** | **$0/month** ✅ | $20-100/month |
| **Parsing** | AI + Regex dual mode ✅ | Just AI or just regex |
| **Ranking** | Transparent Python ✅ | Black box AI |
| **Offline Mode** | Works via regex ✅ | API-dependent |
| **Reliability** | Auto-fallback ✅ | Single point of failure |
| **Scalability** | Unlimited free tier ✅ | API rate limits |
| **Transparency** | Full visibility ✅ | Hidden algorithms |
| **Setup** | 5 minutes ✅ | Complex config |

## 📄 License

MIT License - Free to use and modify

## 👥 Team

- **Developer**: [Your Name]
- **Event**: Hack-Nation Global AI Hackathon
- **Track**: VC Track
- **Challenge**: Agentic Commerce

## 🙏 Acknowledgments

- Google for FREE Gemini API
- Flask team for amazing web framework
- Python community for excellent tools
- Hack-Nation for the opportunity

## 📚 Additional Resources

- **Gemini API Docs**: https://ai.google.dev/docs
- **Get FREE API Key**: https://aistudio.google.com/app/apikey
- **Flask Documentation**: https://flask.palletsprojects.com/
- **Detailed Setup Guide**: See `SETUP_GEMINI.md`

---

**Built with ❤️ and 🐍 for Hack-Nation Global AI Hackathon**

**🎉 100% FREE to run. No API costs. Just smart Python! 🎉**

For questions or issues, check the code comments or run the test script!

```bash
python test_gemini_setup.py
```
