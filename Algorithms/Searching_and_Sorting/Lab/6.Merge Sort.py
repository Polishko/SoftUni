def merge_arrays(left, right):
    result = [None] * (len(right) + len(left))
    left_idx = 0
    right_idx = 0
    result_idx = 0

    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            result[result_idx] = left[left_idx]
            left_idx += 1

        else:
            result[result_idx] = right[right_idx]
            right_idx += 1

        result_idx += 1

    # if right finished add already sorted left to result
    while left_idx < len(left):
        result[result_idx] = left[left_idx]
        left_idx += 1
        result_idx += 1

    # if left finished add already sorted right to result
    while right_idx < len(right):
        result[result_idx] = right[right_idx]
        right_idx += 1
        result_idx += 1

    # return sorted array
    return result


def merge_sort(arr):
    if len(arr) == 1:
        return arr

    mid_idx = len(arr) // 2
    left = arr[: mid_idx]
    right = arr[mid_idx:]

    # return the result/sorted merged array so that it can be used
    return merge_arrays(merge_sort(left), merge_sort(right))

arr = [int(x) for x in input().split()]
sorted_arr = merge_sort(arr)

print(*sorted_arr, sep=' ')
