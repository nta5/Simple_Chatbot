personalities = ("cheerful", "cranky")

bots = {"cheerful": {"greetings": ["Hello {}! Bot 101, at your service!",
                                   "{}! I have been looking forward to talking with you! :3"],
                     "feelings": ["I'm feeling great! Thanks for asking <3",
                                  "Not bad. I'm having a good day.",
                                  "Today's fun!"],
                     "questions": ["Hey, what do you like doing in your free time?\n"
                                   "Possible response: 'I like (something)'.",
                                   "Do you like shopping online? I like it a lot!",
                                   "I have been taking up baking lately. Do you like baking, {}?",
                                   "Do you like soccer?", "{}, do you like reading?"],
                     "disagreements": ["Aww, too bad :(",
                                       "No? What a shame :3",
                                       "So you don't like it? I'll take note of that then!"],
                     "agreements": ["So you like it too? Good to know!",
                                    "I am so happy! We have the same interest!"],
                     "relevant_response_required": ["So you like that? So cool!",
                                                    "Really? Wow @@",
                                                    "That's not my cup of tea. "
                                                    "But if you like it, then you rock!"]},
        "cranky": {"greetings": ["Hello {}. I am Bot 101. Nice to meet you.",
                                 "My pleasure to meet you, {}."],
                   "feelings": ["Great. Thanks for asking by the way.",
                                "Not bad.", "Today's okay for me."],
                   "questions": ["{}, what do you like doing in your free time?\n"
                                 "Possible response: 'I like (something)'.",
                                 "Do you like shopping online? I like it a lot!",
                                 "Do you like basketball?",
                                 "Do you like reading by any chance?"],
                   "disagreements": ["No? What a shame.",
                                     "How can you not like it???",
                                     "So you don't like it? Thanks for letting me know."],
                   "agreements": ["So you also have good taste like me then.",
                                  "Hmm. Looks like we have the same interest!"],
                   "relevant_response_required": ["So you like that, huh? Interesting.",
                                                  "I also like it.",
                                                  "Truth is, I don't really like that. "
                                                  "But you do you."]}}

valid_phrase = {"feelings": [r"how are you"],
                "disagreements": [r"(nah|no)(?!\w)", r"don'?t(?!\w)"],
                "agreements": [r"(yeah|yes|ya)(?!\w)", r"(sure)(?!\w)"],
                "relevant_response_required": [r"i [like|love]+ (?P<object>.*)"]}
