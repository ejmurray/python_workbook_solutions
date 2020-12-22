"""
Take a text file, creating (and printing) a nonsensical sentence from the nth
word on each of the first 10 lines, where n is the line number.
"""


def nonsensical_text(filename: str, word_number: int):
    """
    Read in a file and return a nonsense sentence.

    :param word_number: Index of letter to jumble.
    :param filename: Name of text file.
    :return: Nonsense sentence.
    """

    with open(filename, "r") as f:
        count = 10
        pig_sentence = []
        vowels = "aeiouAEIOU"

        for line in f:
            words = line.rstrip().split(" ")
            word_n = words[word_number]
            if word_n[0] in vowels:
                pig_sentence.append(f"{word_n}way")
            else:
                pig_sentence.append(f"{word_n[1:]}{word_n[0]}ay")
            count -= 1

    return " ".join(pig_sentence)


print(nonsensical_text("test_text.txt", 2))
