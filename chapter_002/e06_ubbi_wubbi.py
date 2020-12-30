"""
For this exercise, you’ll write a function (called ubbi_dubbi) that takes a single word
(string) as an argument. It returns a string, the word’s translation into Ubbi Dubbi.
So if the function is called with octopus, the function will return the string uboctubopubus.
And if the user passes the argument elephant, you’ll output ubelubephubant.
"""

vowels = "aeiou"
new_word = []


def ubbi_dubbi(word):
    for item in word:
        if item in vowels:
            new_word.append('ub')
            new_word.append(item)
        else:
            new_word.append(item)
    return ''.join(new_word)


assert ubbi_dubbi('octopus') == "uboctubopubus", 'Incorrect translation.'
