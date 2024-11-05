from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Simple rule-based chatbot response
def generate_response(user_input):
    user_input = user_input.lower()

    # Basic responses for greetings
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I assist you today?"
    elif "how are you" in user_input:
        return "I'm just a bot, but I'm here to help! How about you?"
    elif "bye" in user_input or "goodbye" in user_input:
        return "Goodbye! Have a great day!"
    elif "name" in user_input:
        return "I am your friendly chatbot built using Flask!"
    else:
        return "I'm not sure how to respond to that. Can you ask me something else?"

# Flask route for chatbot responses (POST)
@app.route('/chatbot', methods=['POST'])
def chatbot():
    try:
        # Get the user input from the request JSON body
        user_message = request.json.get('message')
        if not user_message:
            return jsonify({'error': 'No message provided'}), 400

        # Generate a response using the function
        bot_response = generate_response(user_message)

        # Return the response as a JSON object
        return jsonify({'response': bot_response})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Optional homepage route (GET)
@app.route('/')
def home():
    return render_template('index.html')  # Render the HTML page

# Favicon route to prevent 404 errors for favicon requests
@app.route('/favicon.ico')
def favicon():
    return '', 204  # Return a 204 No Content response

if __name__ == '__main__':
    app.run(debug=True)
