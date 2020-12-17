"""
For this exercise, write a Python function (pig_latin) that takes a string as input, assumed to be an English word.
The function should return the translation of this word into Pig Latin. You may assume that the word contains no
capital letters or punctuation.

If the word begins with a vowel (a, e, i, o, or u), add “way” to the end
of the word. So “air” becomes “airway” and “eat” becomes “eatway.”

If the word begins with any other letter, then we take the first letter, put it on the end of
the word, and then add “ay.” Thus, “python” becomes “ythonpay” and “computer” becomes “omputercay.”
"""


def pig_latin(word):
    """
    Convert a string into pig latin.
    """
    if word[0] in "aeiou":
        translated_word = word + "way"
    else:
        translated_word = word[1:] + word[0] + "ay"
    return translated_word


assert pig_latin("easy") == "easyway", "Mistranslation happened!"
assert pig_latin("many") == "anymay", "Mistranslation happened!"
