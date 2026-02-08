# Agentic Commerce - Python Edition 🛒

![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-2.3+-green?logo=flask)
![Google AI](https://img.shields.io/badge/Google_AI-Gemini-orange?logo=google)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Hackathon](https://img.shields.io/badge/Hackathon-Hack--Nation_Global-red)
![Status](https://img.shields.io/badge/Status-Active-success)

**Hack-Nation Global AI Hackathon Submission | VC Track**

---

## 📋 Table of Contents

- [Overview](#overview)
- [Challenge Requirements](#challenge-requirements)
- [Tech Stack](#tech-stack)
- [Installation & Setup](#installation--setup)
- [How It Works](#how-it-works)
- [Hybrid Intelligence Design](#hybrid-intelligence-design)
- [Ranking Algorithm](#ranking-algorithm)
- [Project Structure](#project-structure)
- [API Endpoints](#api-endpoints)
- [Key Features](#key-features)
- [Future Enhancements](#future-enhancements)
- [Team Information](#team-information)
- [License](#license)

---

## 🎯 Overview

**Agentic Commerce** is an end-to-end AI-powered shopping agent built with **Python + Flask** that automates the process of finding and purchasing products across multiple retailers.

### Core Capabilities

This AI agent automatically:

- Understands shopping intent from natural language
- Discovers products across multiple retailers
- Ranks options using transparent, explainable logic
- Combines items into a single cart
- Orchestrates a unified checkout flow

### Design Philosophy

The system is designed to be **reliable, explainable, and production-oriented**, combining AI flexibility with deterministic backend logic.

---

## ✅ Challenge Requirements

### 1. Conversational Brief & Constraints Capture

**Implemented Features:**
- Natural language input for shopping requirements
- Structured JSON output generation
  - Budget constraints
  - Delivery preferences
  - Size requirements
  - User preferences
- Quick-start scenarios for common use cases
- Dual parsing pipeline:
  - AI-assisted understanding
  - Deterministic fallback mechanism

### 2. Multi-Retailer Discovery

**Supported Retailers:**
- Amazon
- REI
- Backcountry
- Evo

**Product Categories:**
- Jackets
- Pants
- Gloves
- Goggles
- Helmets

**Product Data Includes:**
- Realistic pricing
- Customer ratings
- Delivery time estimates

### 3. Transparent Ranking Engine

**Python-Based Scoring System:**

**Weighted Criteria:**
- **Price Fit:** 40% weightage
- **Delivery Speed:** 30% weightage
- **Quality Rating:** 25% weightage
- **Preference Match:** Bonus points

**Key Features:**
- Score-based ranking (not LLM-generated)
- Full score breakdown per product
- Explainable decision-making
- No black-box AI decisions

### 4. Unified Cart Experience

**Features:**
- Single cart for products from multiple retailers
- Real-time budget usage tracking
- Category-wise cost breakdown
- Delivery timeline aggregation
- Visual budget utilization display

### 5. Checkout Orchestration

**Simulated Checkout Flow:**
- Unified checkout interface
- Multi-retailer order simulation
- Step-by-step status updates
- Order confirmation tracking

---

## 🏗️ Tech Stack

### Backend Technologies

| Technology | Version | Purpose |
|------------|---------|---------|
| **Python** | 3.8+ | Core backend language |
| **Flask** | Latest | Web framework |
| **python-dotenv** | Latest | Environment variable management |
| **google-generativeai** | Latest | AI-assisted parsing |

### Frontend Technologies

| Technology | Purpose |
|------------|---------|
| **Vanilla JavaScript** | Frontend interactivity |
| **HTML5** | Structure |
| **CSS3** | Styling |

### Architecture Highlights

- **AI-Assisted Intent Understanding:** Natural language processing for user input
- **Deterministic Python Ranking:** Transparent scoring algorithm
- **Graceful Fallback Mechanisms:** Robust error handling
- **Modular Design:** Easy to extend and maintain

---

## 📦 Installation & Setup

### Prerequisites

You must have Python 3.8 or higher installed on your system:

```bash
python --version
```

### Step-by-Step Setup

**1. Clone the Repository**

```bash
git clone <repository-url>
cd agentic-commerce-python
```

**2. Create Virtual Environment**

```bash
# Linux/Mac
python -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

**3. Install Dependencies**

```bash
pip install -r requirements.txt
```

**4. Configure Environment Variables**

Create a `.env` file in the root directory:

```bash
GEMINI_API_KEY=your_api_key_here
FLASK_ENV=development
```

**5. Run the Application**

```bash
python app.py
```

**6. Access the Application**

Open your browser and visit:
```
http://localhost:5000
```

---

## 🎮 How It Works

### Step 1: Conversational Input

User apni needs natural language mein describe karta hai:

**Example:**
```
"I need warm skiing gear, budget 400, medium size, deliver fast"
```

### Step 2: Structured Specification

The system automatically extracts:

| Field | Description | Example |
|-------|-------------|---------|
| **Budget** | Maximum spending limit | $400 |
| **Delivery** | Time constraints | Fast (2-3 days) |
| **Size** | Product size | Medium |
| **Preferences** | Special requirements | Warmth, waterproofing |
| **Required Items** | Product categories | Jacket, pants, gloves |

### Step 3: Product Discovery

**Discovery Process:**
1. Query multiple retailers simultaneously
2. Gather candidate products across categories
3. Collect product metadata:
   - Price information
   - Availability status
   - Rating and reviews
   - Delivery estimates

### Step 4: Transparent Ranking

**Ranking Criteria:**

Each product is scored using a **pure Python algorithm**:

```python
Total Score = (Price Score × 0.40) + 
              (Delivery Score × 0.30) + 
              (Rating Score × 0.25) + 
              (Preference Bonus)
```

**Score Breakdown Example:**
```
Arc'teryx Rush Jacket — 91/100
├─ Price fit: 21/25
├─ Delivery: 30/30
├─ Rating: 24/25
└─ Preference match: 16/20
```

### Step 5: Unified Cart & Checkout

**Cart Features:**
- Best-ranked products automatically selected
- Budget validation in real-time
- Delivery timeline verification
- Multi-retailer checkout simulation

**Checkout Flow:**
1. Review selected products
2. Confirm budget allocation
3. Process multi-retailer orders
4. Track order status

---

## 🧮 Hybrid Intelligence Design

### AI vs Deterministic Logic

| Layer | Technology | Purpose |
|-------|------------|---------|
| **Parsing** | AI-Assisted | Natural language understanding |
| **Fallback** | Deterministic | Robust constraint extraction |
| **Ranking** | Pure Python | Transparent decision-making |
| **Scoring** | Algorithmic | Explainable product evaluation |

### Parsing Layer Architecture

**AI-Assisted Parsing:**
```python
def parse_with_ai(user_input):
    """
    Uses Google Gemini to understand:
    - Shopping intent
    - Budget constraints
    - Delivery preferences
    - Product requirements
    """
    # Returns structured JSON
```

**Deterministic Fallback:**
```python
def fallback_parser(user_input):
    """
    Regex-based extraction for:
    - Budget amounts ($XXX, XXX dollars)
    - Size keywords (small, medium, large)
    - Delivery terms (fast, urgent, quick)
    - Product categories (jacket, pants, etc.)
    """
    # Returns structured specification
```

### Decision Layer Algorithm

```python
def rank_products(products, specification):
    """
    Deterministic scoring algorithm:
    
    1. Price Fit Score (40 points)
       - Calculate price deviation from budget
       - Penalize overpriced items
       - Reward value options
    
    2. Delivery Feasibility (30 points)
       - Check delivery timeframe
       - Prioritize faster shipping
       - Consider user urgency
    
    3. Product Quality (25 points)
       - Normalize ratings (0-5 scale)
       - Consider review count
       - Factor in brand reputation
    
    4. Preference Alignment (bonus points)
       - Match user requirements
       - Technical specifications
       - Feature matching
    
    Returns: Sorted list with score breakdown
    """
```

### Key Design Principle

> **"AI is used for understanding intent, not for making opaque decisions."**

**Benefits:**
- Full transparency in product ranking
- Reproducible results
- Easy to debug and improve
- User trust through explainability

---

## 📊 Ranking Algorithm Details

### Score Components

#### 1. Price Fit Score (40 points max)

```python
def calculate_price_score(price, budget, max_score=40):
    """
    Perfect score for prices ≤ 80% of budget
    Linear penalty above that
    Zero score if > budget
    """
    if price > budget:
        return 0
    
    ratio = price / budget
    if ratio <= 0.8:
        return max_score
    else:
        # Linear decrease from 0.8 to 1.0
        return max_score * (1 - (ratio - 0.8) / 0.2)
```

**Example:**
- Budget: $100
- Product at $70 → 40/40 points (excellent value)
- Product at $90 → 20/40 points (acceptable)
- Product at $110 → 0/40 points (over budget)

#### 2. Delivery Score (30 points max)

```python
def calculate_delivery_score(delivery_days, urgency, max_score=30):
    """
    Faster delivery = higher score
    Scales based on user urgency
    """
    if urgency == "fast":
        if delivery_days <= 2:
            return max_score
        elif delivery_days <= 5:
            return max_score * 0.6
        else:
            return max_score * 0.3
    
    # Similar logic for normal/slow urgency
```

**Example:**
- Urgency: Fast, Delivery: 2 days → 30/30 points
- Urgency: Normal, Delivery: 5 days → 25/30 points
- Urgency: Fast, Delivery: 7 days → 9/30 points

#### 3. Rating Score (25 points max)

```python
def calculate_rating_score(rating, review_count, max_score=25):
    """
    Normalizes ratings to 0-25 scale
    Considers review count for reliability
    """
    base_score = (rating / 5.0) * max_score
    
    # Confidence adjustment based on reviews
    if review_count < 10:
        confidence = 0.7
    elif review_count < 50:
        confidence = 0.85
    else:
        confidence = 1.0
    
    return base_score * confidence
```

**Example:**
- 4.5★ with 200 reviews → 22.5/25 points
- 4.8★ with 5 reviews → 16.8/25 points
- 3.5★ with 100 reviews → 17.5/25 points

#### 4. Preference Bonus (0-20 points)

```python
def calculate_preference_bonus(product, preferences, max_bonus=20):
    """
    Matches product features to user preferences
    Each match adds points
    """
    bonus = 0
    for pref in preferences:
        if pref.lower() in product['description'].lower():
            bonus += max_bonus / len(preferences)
    
    return min(bonus, max_bonus)
```

**Example:**
- Preferences: ["warm", "waterproof"]
- Product mentions both → 20/20 bonus
- Product mentions one → 10/20 bonus
- Product mentions neither → 0/20 bonus

### Complete Ranking Example

```
Product: Arc'teryx Rush Jacket
────────────────────────────────────
Price: $380 (Budget: $400)
Delivery: 2 days (Requirement: Fast)
Rating: 4.8★ (250 reviews)
Matches: Warm, Waterproof

Score Breakdown:
├─ Price Fit:    38/40  (95% of budget)
├─ Delivery:     30/30  (Fast delivery)
├─ Rating:       24/25  (Excellent reviews)
└─ Preferences:  20/20  (All matches)
────────────────────────────────────
TOTAL SCORE:    112/115 = 97%
RANK: #1
```

---

## 🗂️ Project Structure

```
agentic-commerce-python/
│
├── app.py                      # Main Flask application
├── requirements.txt            # Python dependencies
├── test_gemini_setup.py        # API setup verification
├── .env                        # Environment variables
├── README.md                   # Project documentation
│
├── templates/
│   └── index.html             # Main HTML template
│
├── static/
│   ├── css/
│   │   └── styles.css         # Application styling
│   │
│   └── js/
│       └── app.js             # Frontend JavaScript logic
│
├── utils/                     # (Future) Utility modules
│   ├── parser.py             # NLP parsing utilities
│   ├── ranker.py             # Ranking algorithm
│   └── cart.py               # Cart management
│
└── data/                      # (Future) Product data
    ├── retailers.json         # Retailer information
    └── products.json          # Product catalog
```

---

## 🔌 API Endpoints

### 1. Parse Shopping Brief

**Endpoint:** `POST /api/parse-brief`

**Request Body:**
```json
{
  "user_input": "I need skiing gear, budget $500, medium size, fast delivery"
}
```

**Response:**
```json
{
  "success": true,
  "specification": {
    "budget": 500,
    "delivery_urgency": "fast",
    "size": "medium",
    "preferences": ["warm", "waterproof"],
    "required_items": ["jacket", "pants", "gloves"]
  }
}
```

### 2. Discover Products

**Endpoint:** `POST /api/discover-products`

**Request Body:**
```json
{
  "specification": {
    "budget": 500,
    "required_items": ["jacket", "pants"]
  }
}
```

**Response:**
```json
{
  "success": true,
  "products": [
    {
      "id": "prod_001",
      "name": "Arc'teryx Rush Jacket",
      "price": 380,
      "rating": 4.8,
      "retailer": "REI",
      "delivery_days": 2,
      "score": 97,
      "score_breakdown": {
        "price_fit": 38,
        "delivery": 30,
        "rating": 24,
        "preferences": 20
      }
    }
  ]
}
```

### 3. Checkout

**Endpoint:** `POST /api/checkout`

**Request Body:**
```json
{
  "cart": {
    "items": [
      {"product_id": "prod_001", "quantity": 1},
      {"product_id": "prod_002", "quantity": 1}
    ]
  }
}
```

**Response:**
```json
{
  "success": true,
  "order_id": "ORD-2026-001",
  "total": 520,
  "retailers": ["REI", "Amazon"],
  "estimated_delivery": "Feb 12, 2026"
}
```

### 4. Health Check

**Endpoint:** `GET /api/health`

**Response:**
```json
{
  "status": "healthy",
  "timestamp": "2026-02-08T10:30:00Z",
  "version": "1.0.0"
}
```

---

## 🔑 Key Features

### 1. Explainable AI

**Transparency Principles:**
- Every decision has a clear justification
- Score breakdowns visible to users
- No black-box recommendations
- Audit trail for all rankings

### 2. Graceful Degradation

**Fallback Mechanisms:**
```
AI Parsing Failed
    ↓
Deterministic Parser
    ↓
Default Values
    ↓
User Prompt for Clarification
```

### 3. Modular Architecture

**Benefits:**
- Easy to add new retailers
- Simple to extend ranking criteria
- Clean separation of concerns
- Testable components

### 4. User-Centric Design

**Features:**
- Clean, intuitive interface
- Real-time feedback
- Budget tracking
- Progress indicators

### 5. Production-Ready Code

**Quality Measures:**
- Error handling
- Input validation
- Logging
- Documentation
- Type hints (future)

---

## 🚀 Future Enhancements

### Phase 1: Core Improvements

**1. Real Retailer Integration**
- Actual API connections to Amazon, REI, etc.
- Live product data
- Real-time inventory
- Actual pricing

**2. User Authentication**
- Secure login system
- User profiles
- Order history
- Saved preferences

**3. Persistent Storage**
- Database integration (PostgreSQL/MongoDB)
- Cart persistence
- Order tracking
- User preferences storage

### Phase 2: Advanced Features

**4. Personalization Engine**
```python
def personalize_rankings(user_history, products):
    """
    Machine learning model to learn:
    - User brand preferences
    - Price sensitivity
    - Style preferences
    - Purchase patterns
    """
```

**5. Async Orchestration**
- Parallel retailer queries
- Faster response times
- WebSocket for real-time updates
- Background task processing

**6. Advanced Analytics**
- User behavior tracking
- Conversion optimization
- A/B testing framework
- Performance monitoring

### Phase 3: Enterprise Features

**7. Payment Integration**
- Stripe/PayPal integration
- Secure payment processing
- Multi-currency support
- Refund handling

**8. Advanced Search**
- Image-based search
- Voice input
- Semantic search
- Filter combinations

**9. Social Features**
- Wishlists
- Product sharing
- Reviews and ratings
- Social recommendations

### Phase 4: Scaling

**10. Infrastructure**
- Docker containerization
- Kubernetes orchestration
- Load balancing
- CDN integration

**11. Monitoring**
- Application performance monitoring
- Error tracking (Sentry)
- User analytics
- Business metrics dashboard

---

## 👥 Team Information

### Project Details

| Field | Value |
|-------|-------|
| **Developer** | [Your Name] |
| **Event** | Hack-Nation Global AI Hackathon |
| **Track** | VC Track |
| **Challenge** | Agentic Commerce |
| **Technology** | Python + Flask + Google Gemini |

### Contact

- **GitHub:** [Your GitHub Profile]
- **Email:** [Your Email]
- **LinkedIn:** [Your LinkedIn]

---

## 📄 License

```
MIT License

Copyright (c) 2026 [Your Name]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## 🙏 Acknowledgments

### Technologies Used

- **Google Gemini AI** - Natural language understanding
- **Flask** - Web framework
- **Python** - Core language

### Inspiration

This project demonstrates how AI can be used responsibly in e-commerce by:
- Maintaining transparency
- Providing explainable decisions
- Combining AI with deterministic logic
- Prioritizing user trust

---

## 📞 Support

If you encounter any issues or have questions:

1. **Documentation**: Read this README carefully
2. **Issues**: Create GitHub issues for bugs or feature requests
3. **Email**: Contact at [Your email]
4. **Demo**: Watch the video demo: [Link]

---

**Built with Python 🐍 and thoughtful AI engineering for real-world agentic commerce.**

**Happy Shopping! 🛒**
