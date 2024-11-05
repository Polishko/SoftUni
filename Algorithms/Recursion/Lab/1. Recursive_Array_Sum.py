# O(n) complexity because with idx you only move the pointer
def find_array_sum(arr, idx):
    if idx == len(arr) - 1:
        return arr[idx]

    return arr[idx] + find_array_sum(arr, idx + 1)

my_array = [int(x) for x in input().split(' ')]
print(find_array_sum(my_array, 0))

# O(n2) complexity because slicing creates an array

# def find_array_sum(arr):
#     if len(arr) == 1:
#         return arr[0]
#
#     return arr[0] + find_array_sum(arr[1:])
#
# my_array = [int(x) for x in input().split(' ')]
# print(find_array_sum(my_array))