"""A super simple ChatBot."""

from collections.abc import Callable
from dataclasses import dataclass


@dataclass(slots=True)
class ChatBot:
    """A super simple ChatBot.

    :param name: The name of the ChatBot.
    :param username: The name of the user.
    """

    name: str
    username: str = "MISSING"

    def say_hi(self) -> str:
        """Say hi, followed by the name of the chatbot.

        :return: The greeting sentence.
        """
        return f"Hi! This is {self.name}."

    # TODO(Jeffrey): Add option "Leave a souvenir"

    # TODO(Jeffrey): Add option "Tell the time"

    # TODO(Jeffrey): Add option "Give me a random name"

    # TODO(Jeffrey): Add option "Give the answer to life, the universe, and everything"

    def get_conversation_options(self) -> list[tuple[str, Callable[[], str]]]:
        """Get conversation options.

        :return: A list of tuples containing the conversation options.
        """
        return [
            ("Say hello", self.say_hi),
        ]
