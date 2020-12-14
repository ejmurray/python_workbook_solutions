def my_sum(*numbers, initial_number=0):
    """Sum over a list of numbers.

    Args:
        initial_number (int, optional): [description]. Defaults to 0.

    Returns:
        [int]: Sum of values in the list and the added initial number.
    """
    for i in numbers:
        initial_number += i
    return initial_number


print(my_sum(*[10, 20, 30, 40, 50, 100], 5))
