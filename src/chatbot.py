"""A super simple ChatBot."""

import datetime
from collections.abc import Callable
from dataclasses import dataclass

import randomname


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

    def tell_time(self) -> str:
        """Say hi, followed by the time.

        :return: The greeting sentence.
        """
        return f"Hi! The time currently is {datetime.datetime.now().astimezone()}"

    def get_random_name(self) -> str:
        """Run randomname method get name.

        :return: random name string
        """
        return randomname.get_name()

    def get_conversation_options(self) -> list[tuple[str, Callable[[], str]]]:
        """Get conversation options.

        :return: A list of tuples containing the conversation options.
        """
        return [
            ("Say hello", self.say_hi),
            ("Tell the time", self.tell_time),
            ("Give me a random name", self.get_random_name),
            ("Give the answer to life, the universe, and everything", lambda: "42"),
        ]
