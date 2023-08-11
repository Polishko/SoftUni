# num_1 = int(input())
# num_2 = int(input())
# num_3 = int(input())
#
#
# def take_min_num(a, b, c):
#     list_nums = [a, b, c]
#     return min(list_nums)
#
#
# print(take_min_num(num_1, num_2, num_3))

def take_min_num(a):
    return min(a)


num_1 = int(input())
num_2 = int(input())
num_3 = int(input())

nums = [num_1, num_2, num_3]
print(take_min_num(nums))
