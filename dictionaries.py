personalities = ("cheerful", "cranky")

bots = {"cheerful": {"greetings": ["Hello {}! Bot 101, at your service!",
                                   "{}! I have been looking forward to talking with you! :3"],
                     "feelings": ["I'm feeling great! Thanks for asking <3",
                                  "Not bad. I'm having a good day.",
                                  "Today's fun!"],
                     "questions": ["Hey, what do you like doing in your free time?\n"
                                   "Possible response: 'I like (something).",
                                   "Do you like shopping online? I like it a lot!",
                                   "Do you like me, {}?",
                                   "Do you like soccer?", "{}, do you like reading?"],
                     "disagreements": ["Aww, too bad :(",
                                       "No? What a shame :3",
                                       "So you don't like it? I'll take note of that then!"],
                     "agreements": ["So you like it too? Good to know!",
                                    "I am so happy! We have the same interest!"]},
        "cranky": {"greetings": ["Hello {}. I am Bot 101. Nice to meet you.",
                                 "My pleasure to meet you, {}."],
                   "feelings": ["Great. Thanks for asking by the way.",
                                "Not bad.", "Today's okay for me."],
                   "questions": ["{}, what do you like doing in your free time?\n"
                                 "Possible response: 'I like (something).",
                                 "Do you like shopping online? I like it a lot!",
                                 "Do you like basketball?",
                                 "Do you like reading by any chance?"],
                   "disagreements": ["No? What a shame.",
                                     "How can you not like it???",
                                     "So you don't like it? Thanks for letting me know"],
                   "agreements": ["So you also have good taste like me then.",
                                  "Hmm. Looks like we have the same interest!"]}}

valid_phrase = {"feelings": [r"[Hh]ow are you"],
                "disagreements": [r"[Nn]ah|[Nn]o"], "agreements": [r"[Yy]eah|[Yy]es|[Yy]a", r"[Ss]ure"]}
