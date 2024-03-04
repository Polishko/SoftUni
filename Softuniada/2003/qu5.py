
nums = input().split(' ')


def largest_number(lst):
    max_length = max(len(num) for num in lst)

    multiplier = max_length + 1
    lst.sort(key=lambda x: (x * multiplier)[:multiplier], reverse=True)

    largest_num = ''.join(lst)

    return largest_num


print(largest_number(nums))
