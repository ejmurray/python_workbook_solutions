"""
Write a function that transposes a list of strings, in which each string contains
multiple words separated by whitespace. Specifically, it should perform in such a
way that if you were to pass the list ['abc def ghi', 'jkl mno pqr', 'stu vwx yz']
to the function, it would return ['abc jkl stu', 'def mno vwx', 'ghi pqr yz']
"""


def transpose_strings(list_of_strings):
    first_items = []
    second_items = []
    third_items = []
    for item in list_of_strings:
        out = item.split(" ")
        first_items.append(out[0])
        second_items.append(out[1])
        third_items.append(out[2])
    out_one = [" ".join(first_items)] + [" ".join(second_items)] + [" ".join(third_items)]

    return out_one


assert transpose_strings(['abc def ghi', 'jkl mno pqr', 'stu vwx yz']) == ['abc jkl stu', 'def mno vwx', 'ghi pqr yz']