num = int(input())


def odd_even_digit_sums(a):
    odd_list = []
    even_list = []

    for idx, value in enumerate(str(a)):
        digit = int(value)

        if digit % 2 != 0:
            odd_list.append(digit)
        elif digit % 2 == 0:
            even_list.append(digit)

    sum_odd = sum(odd_list)
    sum_even = sum(even_list)

    result = f"Odd sum = {sum_odd}, Even sum = {sum_even}"
    return result


print(odd_even_digit_sums(num))
