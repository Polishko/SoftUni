def quicksort(start, end, arr):
    if start >= end:
        return

    pivot = start
    left = start + 1
    right = end

    while left <= right:
        if arr[left] > arr[pivot] > arr[right]:
            arr[right], arr[left] = arr[left], arr[right]

        if arr[left] <= arr[pivot]:
            left += 1

        if arr[right] >= arr[pivot]:
            right -= 1

    arr[pivot], arr[right] = arr[right], arr[pivot]

    if right - 1 - start < end - left:
        quicksort(start, right - 1, arr)
        quicksort(left, end, arr)
    else:
        quicksort(left, end, arr)
        quicksort(start, right - 1, arr)


arr = [int(x) for x in input().split()]
quicksort(0, len(arr) - 1, arr)

print(*arr, sep=' ')
