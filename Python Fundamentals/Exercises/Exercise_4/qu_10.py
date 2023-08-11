number = int(input())


def perfect_num_checker(a):
    divisor_list = []

    for num in range(1, a):

        if a % num == 0:
            divisor_list.append(num)

    if sum(divisor_list) == a:
        return f"We have a perfect number!"
    else:
        return f"It's not so perfect."


print(perfect_num_checker(number))
