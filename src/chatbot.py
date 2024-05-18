"""A super simple ChatBot."""

import datetime
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

    #
    @staticmethod
    def souvenir() -> str:
        """Write a file.

        :return: confirming success.
        """
        filename = "souvenir.txt"
        text = "AImigo was here."

        with open(filename, "w") as file:
            file.write(text)
        return "Success!"

    def tell_time(self) -> str:
        """Say hi, followed by the time.

        :return: The greeting sentence.
        """
        return f"Hi! The time currently is {datetime.datetime.now().astimezone()}"

    # TODO(Jeffrey): Add option "Give me a random name"

    def get_conversation_options(self) -> list[tuple[str, Callable[[], str]]]:
        """Get conversation options.

        :return: A list of tuples containing the conversation options.
        """
        return [
            ("Say hello", self.say_hi),
            ("Tell the time", self.tell_time),
            ("Leave a souvenir", self.souvenir),
            ("Give the answer to life, the universe, and everything", lambda: "42"),
        ]
