from dictionaries import bots, personalities, valid_phrase
import random
import re


class User:
    def __init__(self, name, bot_info):
        self.name = name
        self.bot = bot_info


def choose_bot_personality():
    print("\nWhich personality would you like your bot be?")
    for index, personality in enumerate(personalities, 1):
        print("\t{0}. {1}".format(index, personality.title()))

    user_choice = input("Your choice: ")
    while user_choice not in map(str, range(1, 3)):
        user_choice = input("Invalid. Please try again. \nYour choice: ")

    return personalities[int(user_choice) - 1]


def ask_for_username():
    return input("\nHi there. What's your name? ").strip()


def create_user_profile():
    return User(ask_for_username(), choose_bot_personality())


def interaction(user_profile):
    username = user_profile.name
    bot_type = user_profile.bot

    print("\nLet's get started. Type Q or q to quit anytime.")
    print("BOT 101: " + random.choice(bots[bot_type]["greetings"]).format(username))
    print("Possible response: Hello back | Ask 'How are you?'")

    user_input = input("YOU: ").strip()
    while user_input.capitalize() != "Q":
        bot_answer = response_matching(user_input)
        print("BOT 101: " + random.choice(bots[bot_type][bot_answer]).format(username))
        user_input = input("YOU: ").strip()


def response_matching(message):
    for question_type, matched_phrases in valid_phrase.items():
        for regex in matched_phrases:
            phrase_regex = re.compile(regex)
            match = phrase_regex.search(message)
            if match is not None:
                return question_type

    return "questions"


def main():
    user = create_user_profile()
    interaction(user)


if __name__ == "__main__":
    start_signal = "N"
    while start_signal == "N":
        start_signal = input("START? Y/n ").title()
    main()
