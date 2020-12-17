"""
Write a program that asks the user for their name and then produces a “name triangle”:
the first letter of their name, then the first two letters, then the first three,
and so forth, until the entire name is written on the final line.
"""


def name_triangle():
    """
    Print the name that is input as a triangle.
    """
    user_name = input("Enter your name: ")
    name_tree = ""
    for i in range(1, len(user_name)+1):
        name_tree += user_name[:i] + "\n"
    return name_tree


print(name_triangle())
