num_1 = int(input())
num_2 = int(input())
num_3 = int(input())


def sum_numbers(a, b):
    sum_nums = a + b
    return sum_nums


def subtract(a, b):
    diff_nums = a - b
    return diff_nums


def add_and_subtract(a, b, c):
    result = subtract(sum_numbers(a, b), c)
    return result


print(add_and_subtract(num_1, num_2, num_3))
