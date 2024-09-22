def recursive_fibonacci(n):
    if n <= 1:
        return 1

    return recursive_fibonacci(n - 1) + recursive_fibonacci(n - 2)

n = int(input('Enter a number between 1 and 49: '))
print(recursive_fibonacci(n))