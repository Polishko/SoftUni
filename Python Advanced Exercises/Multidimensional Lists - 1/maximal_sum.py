# rows, columns = [int(a) for a in input().split(" ")]
# matrix = [[int(num) for num in input().split(" ")] for x in range(rows)]
#
# matrices = []
#
# for row in range(rows - 2):
#
#     for column in range(columns - 2):
#         sub_matrix = []
#         sum_sub_matrix = 0
#
#         for i in range(3): # cok gereksiz bir cycle mı ki:)
#             current = matrix[row + i][column:column + 3]
#             sub_matrix.append(current)
#             sum_sub_matrix += sum(current)
#
#         matrices.append((sub_matrix, sum_sub_matrix))
#
# matrices.sort(key=lambda x: -x[1])
# print(f"Sum = {matrices[0][1]}")
# [print(f"{' '.join([str(a) for a in x])}") for x in matrices[0][0]]
#

rows, columns = [int(a) for a in input().split(" ")]
matrix = [[int(num) for num in input().split(" ")] for x in range(rows)]

target_matrix = []
max_sum = float("-inf")

for row in range(rows - 2):
    for column in range(columns - 2):

        row_1 = [matrix[row][column] for column in range(column, column + 3)]
        row_2 = [matrix[row + 1][column] for column in range(column, column + 3)]
        row_3 = [matrix[row + 2][column] for column in range(column, column + 3)]

        # row_1 = matrix[row][column:column + 3]
        # row_2 = matrix[row + 1][column: column + 3]
        # row_3 = matrix[row + 2][column:column + 3]
        # this is better because you just cut each row list as necessary instead of iterating in list comprehension

        current_matrix = [row_1, row_2, row_3]
        curr_sum = sum([sum(row) for row in current_matrix])

        if curr_sum > max_sum:
            max_sum = curr_sum
            target_matrix = current_matrix

print(f"Sum = {max_sum}")
[print(*row) for row in target_matrix]

