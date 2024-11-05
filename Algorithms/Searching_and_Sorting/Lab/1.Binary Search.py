def find_element_first(arr, ele, first, last):
    if first > last:
        return -1

    middle = (last - first) // 2 + first

    if ele == arr[middle]:
        return middle

    elif ele < arr[middle]:
        return find_element_first(arr, ele, first, middle - 1)
    else:
        return find_element_first(arr, ele, middle + 1, last)


my_array = [int(x) for x in input().split()]
length = len(my_array)
element = int(input())

print(find_element_first(my_array, element, 0, length - 1))
