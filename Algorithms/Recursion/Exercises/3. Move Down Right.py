def find_number_of_paths(row, col, matrix, direction, path, paths):
    matrix[rows - 1][cols - 1] = 'e'

    if col < 0 or row < 0 or col >= cols or row >= rows:
        return
    if matrix[row][col] == 'v':
        return

    path.append(direction)

    if matrix[row][col] == 'e':
        paths.append(path)
    else:
        matrix[row][col] = 'v'

        find_number_of_paths(row, col + 1, matrix, 'R', path, paths)
        find_number_of_paths(row + 1, col, matrix, 'D', path, paths)

        matrix[row][col] = None

    path.pop()

rows = int(input())
cols = int(input())
labyrinth = [[None] * cols for _ in range(rows)]
ways = []

find_number_of_paths(0, 0, labyrinth, '', [], ways)
print(len(ways))
