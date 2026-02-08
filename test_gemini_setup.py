#!/usr/bin/env python3
"""
Test script for Gemini API integration
Run this to verify your setup before running the main app
"""

import os
import sys
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def test_gemini_connection():
    """Test if Gemini API key is valid"""
    print("🔍 Testing Gemini API Connection...")
    print("-" * 50)
    
    # Check if API key exists
    api_key = os.getenv('GEMINI_API_KEY')
    
    if not api_key:
        print("❌ GEMINI_API_KEY not found in .env file")
        print("\nTo fix:")
        print("1. Copy .env.example to .env")
        print("2. Get API key from: https://aistudio.google.com/app/apikey")
        print("3. Add it to .env file")
        return False
    
    if not api_key.startswith('AIzaSy'):
        print(f"⚠️  API key format looks wrong: {api_key[:10]}...")
        print("Gemini API keys usually start with 'AIzaSy'")
        return False
    
    print(f"✅ API key found: {api_key[:10]}...{api_key[-4:]}")
    
    # Try to import and configure Gemini
    try:
        import google.generativeai as genai
        print("✅ google-generativeai package installed")
    except ImportError:
        print("❌ google-generativeai not installed")
        print("\nTo fix:")
        print("pip install google-generativeai")
        return False
    
    # Configure API
    try:
        genai.configure(api_key=api_key)
        print("✅ Gemini API configured")
    except Exception as e:
        print(f"❌ Failed to configure Gemini: {e}")
        return False
    
    # Test API call
    try:
        print("\n🧪 Testing API call...")
        model = genai.GenerativeModel('gemini-2.0-flash-lite')
        response = model.generate_content("Say 'Hello from Gemini!' in JSON format: {\"message\": \"...\"}")
        
        print("✅ API call successful!")
        print(f"📝 Response: {response.text[:100]}...")
        
        return True
        
    except Exception as e:
        print(f"❌ API call failed: {e}")
        print("\nPossible issues:")
        print("- Invalid API key")
        print("- No internet connection")
        print("- API quota exceeded")
        return False


def test_parsing_modes():
    """Test both parsing modes"""
    print("\n" + "="*50)
    print("🧪 Testing Parsing Modes")
    print("="*50)
    
    test_message = "Skiing outfit, $400, size M, 5 days, warm and waterproof"
    
    # Test regex parsing
    print("\n📝 Testing Regex Parsing...")
    try:
        from app import ShoppingAgent
        
        # Force regex mode
        agent = ShoppingAgent()
        agent.use_ai = False
        
        spec = agent.parse_brief_with_regex(test_message)
        print("✅ Regex parsing successful!")
        print(f"   Budget: ${spec['budget']}")
        print(f"   Delivery: {spec['delivery_days']} days")
        print(f"   Size: {spec['size']}")
        print(f"   Items: {', '.join(spec['items'])}")
        
    except Exception as e:
        print(f"❌ Regex parsing failed: {e}")
    
    # Test Gemini parsing
    if os.getenv('GEMINI_API_KEY'):
        print("\n🤖 Testing Gemini AI Parsing...")
        try:
            agent.use_ai = True
            spec = agent.parse_brief_with_gemini(test_message)
            print("✅ Gemini parsing successful!")
            print(f"   Budget: ${spec['budget']}")
            print(f"   Delivery: {spec['delivery_days']} days")
            print(f"   Size: {spec['size']}")
            print(f"   Items: {', '.join(spec['items'])}")
            print(f"   Scenario: {spec.get('scenario', 'N/A')}")
            
        except Exception as e:
            print(f"❌ Gemini parsing failed: {e}")
    else:
        print("\n⏭️  Skipping Gemini test (no API key)")


def test_available_models():
    """List available Gemini models"""
    print("\n" + "="*50)
    print("📋 Available Gemini Models")
    print("="*50)
    
    api_key = os.getenv('GEMINI_API_KEY')
    if not api_key:
        print("⏭️  Skipping (no API key)")
        return
    
    try:
        import google.generativeai as genai
        genai.configure(api_key=api_key)
        
        print("\n🎯 Recommended FREE models for this project:\n")
        
        recommended = [
            'gemini-2.0-flash-lite',
            'gemini-2.5-flash',
            'gemini-2.5-pro'
        ]
        
        models = genai.list_models()
        found_models = []
        
        for model in models:
            model_name = model.name.replace('models/', '')
            if any(rec in model_name for rec in recommended):
                found_models.append(model_name)
        
        for i, model_name in enumerate(found_models[:5], 1):
            emoji = "⚡" if "flash" in model_name else "🧠"
            current = "← CURRENT" if model_name == 'gemini-2.0-flash-lite' else ""
            print(f"{i}. {emoji} {model_name} {current}")
        
        print(f"\n✅ Total available models: {len(list(models))}")
        print("💡 Tip: All models above are FREE to use!")
        
    except Exception as e:
        print(f"❌ Failed to list models: {e}")


def main():
    """Run all tests"""
    print("🚀 Agentic Commerce - Gemini Setup Test")
    print("="*50)
    
    # Test 1: Gemini connection
    gemini_ok = test_gemini_connection()
    
    # Test 2: Parsing modes
    test_parsing_modes()
    
    # Test 3: Available models
    test_available_models()
    
    # Summary
    print("\n" + "="*50)
    print("📊 Test Summary")
    print("="*50)
    
    if gemini_ok:
        print("✅ Gemini API: Working")
        print("✅ Your project will use AI-powered parsing")
        print("\n🎉 You're ready to run: python app.py")
    else:
        print("⚠️  Gemini API: Not configured")
        print("✅ Your project will use regex parsing (still works!)")
        print("\n💡 To enable AI parsing:")
        print("   1. Get free API key: https://aistudio.google.com/app/apikey")
        print("   2. Add to .env file: GEMINI_API_KEY=your-key")
        print("   3. Set USE_AI_PARSING=true in .env")
    
    print("\n" + "="*50)


if __name__ == "__main__":
    main()
