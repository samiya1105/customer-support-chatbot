from chatbot import ChatBot
import nltk

print("Initializing ChatBot...")
try:
    bot = ChatBot()
    print("ChatBot initialized.")
except Exception as e:
    print(f"Error initializing ChatBot: {e}")
    exit()

test_phrases = [
    "forgot password",
    "delivery time",
    "how do I create an account",
    "is my data safe"
]

print("\n--- Testing Phrases ---")
for phrase in test_phrases:
    print(f"\nUser Input: '{phrase}'")
    try:
        response = bot.get_response(phrase)
        print(f"Bot Response: {response}")
    except Exception as e:
        print(f"Error getting response: {e}")
