from chatbot import ChatBot
import unittest

class TestChatBot(unittest.TestCase):
    def setUp(self):
        print("Setting up ChatBot for testing...")
        self.bot = ChatBot()

    def test_greeting(self):
        response = self.bot.get_response("Hello")
        print(f"Input: Hello, Response: {response}")
        self.assertIn(response, [
            "Hello!",
            "Hi there! How can I help you today?",
            "Greetings! What can I do for you?",
            "Hey! I'm here to assist you."
        ])

    def test_hours(self):
        response = self.bot.get_response("What time are you open?")
        print(f"Input: What time are you open?, Response: {response}")
        self.assertIn(response, [
            "We are open from 9am to 5pm, Monday through Friday.",
            "Our operating hours are 9:00 AM to 5:00 PM on weekdays."
        ])

    def test_products(self):
        response = self.bot.get_response("Do you have laptops?")
        print(f"Input: Do you have laptops?, Response: {response}")
        self.assertIn(response, [
             "We sell a variety of electronics including laptops, phones, and accessories.",
             "We offer a wide range of tech products and support services."
        ])

if __name__ == '__main__':
    unittest.main()
