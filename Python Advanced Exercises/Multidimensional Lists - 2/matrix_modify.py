# n = int(input())
# matrix = [[int(a) for a in input().split()] for line in range(n)]
#
# while True:
#     info = input().split()
#
#     if info[0] == "END":
#         break
#
#     x, y = int(info[1]), int(info[2])
#
#     if x not in range(n) or y not in range(n):
#         print("Invalid coordinates")
#         continue
#
#     if info[0] == "Add":
#         matrix[x][y] += int(info[3])
#     elif info[0] == "Subtract":
#         matrix[x][y] -= int(info[3])
#
# [print(" ".join(str(b) for b in a)) for a in matrix]

def check_index(indices):
    return {indices[0], indices[1]}.issubset(range(n))


def apply_operation(command, indices):
    global matrix

    if check_index(indices):
        row, col, value = indices
        matrix[row][col] = operations[command](matrix[row][col], value)
    else:
        print("Invalid coordinates")


n = int(input())
matrix = [[int(a) for a in input().split()] for line in range(n)]
operations = {"Add": lambda a, b: a + b, "Subtract": lambda a, b: a - b}

while True:
    info, *nums = [int(x) if x.isdigit() else x for x in input().split()]

    if info == "END":
        [print(*line, sep=" ") for line in matrix]
        break

    apply_operation(info, nums)
