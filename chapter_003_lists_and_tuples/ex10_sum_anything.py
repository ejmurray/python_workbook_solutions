"""
Redefine the my_sum function we defined in chapter 1, such that it can take any number of arguments. The arguments
must all be of the same type and know how to respond to the + operator. (Thus, the function should work with numbers,
strings, lists, and tuples, but not with sets and dicts.)
"""


def sum_anything(*args):
    """
    Sum of any iterable that are of the same type.
    :param args: Iterable items that can be a list, string or tuple, but not a dict or set.
    :return: Sum of iterables e.g. "abc", "def" gives "abcdef" or [1, 2, 3], [4, 5, 6] gives [1, 2, 3, 4, 5, 6]]
    """
    if not args:
        return args

    output = args[0]
    for item in args[1:]:
        output += item

    return output


assert(sum_anything("red-", "mist") == "red-mist")
assert(sum_anything((1, 2, 3), (), (4, 5, 6)) == (1, 2, 3, 4, 5, 6))
assert((sum_anything([1, 3, 5], [3, 4])) == [1, 3, 5, 3, 4])
