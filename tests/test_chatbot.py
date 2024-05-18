"""Test the ChatBot functionalities."""

from src.chatbot import ChatBot


def test_say_hi() -> None:
    """Test the say_hi method."""

    bot = ChatBot(name="Bot")
    assert bot.say_hi() == "Hi! This is Bot."
