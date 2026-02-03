SCAM_KEYWORDS = [
    "bank", "account", "blocked",
    "otp", "upi", "kyc",
    "verify", "urgent", "click",
    "link", "update", "password",
    "pin", "login", "aadhaar",
    "pan", "safety", "illegal",
    "police", "investigation", "lost",
    "paisa", "inam",
    "lottery", "khata", "band", "karat",
    "badla", "tv", "recharge", "free"
]

THRESHOLD = 1

def is_scam(message: str) -> bool:
    message = message.lower()
    score = 0

    for word in SCAM_KEYWORDS:
        if word in message:
            score += 1

    return score >= THRESHOLD
