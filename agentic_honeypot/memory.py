conversation = []

def save_message(sender, message):
    conversation.append({
        "sender": sender,
        "message": message
    })

def get_history():
    return conversation

def reset_history():
    global conversation
    conversation = []
