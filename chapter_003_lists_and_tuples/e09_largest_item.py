"""
Take a sequence and return the largest element
"""


def largest(sequence):

    if not sequence:
        return None

    output = sequence[0]

    for item in sequence:
        if item > output:
            output = item
    return output


assert(largest("abcde") == "e")