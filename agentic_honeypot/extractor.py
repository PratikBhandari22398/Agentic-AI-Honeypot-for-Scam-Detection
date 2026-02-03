import re

def extract_info(text):
    # Regex for common fraud patterns
    upi_pattern = r"\b[\w.-]+@[\w.-]+\b"
    bank_pattern = r"\b\d{9,18}\b"
    # Improved link pattern to catch URLs without http/https as well
    link_pattern = r"(?:https?://)?(?:www\.)?[\w\.-]+\.[a-z]{2,}(?:\/\S*)?"
    phone_pattern = r"\b\+?\d{10,12}\b"

    extracted = {
        "payment_anchors": {
            "upi_ids": re.findall(upi_pattern, text),
            "bank_accounts": re.findall(bank_pattern, text)
        },
        "digital_footprint": {
            "links": re.findall(link_pattern, text),
            "phones": re.findall(phone_pattern, text),
            "keywords": re.findall(r"(?i)\b(kyc|urgent|blocked|update|verify|account|otp|password|login|lost|safe|pin| Aadhaar|Pan)\b", text)
        },
        "metadata": {
            "threat_score": 0.0,
            "categories": []
        }
    }

    # Basic scoring logic for the 'Intelligence' feel
    if extracted["payment_anchors"]["upi_ids"]:
        extracted["metadata"]["threat_score"] += 0.4
        extracted["metadata"]["categories"].append("Payment Fraud")
    if extracted["digital_footprint"]["links"]:
        extracted["metadata"]["threat_score"] += 0.5
        extracted["metadata"]["categories"].append("Phishing")
    
    # Cap at 1.0
    extracted["metadata"]["threat_score"] = min(1.0, extracted["metadata"]["threat_score"])
    
    return extracted

