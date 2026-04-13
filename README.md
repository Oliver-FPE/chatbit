# chatbit
Meaw! 'hi!' 
# Chatbit

Chatbit is an advanced chat application built on top of modern technologies, designed to facilitate seamless communication between users.

## Installation Instructions

To install Chatbit, you will need to follow the steps below using PowerShell:

1. **Clone the repository**:
   
   Open your PowerShell and run:
   ```powershell
   git clone https://github.com/Oliver-FPE/chatbit.git
   cd chatbit
🌐 Web Interface Quick Start
1. Start the Web Server

Open PowerShell in your chatbit directory and run:
PowerShell

python main.py

Then select option 2 for Web interface:
Code

Choose your interface:
1. CLI
2. Web

Enter choice (1 or 2): 2

2. Access the Web Interface

Open your web browser and go to:
Code

http://localhost:5000

You should see the Chatbit chat interface load.
3. Using the Chat

Send a Message:

    Type your message in the input field at the bottom
    Click the "Send" button or press Enter
    The AI will respond with an answer

Example queries:
Code

"What is Python?"
"Explain this code: print('Hello')"
"How do I create a function in JavaScript?"

4. Code Analysis

To analyze code:

    Type or paste code snippets in your message
    Ask the AI to "analyze" or "review" the code
    The AI will provide feedback on:
        Syntax errors
        Best practices
        Performance suggestions
        Language-specific recommendations

Supported Languages:

    Python (.py)
    JavaScript (.js)
    C++ (.cpp)
    C (.c)
    Lua (.lua)

5. View Conversation History

The right sidebar shows:

    Code Analysis Results - Feedback on analyzed code
    Conversation History - All your previous messages and AI responses

6. Features

✅ Real-time chat - Instant responses
✅ Code highlighting - Syntax highlighting for code snippets
✅ Dark theme - Easy on the eyes
✅ Responsive design - Works on desktop and tablet
✅ Session storage - Conversation saved during your session
Example Usage Flow
Code

1. User: "Can you help me debug this Python code?"
2. User: [pastes code]
3. Bot: [analyzes code and provides feedback]
4. User: "How do I fix the error on line 5?"
5. Bot: [explains the fix]
6. User: "Thanks! What about best practices?"
7. Bot: [provides recommendations]

Troubleshooting

Port 5000 in use?
PowerShell

# Edit .env file
notepad .env
# Change FLASK_PORT=5001 (or any other port)

Can't connect to localhost?
PowerShell

# Check if Flask is running properly
# Look for: "Running on http://127.0.0.1:5000"

API key error?
PowerShell

# Verify your OpenAI API key in .env
Get-Content .env

That's it! Enjoy using Chatbit! 🚀
