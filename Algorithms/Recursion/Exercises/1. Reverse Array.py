# Lecturer`s solution
def reverse_array(array, idx):
    if idx == len(array) // 2:
        print(' '.join(array))
        return

    swap_idx = len(array) - idx - 1
    array[idx], array[swap_idx] = array[swap_idx], array[idx]
    reverse_array(array, idx + 1)

reverse_array(input().split(), 0)

# def reverse_array(array, n=0):
#     if n == len(array):
#          return
#
#     reverse_array(array, n + 1)
#     print(array[n], end=' ')
#
# reverse_array(input().split())
