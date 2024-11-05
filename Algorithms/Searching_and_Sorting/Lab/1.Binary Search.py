# Lecturer`s solution

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        middle_idx = (left + right) // 2
        middle_ele = arr[middle_idx]

        if middle_ele == target:
            return middle_idx

        if target < middle_ele:
            right = middle_idx - 1
        else:
            left = middle_idx + 1

    return - 1


arr = [int(x) for x in input().split()]
target = int(input())

print(binary_search(arr, target))


# def find_element_first(arr, ele, first, last):
#     if first > last:
#         return -1
#
#     middle = (last - first) // 2 + first
#
#     if ele == arr[middle]:
#         return middle
#
#     elif ele < arr[middle]:
#         return find_element_first(arr, ele, first, middle - 1)
#     else:
#         return find_element_first(arr, ele, middle + 1, last)
#
#
# my_array = [int(x) for x in input().split()]
# length = len(my_array)
# element = int(input())
#
# print(find_element_first(my_array, element, 0, length - 1))
