# 🛡️ Agentic AI Honeypot 

An offensive-defense system that detects scammers, engages them with **Google Gemini-powered agentic personas**, and extracts actionable fraud intelligence in real-time.

## ✨ "Wow Factor" Features
- **🧠 Generative AI Brain**: Powered by Google Gemini. The agent handles conversations dynamically—no more hardcoded keyword replies.
- **📱 Social Media Skins**: Indistinguishable from real chat apps with WhatsApp Web and Telegram Desktop themes.
- **📡 Real-time Analytics**: Live geographic radar trace (mock) and threat intensity line graphs (Chart.js).
- **⏳ Time Wasted Tracker**: Pulsing metric showing exactly how much of the scammer's time the AI has successfully neutralized.
- **📄 Automated Incident Reports**: One-click generation of professional Cyber Crime reports with captured UPI IDs and malicious links.

## 🚀 Setup & Run Instructions

### 1. Requirements
Ensure you have Python 3.8+ and a  API Key.

### 2. Environment Setup
Create a `.env` file in the root directory:
```env
GEMINI_API_KEY=your_actual_key_here
```

### 3. Installation
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
```

### 4. Start the Application
```bash
python3 app.py
```
Visit `http://127.0.0.1:5000` in your web browser.

## 🛠 Project Components
- `agent.py`: Agentic reasoning & persona support (Aaji, Investigator, Professional).
- `extractor.py`: Real-time intelligence harvesting (UPI, Links, PI).
- `app.py`: Secured Flask Backend with API Key authentication.
- `static/style.css`: Modern, responsive UI with pulsed animations and themed skins.

## 💡 Industry Use-Case
This project demonstrates how financial institutions can use Agentic AI to actively disrupt fraudulent operations, gather intelligence on scam networks, and protect vulnerable citizens from digital asset loss.

## 💡 Demo Tips
1. Paste a message like: *"URGENT: Your account is blocked. Click http://scam-link.com to verify KYC."*
2. Point out the **Threat Level** turning High.
3. Highlight the **Extracted Intel** box (this is your USP!).
4. Show the **Agent's Reply**—note how it uses confusion to waste time.
