import openai

class Chatbot:
    def __init__(self, api_key):
        openai.api_key = api_key
        self.history = []

    def add_to_history(self, user_input, bot_response):
        self.history.append({'user': user_input, 'bot': bot_response})

    def generate_prompt(self, system_prompt):
        prompt = system_prompt + '\n'.join([f'User: {item['user']}\nBot: {item['bot']}' for item in self.history]) + '\nUser: '
        return prompt

    def get_response(self, user_input, system_prompt):
        prompt = self.generate_prompt(system_prompt)
        response = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=[{'role': 'user', 'content': user_input}],
            temperature=0.7,
        )
        bot_response = response.choices[0].message['content']
        self.add_to_history(user_input, bot_response)
        return bot_response

# Example usage:
# chatbot = Chatbot(api_key='your-api-key')
# response = chatbot.get_response('Hello, how are you?', 'You are a helpful assistant.\n')