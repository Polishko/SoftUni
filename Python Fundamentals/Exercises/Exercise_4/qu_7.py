num_list = [int(num) for num in input().split(" ")]


def min_max_sum(a):
    min_num = min(a)
    max_num = max(a)
    sum_nums = sum(a)

    return f"The minimum number is {min_num}\nThe maximum number is {max_num}\nThe sum number is: {sum_nums}"


print(min_max_sum(num_list))
