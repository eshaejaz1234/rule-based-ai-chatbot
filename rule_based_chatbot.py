"""
Project 1: Rule-Based AI Chatbot
DecodeLabs - Industrial Training Kit (Batch 2026)
"""

import random

BOT_NAME = "DecodeBot"

responses = {
    "hi": ["Hello! How can I help you today?", "Hey there! 👋"],
    "hello": ["Hi there!", "Hello! Nice to see you."],
    "hey": ["Hey! What's up?", "Hey hey! How's it going?"],
    "how are you": ["I'm just a bot, but I'm doing great! How about you?",
                     "Running smoothly on pure logic today!"],
    "your name": [f"I am {BOT_NAME}, your rule-based assistant."],
    "who are you": [f"I am {BOT_NAME}, built for Project 1 at DecodeLabs."],
    "what can you do": ["I can chat using simple rules — try 'help' to see topics."],
    "help": ["You can talk to me using: hi, how are you, your name, "
              "what can you do, joke, thanks, bye"],
    "joke": ["Why do programmers prefer dark mode? Because light attracts bugs!",
              "I would tell you a UDP joke, but you might not get it."],
    "thanks": ["You're welcome!", "Anytime! 😊"],
    "thank you": ["You're welcome! Happy to help."],
    "bye": ["Goodbye! Have a nice day."],
}

exit_commands = {"bye", "exit", "quit"}


def get_response(user_input: str) -> str:
    options = responses.get(user_input)
    if options:
        return random.choice(options)
    return "I do not understand that. Type 'help' to see what I know."


def main():
    print(f"🤖 {BOT_NAME}: Hello! I'm {BOT_NAME}. "
          f"Type 'bye', 'exit', or 'quit' to leave anytime.\n")

    while True:
        raw_input_text = input("You: ")
        user_input = raw_input_text.lower().strip()

        if user_input in exit_commands:
            print(f"🤖 {BOT_NAME}: Goodbye! Have a nice day. 👋")
            break

        if not user_input:
            continue

        reply = get_response(user_input)
        print(f"🤖 {BOT_NAME}: {reply}")


if __name__ == "__main__":
    main()