input_1 = input()
input_2 = input()


def calculation(a, b):
    result = 0

    if a == "int":
        b = int(b)
        result = b * 2
    elif a == "real":
        result = f"{(float(b) * 1.5):.2f}"
    elif a == "string":
        result = f"${b}$"

    return result


print(calculation(input_1, input_2))
