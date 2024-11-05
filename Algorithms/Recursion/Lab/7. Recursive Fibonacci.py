# def recursive_fibonacci(n):
#     if n <= 1:
#         return 1
#
#     return recursive_fibonacci(n - 1) + recursive_fibonacci(n - 2)
#
# n = int(input(''))
# print(recursive_fibonacci(n))


def fibonacci(n):
    arr = [1] * n
    for i in range(1, n + 1):
        if i <= 1:
            arr[i - 1] = 1
        else:
            arr[i - 1] = arr[i - 2] + arr[i - 3]

    return arr[-1]

print(fibonacci(int(input())))
