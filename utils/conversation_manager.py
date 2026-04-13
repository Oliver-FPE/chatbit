class ConversationManager:
    def __init__(self):
        self.history = []

    def add_message(self, message):
        self.history.append(message)

    def retrieve_history(self):
        return self.history

    def clear_conversations(self):
        self.history = []

    def export_session_data(self):
        return {'session_data': self.history}

# Example Usage:
# cm = ConversationManager()
# cm.add_message("Hello, how are you?")
# print(cm.retrieve_history())
# cm.clear_conversations()