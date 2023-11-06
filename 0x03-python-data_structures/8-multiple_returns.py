#!/usr/bin/python3
def multiple_returns(sentence):

    lens = len(sentence)
    if not sentence:
        first_character = None
    else:
        first_character = sentence[0]
    return (lens, first_character)
