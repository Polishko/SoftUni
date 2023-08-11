list_nums = [int(num) for num in input().split(" ")]
sum_removed = 0

while len(list_nums) > 0:
    idx = int(input())

    if idx < 0:
        value = list_nums[0]
        list_nums[0] = list_nums[-1]

    elif idx > len(list_nums) - 1:
        value = list_nums[-1]
        list_nums[-1] = list_nums[0]

    else:
        value = list_nums[idx]
        del list_nums[idx]

    list_nums = list(map(lambda x: x + value if x <= value else x - value, list_nums))
    sum_removed += value

print(sum_removed)
