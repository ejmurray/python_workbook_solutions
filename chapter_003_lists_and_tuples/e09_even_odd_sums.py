"""
Write a function that takes a list or tuple of numbers. Return a two-element list, containing (respectively)
the sum of the even-indexed numbers and the sum of the odd-indexed numbers. So calling the function as
even_odd_sums([10, 20, 30, 40, 50, 60]), you’ll get back [90, 120].
"""


def even_odd_sums(sequence):

    odds = sum(sequence[::2])
    evens = sum(sequence[1::2])
    return [odds, evens]


assert(even_odd_sums([10, 20, 30, 40, 50, 60]) == [90, 120])