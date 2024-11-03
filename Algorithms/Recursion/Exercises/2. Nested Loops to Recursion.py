# Lecturer`s solution

def nested_loops(idx, arr):
    if idx >= len(arr):
        print(*arr, sep = ' ')
        return

    for num in range(1, len(arr) + 1):
        arr[idx] = num
        nested_loops(idx + 1, arr)

n = int(input())
array = [None] * n
nested_loops(0, array)


# def find_iteration_variables(n, result):
#     if len(result) == n:
#         print(' '.join(str(x) for x in result))
#         return
#
#     for i in range(1, n + 1):
#         result.append(i)
#         find_iteration_variables(n, result)
#         result.pop()
#
#
# find_iteration_variables(int(input()), [])
