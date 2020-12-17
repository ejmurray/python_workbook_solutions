"""
For this exercise, write a Python function (pig_latin) that takes a string as input, assumed to be an English word.
The function should return the translation of this word into Pig Latin. You may assume that the word contains no
capital letters or punctuation.

If the word begins with a vowel (a, e, i, o, or u), add “way” to the end
of the word. So “air” becomes “airway” and “eat” becomes “eatway.”

If the word begins with any other letter, then we take the first letter, put it on the end of
the word, and then add “ay.” Thus, “python” becomes “ythonpay” and “computer” becomes “omputercay.”

Consider an alternative version of Pig Latin --We don’t check to see if the first letter is a vowel, but,
rather, we check to see if the word contains two different vowels. If it does, we don’t move the first letter
to the end. Because the word “wine” contains two different vowels (“i” and “e”), we’ll add “way” to the end of it,
giving us “wineway.” By contrast, the word “wind” contains only one vowel, so we would move the first letter to
the end and add “ay,” rendering it “indway.”
"""


def pig_latin_alternative(word):
    """
    Convert a string into pig latin. Handle punctuation.
    """
    letters_set = {char for char in word}
    vowels = "aeiouAEIOU"
    vowel_count = 0

    for i in letters_set:
        if i in vowels:
            vowel_count += 1
    if vowel_count > 1:
        return f"{word}way"
    elif vowel_count <= 1:
        return f"{word[1:]}{word[0]}ay"


err_msg = "Mistranslation happened!"
assert pig_latin_alternative("wine") == "wineway", err_msg
assert pig_latin_alternative("wind") == "indway", err_msg
