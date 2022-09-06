"""Py Lint Test.py"""
# SOURCE OF CODE: https://docs.pylint.org/en/1.6.0/tutorial.html

import string

SHIFT = 3
CHOICE = input("would you like to encode or decode?")
WORD = (input("Please enter text"))
LETTERS = string.ascii_letters + string.punctuation + string.digits
ENCODED = ''
if CHOICE == "encode":
    for letter in WORD:
        if letter == ' ':
            ENCODED = ENCODED + ' '
        else:
            X = LETTERS.index(letter) + SHIFT
            ENCODED = ENCODED + LETTERS[X]
if CHOICE == "decode":
    for letter in WORD:
        if letter == ' ':
            ENCODED = ENCODED + ' '
        else:
            X = LETTERS.index(letter) - SHIFT
            ENCODED = ENCODED + LETTERS[X]

print(ENCODED)
