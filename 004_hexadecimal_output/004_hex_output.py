"""
Create a function that converts hexadecimal input into base10 output.

For this exercise, you need to write a function (hex_output) that takes a hex number
and returns the decimal equivalent. That is, if the user enters 50, you’ll assume that
it’s a hex number (equal to 0x50) and will print the value 80 to the screen.
And no, you shouldn’t convert the number all at once using the int function,
although it’s permissible to use int one digit at a time.
"""


def hex_output(hex_input):
    """
    Returns the base10 value of a hexadecimal input.

    """
    values_dict = {"A": 10,
                   "B": 11,
                   "C": 12,
                   "D": 13,
                   "E": 14,
                   "F": 15}
    total = 0
    for i, value in enumerate(reversed(str(hex_input))):
        if value.isalpha():
            value = values_dict[value]
        total += 16**i * int(value)
    return total


assert hex_output("BA15") == 47637
assert hex_output("E1F") == 3615
