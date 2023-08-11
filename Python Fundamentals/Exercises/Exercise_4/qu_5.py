

#
# def even_nums(x):
#     result = x % 2 == 0
#     return result
#
#
# even_list = list(filter(even_nums, num_list))
# print(even_list)

num_list = [int(num) for num in input().split(" ")]
filtered_list = list(filter(lambda x: x % 2 == 0, num_list))
