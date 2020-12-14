def my_average(*numbers, initial_number=0):
    """Calculate the average from a list of numbers.

    Args:
        initial_number (int, optional): [description]. Defaults to 0.

    Returns:
        [int]: Average of values in the list of numbers.
    """
    for i in numbers:
        initial_number += i
    return initial_number / len(numbers)


print(my_average(*[10, 20, 30, 50, 40]))
