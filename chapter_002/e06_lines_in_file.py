"""
Take a text file, creating (and printing) a nonsensical sentence from the nth
word on each of the first 10 lines, where n is the line number.
"""


def nonsensical_text(filename: str, nth_word: int):
    """
    Read in a file and return a nonsense sentence.

    :param nth_word: Index of letter to jumble.
    :param filename: Name of text file.
    :return: Nonsense sentence.
    """

    with open(filename, "r") as f:
        pig_sentence = []
        vowels = "aeiouAEIOU"

        for line in f:
            words = line.rstrip().split(" ")
            word_n = words[nth_word]
            if word_n[0] in vowels:
                pig_sentence.append(f"{word_n}way")
            else:
                pig_sentence.append(f"{word_n[1:]}{word_n[0]}ay")

    return " ".join(pig_sentence[:10])


print(nonsensical_text("test_text.txt", 8))
