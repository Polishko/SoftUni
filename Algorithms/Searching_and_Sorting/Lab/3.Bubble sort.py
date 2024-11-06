arr = [int(x) for x in input().split()]

for idx in range(len(arr) - 1):
    for next_idx in range(len(arr) - idx - 1):
        if arr[next_idx + 1] < arr[next_idx]:
            arr[next_idx], arr[next_idx + 1] = arr[next_idx + 1], arr[next_idx]

print(*arr, sep=' ')
