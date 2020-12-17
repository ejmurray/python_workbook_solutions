"""
For this exercise, write a Python function (pig_latin) that takes a string as input, assumed to be an English word.
The function should return the translation of this word into Pig Latin. You may assume that the word contains no
capital letters or punctuation.

If the word begins with a vowel (a, e, i, o, or u), add “way” to the end
of the word. So “air” becomes “airway” and “eat” becomes “eatway.”

If the word begins with any other letter, then we take the first letter, put it on the end of
the word, and then add “ay.” Thus, “python” becomes “ythonpay” and “computer” becomes “omputercay.”

Write a function called pl_sentence that takes a string containing several words, separated by spaces.
(To make things easier, we won’t actually ask for a real sentence. More specifically, there will be
no capital letters or punctuation.)
"""


def pig_latin_sentence(sentence):
    """
    Convert a sentence into pig latin.
    """
    vowels = "aeiou"
    sentence_items = sentence.split(" ")
    pig_sentence = []  # use a list instead of adding each item using +=. For efficiency use append and then join.
    for word in sentence_items:
        if word[0] in vowels:
            pig_sentence.append(f"{word}way")
        else:
            pig_sentence.append(f"{word[1:]}{word[0]}ay")

    return " ".join(pig_sentence)


assert pig_latin_sentence("this is a test translation") == "histay isway away esttay ranslationtay"