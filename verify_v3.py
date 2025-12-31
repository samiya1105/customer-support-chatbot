from chatbot import ChatBot

bot = ChatBot()
print("Testing 'java'...")
response_java = bot.get_response("java")
print(f"Response: {response_java}")

print("\nTesting 'python'...")
response_python = bot.get_response("python")
print(f"Response: {response_python}")

print("\nTesting 'short_query'...")
response_short = bot.get_response("abc")
print(f"Response: {response_short}")
