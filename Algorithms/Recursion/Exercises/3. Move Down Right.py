# Lecturer`s solution
# result is immutable type, but it locally accumulates its value and returns it to the parent call
def count_all_paths(row, col, rows, cols):
    if col >= cols or row >= rows: # Since allowed directions are only right and down
        return 0 # no path
    if col == cols - 1 or row == rows - 1:
        return 1 # path found

    result = 0
    result += count_all_paths(row, col + 1, rows, cols) # Right
    result += count_all_paths(row + 1, col, rows, cols) # Left

    return result

rows = int(input())
cols = int(input())

print(count_all_paths(0, 0, rows, cols))

# def find_number_of_paths(row, col, matrix, direction, path, paths):
#     matrix[rows - 1][cols - 1] = 'e'
#
#     if col < 0 or row < 0 or col >= cols or row >= rows:
#         return
#     if matrix[row][col] == 'v':
#         return
#
#     path.append(direction)
#
#     if matrix[row][col] == 'e':
#         paths.append(path)
#     else:
#         matrix[row][col] = 'v'
#
#         find_number_of_paths(row, col + 1, matrix, 'R', path, paths)
#         find_number_of_paths(row + 1, col, matrix, 'D', path, paths)
#
#         matrix[row][col] = None
#
#     path.pop()
#
# rows = int(input())
# cols = int(input())
# labyrinth = [[None] * cols for _ in range(rows)]
# ways = []
#
# find_number_of_paths(0, 0, labyrinth, '', [], ways)
# print(len(ways))
