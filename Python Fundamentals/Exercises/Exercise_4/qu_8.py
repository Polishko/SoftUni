input_str = input()
list_integers = input_str.split(", ")


def check_if_palindome(a):
    first_part = []
    second_part = []

    n = len(a)
    half_n = len(a) // 2

    if n % 2 == 0:
        for i in range(half_n):
            first_part.append(a[i])
        for k in range(n - 1, half_n - 1, -1):
            second_part.append(a[k])

    elif len(a) % 2 != 0:
        for i in range(half_n):
            first_part.append(a[i])
        for k in range(n - 1, half_n, - 1):
            second_part.append(a[k])

    if first_part == second_part:
        return True
    else:
        return False


for idx in range(len(list_integers)):
    number = list_integers[idx]
    print(check_if_palindome(number))
