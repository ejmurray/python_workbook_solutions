"""
Write a function that partly emulates the built-in zip function (http://mng.bz/ Jyzv), taking any number of iterables
and returning a list of tuples. Each tuple will contain one element from each of the iterables passed to the function.
Thus, if I call my_zip([10, 20, 30], 'abc'), the result will be [(10, 'a'), (20, 'b'), (30, 'c')]. You can return a list
(not an iterator) and can assume that all of the iterables are of the same length.
"""


zipped_items = []


def my_zip(item_1, item_2):
    """
    Return a list of tuples from two iterables. This assumes that the iterables are of the same length.
    :param item_1: An iterable that can be a list or string
    :param item_2: A second iterable that can be a list or a string
    :return: a list of tuples
    """
    for item in range(len(item_1)):
        paired_items = (item_1[item], item_2[item])
        zipped_items.append(paired_items)
    return zipped_items


# For more than two items and a more general approach use *args


def my_zip_generalised(*args):
    """

    :param args: iterables
    :return: A list of tuples
    """
    zipped_general = [tuple(arg[item] for arg in args) for item in range(len(min(args, key=len)))]
    return zipped_general


assert(my_zip([10, 20, 30], 'abc') == [(10, 'a'), (20, 'b'), (30, 'c')])
assert(my_zip_generalised([10, 20, 30], 'abc', [1, 2, 3, 4]) == [(10, 'a', 1), (20, 'b', 2), (30, 'c', 3)])
