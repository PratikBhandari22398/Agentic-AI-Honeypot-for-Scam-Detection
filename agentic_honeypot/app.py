from flask import Flask, request, jsonify, render_template
from detector import is_scam
from memory import save_message, get_history, reset_history
from extractor import extract_info
from agent import agent_reply

app = Flask(__name__)

@app.route("/")
def home():
    reset_history()
    return render_template("index.html")

@app.route("/api/message", methods=["POST"])
def receive_message():
    data = request.json
    message = data.get("message", "").strip()
    persona = data.get("persona", "grandma")

    # Hackathon Security Requirement: API Key check
    expected_api_key = os.getenv("HONEPOT_API_KEY", "hackathon-secret-key")
    provided_key = request.headers.get("X-API-Key")

    if provided_key != expected_api_key:
        return jsonify({"status": "error", "message": "Unauthorized: Invalid API Key"}), 401

    save_message("user", message)
    history = get_history()
    was_scam_before = any(m['sender'] == 'agent' for m in history)
    
    scam = is_scam(message)
    reply = ""
    intelligence = {}

    if scam or was_scam_before:
        reply = agent_reply(message, persona_type=persona)
        save_message("agent", reply)
        intelligence = extract_info(message)
        scam = True # Force scam=True if session is active

    # Professional Intelligence JSON Schema
    history = get_history()
    response = {
        "session_id": "Honeypot-Agent-X1",
        "threat_profile": {
            "scam_detected": scam,
            "threat_level": "High" if scam and intelligence.get("metadata", {}).get("threat_score", 0) >= 0.5 else "Medium" if scam else "None"
        },
        "honeypot_stats": {
            "conversation_turns": len(history),
            "agent_persona": persona,
            "active_engagement": scam
        },
        "extracted_intelligence": intelligence if scam else None,
        "agent_reply": reply,
        "conversation_history": history
    }

    return jsonify(response)


if __name__ == "__main__":
    app.run(debug=True)
