# size = int(input())
#
# matrix = []
# sum_primary = 0
# sum_secondary = 0
#
# for _ in range(size):
#     line = [int(num) for num in input().split()]
#     matrix.append(line)
#
# for row in range(size):
#     for column in range(size):
#
#         if column == row:
#             sum_primary += matrix[row][column]
#
#         if size - row - 1 == column:
#             sum_secondary += matrix[row][column]
#
# print(abs(sum_primary - sum_secondary))


size = int(input())
matrix = [[int(a) for a in input().split()] for r in range(size)]

primary = sum([matrix[row][row] for row in range(size)])
secondary = sum([matrix[row][size - row - 1] for row in range(size)])

print(abs(primary - secondary))


