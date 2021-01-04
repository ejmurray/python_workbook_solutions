"""
Write a function, first_last, that takes a sequence (string, list, or tuple) and returns the first and last
elements of that sequence, in a two-element sequence of the same type. So first_last('abc') will return the
string ac, while first_last([1,2,3,4]) will return the list [1,4].
"""


def first_last(sequence):
    return sequence[:1] + sequence[-1:]  # the sequence types are the same in this case.


assert(first_last([1, 2, 3, 4])) == [1, 4]
