def select_sort(arr):
    for idx in range(len(arr)):
        for i in range(idx):
            if arr[idx] < arr[i]:
                arr[idx], arr[i] = arr[i], arr[idx]


    result = list(arr)
    print (*result, sep=' ')



arr = [int(x) for x in input().split()]
select_sort(arr)
