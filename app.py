from flask import Flask, render_template, request, jsonify
from chatbot import ChatBot

app = Flask(__name__)

# Initialize chatbot
try:
    bot = ChatBot()
    print("Chatbot initialized successfully!")
except Exception as e:
    print(f"Error initializing chatbot: {e}")
    # Optional: You might want to handle this more gracefully
    bot = None

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get_response", methods=["POST"])
def get_response():
    if bot is None:
         return jsonify({"response": "Chatbot is not available. Check server logs."})

    user_input = request.json.get("message")
    if not user_input:
        return jsonify({"response": "Please enter a message."})
    
    response = bot.get_response(user_input)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
