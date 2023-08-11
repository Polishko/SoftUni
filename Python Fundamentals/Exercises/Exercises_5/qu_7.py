def sort_list(a):
    factor_tens = 0
    tens_groups = []

    while len(a) > 0:
        factor_tens += 10

        current_tens_list = list(filter(lambda x: x <= factor_tens, a))
        a = list(filter(lambda x: x > factor_tens, a))

        tens_group = f"Group of {factor_tens}'s: {current_tens_list}"
        tens_groups.append(tens_group)

    return tens_groups


num_list = [int(num) for num in input().split(", ")]

result = sort_list(num_list)
print(*result, sep="\n")
