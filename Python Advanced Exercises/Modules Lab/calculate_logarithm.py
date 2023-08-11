import math

num = int(input())
logarithm = input()

try:
    print(f"{math.log(num):.2f}") if logarithm == "natural" else print(f"{math.log(num, int(logarithm)):.2f}")
except ValueError:
    print("Cannot take negative base number")
