"""
For this exercise, write a Python function (pig_latin) that takes a string as input, assumed to be an English word.
The function should return the translation of this word into Pig Latin. You may assume that the word contains no
capital letters or punctuation.

If the word begins with a vowel (a, e, i, o, or u), add “way” to the end
of the word. So “air” becomes “airway” and “eat” becomes “eatway.”

If the word begins with any other letter, then we take the first letter, put it on the end of
the word, and then add “ay.” Thus, “python” becomes “ythonpay” and “computer” becomes “omputercay.”

Handle capitalized words --If a word is capitalized (i.e., the first letter is capitalized,
but the rest of the word isn’t), then the Pig Latin translation should be similarly capitalized.
"""
import string


def pig_latin_punctuation(word):
    """
    Convert a string into pig latin. Handle punctuation.
    """
    vowels = "aeiouAEIOU"
    if word[-1] in string.punctuation and word[0] in vowels:
        return f"{word[:-1]}way{word[-1]}"
    return f"{word[1:-1]}{word[0]}ay{word[-1]}"


err_msg = "Mistranslation happened!"
assert pig_latin_punctuation("Easy!") == "Easyway!", err_msg
assert pig_latin_punctuation("Many!") == "anyMay!", err_msg
assert pig_latin_punctuation("Many%") == "anyMay%", err_msg
