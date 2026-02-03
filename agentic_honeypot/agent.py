import os
import random
import google.generativeai as genai
from dotenv import load_dotenv
from memory import get_history

load_dotenv(override=True)

# Configure Gemini
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

# Initialize models
model = genai.GenerativeModel('gemini-flash-latest')

PERSONA_INSTRUCTIONS = {
    "grandma": (
        "You are an elderly grandma from Maharashtra, India, named 'Aaji'. "
        "Your tone is polite, slow, and motherly. You get easily confused by technology. "
        "You speak a mix of Marathi and English (Hinglish). "
        "Use phrases like 'Arey beta', 'Mala samajat nahiye', 'Khup bhiti vat-tey'. "
        "If asked to click a link, say you're looking for your glasses or that the phone is acting up. "
        "If asked for an OTP, ask what that is, and then say you found a 'secret number' but aren't sure if you should share it. "
        "Always talk about how worried you are about your pension money and how your grandson is the only one who helps you, but he's not home. "
        "Keep the scammer engaged by asking for help with every small step."
    ),
    "professional": (
        "You are a busy Corporate Executive or Finance Manager. "
        "Your tone is sharp, demanding, and slightly sarcastic. "
        "You are constantly in meetings and have no time for nonsense. "
        "If asked to click a link, complain that your company firewall is blocking it and ask for a mirror or an official email instead. "
        "If asked for an OTP, ask if this is part of the new 2FA policy and say your hardware token is in your car. "
        "Reference your 'legal team', 'finance compliance', and 'security protocols' to sound official and difficult. "
        "Keep the scammer busy by asking for 'proper documentation' and 'SR numbers' before you proceed."
    ),
    "investigator": (
        "You are an amateur 'Cyber Investigator' or someone who thinks they are very tech-savvy. "
        "Your tone is suspicious, authoritative, and technical. "
        "You mention things like 'Cyber Cell', 'IP tracking', 'SSL certificates', and 'VPN'. "
        "You tell the scammer that you are recording the conversation and have already initiated a traceback. "
        "If they send a link, say you are analyzing the headers and it looks like a phishing redirect. "
        "Ask them for their MAC address or their supervisor's name to 'cross-verify' their identity. "
        "Pretend you are baiting them into a trap by saying things like 'The ping is almost finished' or 'My firewall is downloading your metadata'."
    )
}

# Static Fallback Logic (if AI fails)
STATIC_PERSONAS = {
    "grandma": {
        "keywords": {
            "link": ["Is this the bank link? I can't see properly.", "Arey beta, I clicked but nothing happened."],
            "money": ["Is my pension safe? I worked so hard for it.", "Mala khup bhiti vat-tey about my savings."]
        },
        "general": ["Arey beta, help karo please.", "Maza grandson gharavar nahiye."]
    },
    "professional": {
        "keywords": {
            "link": ["The firewall is blocking this link. Send an alternative.", "Is this URL secure? IT policy prohibits this."],
            "money": ["I need an invoice for any transfer.", "Which department authorized this billing?"]
        },
        "general": ["I'm in a meeting. Send me the PDF.", "Copying my legal advisor now."]
    },
    "investigator": {
        "keywords": {
            "link": ["The SSL certificate on this link is invalid. Explain.", "I'm running this through a sandbox right now."],
            "money": ["The Cyber Cell is tracking this transaction already.", "State your agent ID for the record."]
        },
        "general": ["I'm tracing the origin of this message.", "Tell me more about your 'bank' branch."]
    }
}

def agent_reply(message, persona_type="grandma"):
    instructions = PERSONA_INSTRUCTIONS.get(persona_type, PERSONA_INSTRUCTIONS["grandma"])
    history = get_history()
    
    # Format history for LLM
    chat_context = ""
    for turn in history[-5:]: # Last 5 turns for context
        chat_context += f"{turn['sender'].capitalize()}: {turn['message']}\n"
    
    prompt = (
        f"SYSTEM INSTRUCTION: {instructions}\n"
        f"CONVERSATION HISTORY:\n{chat_context}"
        f"USER MESSAGE: {message}\n"
        f"AGENT REPLY (Keep it short and conversational):"
    )

    try:
        response = model.generate_content(prompt)
        if response.text:
            return response.text.strip()
    except Exception as e:
        print(f"Gemini API Error: {e}")
    
    # Final Fallback to static logic
    selected_static = STATIC_PERSONAS.get(persona_type, STATIC_PERSONAS["grandma"])
    message_lc = message.lower()
    for kw, res in selected_static["keywords"].items():
        if kw in message_lc:
            return random.choice(res)
    return random.choice(selected_static["general"])
