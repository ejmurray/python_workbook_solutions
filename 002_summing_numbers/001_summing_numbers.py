def my_sum(*numbers):
    start_num = 0
    for i in numbers:
        start_num += i
    return start_num


print(my_sum(*[10, 20, 30, 40, 50]))
