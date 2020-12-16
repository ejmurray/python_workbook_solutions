"""
Write a function that takes a float and two integers (before and after). The function should return a
float consisting of before digits before the decimal point and after digits after. Thus, if we call the
function with 1234.5678, 2 and 3, the return value should be 34.567.
"""


def returning_float(first_float, second_int, third_int):
    """
    Return a float consisting of the digits preceding the decimal point (second argument)
    and after the decimal point (third argument).

    This can also be solved using the `index` method of a string.
    """
    before, after = str(first_float).split(".")
    update_before = before[second_int:]
    update_after = after[:third_int]
    new_number = update_before + "." + update_after
    return float(new_number)


print(returning_float(1234.5678, 2, 3))
