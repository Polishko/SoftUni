# size = int(input())
#
# matrix = [[0] * size for i in range(size)]
#
# for i in range(size):
#     line = [int(num) for num in input().split(", ")]
#     for j in range(size):
#         matrix[i][j] = line[j]
#
# primary_diagonal = []
# secondary_diagonal = []
#
# for i in range(size):
#     num_prim = matrix[size - i - 1][size - i - 1]
#     num_sec = matrix[(size - i - 1)][-(size - i)]
#     secondary_diagonal.append(num_sec)
#     primary_diagonal.append(num_prim)
#
# secondary_diagonal.reverse()
# primary_diagonal.reverse()
#
# print(f"Primary diagonal: {', '.join([str(num) for num in primary_diagonal])}. Sum: {sum(primary_diagonal)}")
# print(f"Secondary diagonal: {', '.join([str(num) for num in secondary_diagonal])}. Sum: {sum(secondary_diagonal)}")


# size = int(input())
# matrix = [[int(num) for num in input().split(", ")] for x in range(size)]
#
# primary_diagonal = []
# secondary_diagonal = []
#
# for row in range(size):
#     for column in range(size):
#
#         if column == row:
#             primary_diagonal.append(matrix[row][column])
#         if size - row - 1 == column:
#             secondary_diagonal.append(matrix[row][column])
#
# print(f"Primary diagonal: {', '.join([str(num) for num in primary_diagonal])}. Sum: {sum(primary_diagonal)}")
# print(f"Secondary diagonal: {', '.join([str(num) for num in secondary_diagonal])}. Sum: {sum(secondary_diagonal)}")

# size = int(input())
# matrix = [[int(num) for num in input().split(", ")] for x in range(size)]
#
# primary_diagonal = []
# secondary_diagonal = []
#
# for row in range(size):
#     primary_diagonal.append(matrix[row][row])
#     secondary_diagonal.append(matrix[row][size - row - 1])
#
# print(f"Primary diagonal: {', '.join([str(num) for num in primary_diagonal])}. Sum: {sum(primary_diagonal)}")
# print(f"Secondary diagonal: {', '.join([str(num) for num in secondary_diagonal])}. Sum: {sum(secondary_diagonal)}")


size = int(input())
matrix = [[int(num) for num in input().split(", ")] for x in range(size)]

primary_diagonal = [matrix[row][row] for row in range(size)]
secondary_diagonal = [matrix[row][size - row - 1] for row in range(size)]

print(f"Primary diagonal: {', '.join([str(num) for num in primary_diagonal])}. Sum: {sum(primary_diagonal)}")
print(f"Secondary diagonal: {', '.join([str(num) for num in secondary_diagonal])}. Sum: {sum(secondary_diagonal)}")
