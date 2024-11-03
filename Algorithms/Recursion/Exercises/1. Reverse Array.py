
def reverse_array(array, n=0):
    if n == len(array):
         return

    reverse_array(array, n + 1)
    print(array[n], end=' ')

reverse_array(input().split())
