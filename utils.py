import random
from datetime import datetime
from config import OFFLOAD_PROBABILITY

def parse_log_message(text, update):
    tags = [word[1:] for word in text.split() if word.startswith("#")]
    return {
        "user": update.effective_user.username or str(update.effective_user.id),
        "text": text,
        "tags": tags,
        "timestamp": datetime.now()
    }

def should_offload():
    return random.random() < float(OFFLOAD_PROBABILITY)
