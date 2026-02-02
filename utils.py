EXIT_KEYWORDS = ["exit", "quit", "bye", "stop", "end"]

def is_exit_message(text: str) -> bool:
    return text.lower().strip() in EXIT_KEYWORDS
