def is_valid_index(nums):
    return {nums[0], nums[2]}.issubset(range(rows)) and {nums[1], nums[3]}.issubset(range(columns))


rows, columns = [int(a) for a in input().split()]
matrix = [input().split() for _ in range(rows)]

while True:
    command, *indices = [int(x) if x.isdigit() else x for x in input().split()]

    if command == "END":
        break

    if not is_valid_index(indices) or command != "swap" or len(indices) != 4:
        print("Invalid input!")
    else:
        row_1, col_1, row_2, col_2 = indices
        matrix[row_1][col_1], matrix[row_2][col_2] = matrix[row_2][col_2], matrix[row_1][col_1]
        [print(" ".join(r)) for r in matrix]

# Dilyan
#
# def check_valid_indices(indices):
#     return {indices[0], indices[2]}.issubset(valid_rows) and {indices[1], indices[3]}.issubset(valid_cols)
#
#
# def swap_command(command, indices):
#     if check_valid_indices(indices) and command == "swap" and len(indices) == 4:
#         row1, col1, row2, col2 = indices
#
#         matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
#
#         print(*[' '.join(r) for r in matrix], sep="\n")
#     else:
#         print("Invalid input!")
#
#
# rows, cols = [int(x) for x in input().split()]
# matrix = [input().split() for _ in range(rows)]
#
# valid_rows = range(rows)
# valid_cols = range(cols)
#
# while True:
#     command_type, *info = [int(x) if x.isdigit() else x for x in input().split()]
#
#     if command_type == "END":
#         break
#
#     swap_command(command_type, info)