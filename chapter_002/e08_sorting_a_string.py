"""
In this exercise, you’ll explore this idea by writing a function, str_sort, that takes a single string as its
input and returns a string. The returned string should contain the same characters as the input, except that
its characters should be sorted in order, from the lowest Unicode value to the highest Unicode value.
For example, the result of invoking str_sort('cba') will be the string abc.
"""


new_string = []


def str_sort_verbose(input_string):
    for letter in input_string:
        new_string.append(letter)
    sorted_string = sorted(new_string)
    return "".join(sorted_string)


def str_sort_better(inpupt_string):
    return "".join(sorted(inpupt_string))


assert str_sort_better("dcba") == "abcd"