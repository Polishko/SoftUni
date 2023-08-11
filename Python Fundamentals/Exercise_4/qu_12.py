num_1 = int(input())
num_2 = int(input())


def factorial_num_operations(a, b):
    factorial_a = 1
    factorial_b = 1

    for i in range(a, 1, -1):
        factorial_a *= i

    for i in range(b, 1, -1):
        factorial_b *= i

    return f"{factorial_a / factorial_b:.2f}"


print(factorial_num_operations(num_1, num_2))
