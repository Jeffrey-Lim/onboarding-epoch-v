"""Run AIMigo."""

import time

from tqdm import tqdm

from src.chatbot import ChatBot


def run_aimigo() -> None:
    """Run AIMigo."""
    print("Loading AIMigo...")
    for _ in tqdm(range(100)):
        time.sleep(0.01)
    print("Done!")

    # Ask for the user's name and store it
    username = input("What is your name? ")
    aimigo: ChatBot = ChatBot(name="AIMigo", username=username)
    print(f"Hello, {aimigo.username}! I am {aimigo.name}, your Artificially Intelligent friend.")

    # Indefinitely ask for the user's input
    while True:
        # Print the conversation options
        print("What would you like to do?")
        print("0. Exit")

        for i, (option, _) in enumerate(aimigo.get_conversation_options()):
            print(f"{i + 1}. {option}")

        # Get the user's choice
        choice = input("Your choice: ")

        # Check if the user's choice is valid
        if not choice.isdigit() or not 0 <= int(choice) <= len(aimigo.get_conversation_options()):
            print("Invalid choice. Please try again.")
            continue

        if choice == "0":
            print(f"Goodbye, {aimigo.username}!")
            return

        # Get the function to call
        _, func = aimigo.get_conversation_options()[int(choice) - 1]

        # Call the function
        print(func())


if __name__ == "__main__":
    run_aimigo()
