from collections import deque

class ChatMemory:
    def __init__(self, max_length=5):
        # Deque to store recent turns (sliding window)
        self.buffer = deque(maxlen=max_length)

    def add_turn(self, user_input, bot_response):
        # Add user input and bot response to memory
        self.buffer.append((user_input, bot_response))

    def get_context(self):
        # Combine recent turns into a context string
        return "\n".join([f"User: {u}\nBot: {b}" for u, b in self.buffer])
