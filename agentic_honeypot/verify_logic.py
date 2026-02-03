from detector import is_scam
from extractor import extract_info
from agent import agent_reply

test_messages = [
    "Dear customer, your bank account is blocked. Please click http://scam-link.com to verify KYC and update UPI.",
    "Pay to pratik@upi for your electricity bill."
]

for msg in test_messages:
    scam = is_scam(msg)
    print(f"Message: {msg}")
    print(f"Is Scam: {scam}")
    if scam:
        intel = extract_info(msg)
        print(f"Extracted Intel: {intel}")
        reply = agent_reply()
        print(f"Agent Reply: {reply}")
    print("-" * 20)
