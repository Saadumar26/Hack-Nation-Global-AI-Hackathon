# ShopUnify 🛒

![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-2.3+-green?logo=flask)
![Google AI](https://img.shields.io/badge/Google_AI-Gemini-orange?logo=google)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Hackathon](https://img.shields.io/badge/Hackathon-Hack--Nation_Global-red)
![Status](https://img.shields.io/badge/Status-Active-success)

**Hack-Nation Global AI Hackathon Submission | VC Track**

An end-to-end AI-powered shopping agent built with Python + Flask that automates the process of finding and purchasing products across multiple retailers.

---

## 🎯 Overview

**ShopUnify** demonstrates how an autonomous AI agent can understand shopping intent, discover products across retailers, rank options transparently, and orchestrate a unified checkout flow.

### Core Capabilities

- Understands shopping intent from natural language
- Discovers products across multiple retailers (Amazon, REI, Backcountry, Evo)
- Ranks options using transparent, explainable Python algorithms
- Combines items into a single unified cart
- Orchestrates multi-retailer checkout flow

### Design Philosophy

> **AI for understanding, algorithms for decisions.**

The system combines AI flexibility (Gemini for parsing) with deterministic Python logic (transparent ranking), making every decision explainable and reproducible.

---

## 🏗️ Tech Stack

| Component | Technology |
|-----------|------------|
| **Backend** | Python 3.8+, Flask |
| **AI Parsing** | Google Gemini API (Free) |
| **Ranking** | Pure Python algorithms |
| **Frontend** | Vanilla JavaScript, HTML5, CSS3 |
| **Deployment** | Vercel / PythonAnywhere |

---

## 🚀 Quick Start

### Prerequisites

```bash
python --version  # Requires Python 3.8+
```

### Installation

```bash
# Clone repository
git clone https://github.com/Saadumar26/Hack-Nation-Global-AI-Hackathon.git
cd Hack-Nation-Global-AI-Hackathon

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Add your GEMINI_API_KEY to .env

# Run application
python app.py
```

Visit: `http://localhost:5000`

---

## 🎮 How It Works

### 1. Natural Language Input

```
User: "I need warm skiing gear, budget $400, medium size, deliver fast"
```

### 2. AI-Powered Parsing (Google Gemini)

```json
{
  "budget": 400,
  "delivery_urgency": "fast",
  "size": "M",
  "preferences": ["warm", "waterproof"],
  "required_items": ["jacket", "pants", "gloves", "goggles", "helmet"]
}
```

### 3. Multi-Retailer Discovery

Searches across:
- Amazon
- REI
- Backcountry
- Evo

### 4. Transparent Ranking Algorithm

```python
Score = (Price Fit × 40%) + (Delivery × 30%) + (Rating × 25%) + Preferences Bonus
```

**Example Output:**
```
Arc'teryx Rush Jacket — 91/100
├─ Price fit:    38/40  (fits budget)
├─ Delivery:     30/30  (2-day shipping)
├─ Rating:       24/25  (4.8★, 250 reviews)
└─ Preferences:  20/20  (warm + waterproof)
```

### 5. Unified Cart & Checkout

- Single cart for multiple retailers
- Real-time budget tracking
- Simulated checkout flow

---

## 📊 Ranking Algorithm Details

### Score Components

| Component | Weight | Description |
|-----------|--------|-------------|
| **Price Fit** | 40% | How well price fits budget |
| **Delivery Speed** | 30% | Matches delivery urgency |
| **Product Quality** | 25% | Rating + review count |
| **Preference Match** | Bonus | Feature alignment |

### Example Calculation

```python
# Product: Arc'teryx Rush Jacket ($380)
# Budget: $400, Urgency: Fast, Preferences: [warm, waterproof]

Price Score    = 38/40  # $380 is 95% of budget
Delivery Score = 30/30  # 2-day delivery (fast)
Rating Score   = 24/25  # 4.8★ with 250 reviews
Preference     = 20/20  # Mentions warm AND waterproof

Total Score    = 112/115 = 97%  → Rank #1
```

---

## ✅ Challenge Requirements Met

### 1. Conversational Brief & Constraints Capture 
- Natural language parsing via Google Gemini
- Structured JSON output
- Fallback to regex-based parsing
- Quick-start scenarios

### 2. Multi-Retailer Discovery 
- 4 retailers (Amazon, REI, Backcountry, Evo)
- 5 product categories
- Realistic pricing and ratings

### 3. Transparent Ranking Engine 
- **Pure Python algorithm** (not LLM-generated)
- Full score breakdown shown to users
- Weighted criteria with clear justification

### 4. Unified Cart Experience 
- Single cart for multiple retailers
- Budget usage tracking
- Category-wise breakdown

### 5. Checkout Orchestration 
- Multi-retailer order simulation
- Step-by-step status updates

---

## 🗂️ Project Structure

```
Hack-Nation-Global-AI-Hackathon/
│
├── app.py                  # Main Flask application
├── requirements.txt        # Python dependencies
├── .env                    # Environment variables (not in repo)
├── .gitignore             # Git ignore rules
├── README.md              # This file
├── vercel.json            # Vercel deployment config
│
├── api/
│   └── index.py           # Vercel entry point
│
├── templates/
│   └── index.html         # Main UI
│
└── static/
    ├── css/
    │   └── styles.css     # Styling
    └── js/
        └── app.js         # Frontend logic
```

---

## 🔌 API Endpoints

### POST `/api/parse-brief`
Parse natural language shopping request

**Request:**
```json
{
  "user_input": "Skiing gear, $400, size M, fast delivery"
}
```

**Response:**
```json
{
  "success": true,
  "specification": {
    "budget": 400,
    "delivery_urgency": "fast",
    "size": "M",
    "required_items": ["jacket", "pants", "gloves"]
  }
}
```

### POST `/api/discover-products`
Get ranked products based on specification

### POST `/api/checkout`
Process multi-retailer checkout

### GET `/api/health`
Health check endpoint

---

## 🔑 Key Features

### 1. Explainable AI
- Every ranking decision is transparent
- Score breakdown shown to users
- No black-box recommendations

### 2. Hybrid Intelligence
- AI (Gemini) for natural language understanding
- Deterministic algorithms for decision-making
- Best of both worlds

### 3. Graceful Fallback
```
Gemini AI → Regex Parser → Default Values → User Clarification
```

### 4. Production-Ready
- Error handling
- Input validation
- Environment configuration
- Deployment configs included

---

## 🚀 Deployment

### Option 1: Vercel (Recommended)

```bash
# Files already configured:
# - vercel.json
# - api/index.py

# Deploy via Vercel Dashboard:
1. Go to vercel.com
2. Import GitHub repository
3. Add environment variables:
   - GEMINI_API_KEY
   - USE_AI_PARSING=true
4. Deploy!
```

### Option 2: PythonAnywhere

```bash
# Free hosting, no credit card
1. Sign up at pythonanywhere.com
2. Clone repository in Bash console
3. Install dependencies
4. Configure WSGI file
5. Add environment variables
6. Reload web app
```

---

## 🎯 Future Enhancements

### Phase 1
- [ ] Real retailer API integration
- [ ] User authentication
- [ ] Database (PostgreSQL)
- [ ] Order history

### Phase 2
- [ ] Personalization engine
- [ ] Image-based search
- [ ] Voice input
- [ ] Advanced analytics

### Phase 3
- [ ] Payment integration (Stripe)
- [ ] Mobile app
- [ ] Social features
- [ ] Recommendation engine

---

## 👥 Team & Contact

| Field | Value |
|-------|-------|
| **Developer** | Muhammad Saad Umar |
| **Event** | Hack-Nation Global AI Hackathon |
| **Track** | VC Track |
| **Challenge** | Agentic Commerce |
| **Project** | ShopUnify |

**Links:**
- 🔗 **GitHub:** [Saadumar26](https://github.com/Saadumar26)
- 📦 **Repository:** [Hack-Nation-Global-AI-Hackathon](https://github.com/Saadumar26/Hack-Nation-Global-AI-Hackathon)
- 💼 **LinkedIn:** [Connect](https://www.linkedin.com/in/muhammadsaadumar/)

---

## 📄 License

MIT License - Copyright (c) 2026 Muhammad Saad Umar

See [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

**Technologies:**
- Google Gemini AI (free tier)
- Flask web framework
- Python 3.8+

**Inspiration:**
This project demonstrates responsible AI use in e-commerce by maintaining transparency, providing explainable decisions, and combining AI with deterministic logic.

---

## 📞 Support

- 📖 **Documentation:** Read this README
- 🐛 **Issues:** [GitHub Issues](https://github.com/Saadumar26/Hack-Nation-Global-AI-Hackathon/issues)
- ⭐ **Star the repo** if you find it helpful!

---

**Built with Python 🐍 + thoughtful AI engineering for real-world unified shopping.**

**Happy Shopping! 🛒**
