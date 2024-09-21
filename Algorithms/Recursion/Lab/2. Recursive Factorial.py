def recursive_factorial(n):
    if n == 0:
        return 1

    return n * recursive_factorial(n-1)


num = int(input("Enter a number: "))
print(recursive_factorial(num))
