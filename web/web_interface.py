from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__)

# Define mock data for the purpose of this example
conversation_history = []

# REST API endpoint for chat
@app.route('/api/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    # Here you would add logic to process the chat input
    response = {'reply': f'You said: {user_input}'}  # Mock response
    conversation_history.append({'user': user_input, 'bot': response['reply']})
    return jsonify(response)

# REST API endpoint for code analysis
@app.route('/api/analyze_code', methods=['POST'])
def analyze_code():
    code = request.json.get('code')
    # Logic for code analysis would go here
    analysis_result = {'result': f'Analyzed code: {code}'}  # Mock result
    return jsonify(analysis_result)

# REST API endpoint for conversation history
@app.route('/api/history', methods=['GET'])
def history():
    return jsonify(conversation_history)

# Serve static HTML frontend
@app.route('/')
def serve_frontend():
    return send_from_directory('.', 'index.html')  # Assuming index.html is in the root directory

if __name__ == '__main__':
    app.run(debug=True)