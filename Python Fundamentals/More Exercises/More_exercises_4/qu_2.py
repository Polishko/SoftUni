from math import sqrt, floor

x_1 = float(input())
y_1 = float(input())
x_2 = float(input())
y_2 = float(input())


def distance_to_center(a, b, c, d):

    result = 0

    distance_1 = sqrt(a ** 2 + b ** 2)
    distance_2 = sqrt(c ** 2 + d ** 2)

    if distance_1 <= distance_2:
        result = f"({floor(a)}, {floor(b)})"
    else:
        result = f"({floor(c)}, {floor(d)})"

    print(result)


distance_to_center(x_1, y_1, x_2, y_2)
