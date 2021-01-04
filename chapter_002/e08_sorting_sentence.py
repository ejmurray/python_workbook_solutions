"""
Given the string “Tom Dick Harry,” break it into individual words,
and then sort those words alphabetically. Once they’re sorted, print them with commas (,) between the names.
"""


def sorted_sentence(sentence):
    words = sentence.split()
    return ", ".join(sorted(words))


assert(sorted_sentence("Tom Dick Harry")) == "Dick, Harry, Tom"
