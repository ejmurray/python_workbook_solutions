def sum_of_objects(list_of_objects):
    """
    Write a function that takes a list of Python objects [ints and strings].
    Sum the objects that either are integers or can be turned into integers,
    ignoring the others.
    """
    numerals = []
    string_list = []

    for i in list_of_objects:
        if type(i) == int:
            numerals.append(i)
        else:
            string_list.append(i)
    try:
        for j in string_list:
            if j.isnumeric():
                numerals.append(int(j))
    except ValueError:
        pass
    print(numerals)
    return sum(numerals)


items_list = [11, 1, 2, 3, 4, "5", "six", 7, 8, 9, "10", "tree"]
print(sum_of_objects(items_list))
