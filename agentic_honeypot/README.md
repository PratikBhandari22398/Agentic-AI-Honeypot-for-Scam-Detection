# Agentic AI Honeypot

An offensive-defense system that detects scammers, engages them with stalling personas, and extracts fraud intelligence.

## 🚀 Setup & Run Instructions

To run this project on your system, follow these steps:

### 1. Create a Virtual Environment
```bash
python3 -m venv venv
```

### 2. Install Dependencies
```bash
./venv/bin/pip install flask
```

### 3. Run the Application
```bash
./venv/bin/python app.py
```

### 4. Open in Browser
Visit `http://127.0.0.1:5000` in your web browser.

---

## 🛠 Project Components
- `app.py`: Flask backend and intelligence orchestration.
- `agent.py`: Persona logic for the 'Elderly Grandma' strategic stall.
- `detector.py`: Scam identification logic.
- `extractor.py`: Real-time intelligence extraction (UPI, Links, Keywords).
- `templates/index.html`: Premium intelligence dashboard.

## 💡 Hackathon Demo Tips
1. Paste a message like: *"URGENT: Your account is blocked. Click http://scam-link.com to verify KYC."*
2. Point out the **Threat Level** turning High.
3. Highlight the **Extracted Intel** box (this is your USP!).
4. Show the **Agent's Reply**—note how it uses confusion to waste time.
