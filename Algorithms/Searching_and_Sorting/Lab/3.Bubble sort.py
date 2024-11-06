# lecturer`s solution
arr = [int(x) for x in input().split()]

is_sorted = False
counter = 0

while not is_sorted:
    is_sorted = True
    for idx in range(1, len(arr)):
        if arr[idx] < arr[idx - 1]:
            arr[idx - 1], arr[idx] = arr[idx], arr[idx - 1]
            is_sorted = False

print(*arr, sep=' ')


# arr = [int(x) for x in input().split()]
#
# for idx in range(len(arr) - 1):
#     for next_idx in range(len(arr) - idx - 1):
#         if arr[next_idx + 1] < arr[next_idx]:
#             arr[next_idx], arr[next_idx + 1] = arr[next_idx + 1], arr[next_idx]
#
# print(*arr, sep=' ')
