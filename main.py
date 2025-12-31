from chatbot import ChatBot

def main():
    print("Initializing Chatbot... please wait.")
    try:
        bot = ChatBot()
        print("Chatbot is ready! Type 'quit' to exit.")
    except Exception as e:
        print(f"Error initializing chatbot: {e}")
        return

    while True:
        try:
            user_input = input("You: ")
            if user_input.lower() in ['quit', 'exit', 'bye']:
                print("Chatbot: Goodbye!")
                break
            
            response = bot.get_response(user_input)
            print(f"Chatbot: {response}")
            
        except KeyboardInterrupt:
            print("\nChatbot: Goodbye!")
            break

if __name__ == "__main__":
    main()
