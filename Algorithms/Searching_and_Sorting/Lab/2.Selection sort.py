# def select_sort(arr):
#     for idx in range(len(arr)):
#         for i in range(idx):
#             if arr[idx] < arr[i]:
#                 arr[idx], arr[i] = arr[i], arr[idx]
#
#
#     result = list(arr)
#     print (*result, sep=' ')
#
#
#
# arr = [int(x) for x in input().split()]
# select_sort(arr)
#
from array import array


def select_sort(arr, idx):
    if idx >= len(arr):
        print(*arr, sep=' ')
        return

    min_idx = idx
    for i in range(idx + 1, len(arr)):
        if arr[i] < arr[min_idx]:
            min_idx = i

    arr[idx], arr[min_idx] = arr[min_idx], arr[idx]

    select_sort(arr, idx + 1)


arr = [int(x) for x in input().split()]
select_sort(arr, 0)
