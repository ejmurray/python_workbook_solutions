from decimal import Decimal, getcontext


def add_two_numbers(first_number, second_number):
    """
    Add two numbers using the built-in decimal module.
    """
    getcontext().prec = 2
    return Decimal(first_number) + Decimal(second_number)


print(add_two_numbers(2.3444, 3.3222))
