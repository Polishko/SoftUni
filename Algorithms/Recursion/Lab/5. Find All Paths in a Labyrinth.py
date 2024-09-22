def find_all_paths(row, col, labyrinth, direction, path):

    if col < 0 or row < 0 or col >= columns or row >= rows:
        return
    if labyrinth[row][col] == '*':
        return
    if labyrinth[row][col] == 'v':
        return

    path.append(direction) # append before checking for e if you want to print the last move leading to e

    if labyrinth[row][col] == 'e':
        print(' '.join(path))
    else:
        labyrinth[row][col] = 'v'

        # explore all routes from a given point
        find_all_paths(row, col + 1, labyrinth, 'R', path)
        find_all_paths(row + 1, col, labyrinth, 'D', path)
        find_all_paths(row - 1, col, labyrinth, 'U', path)
        find_all_paths(row, col - 1, labyrinth, 'L', path)
        # when done with the point unmark visited so that the route is open for visiting from another point
        # that awaits exploration in the stack
        labyrinth[row][col] = '-'

    # remove last move from path when you go a step back
    path.pop()

rows = int(input())
columns = int(input())
labyrinth = [list(input()) for r in range(rows)]

find_all_paths(0, 0, labyrinth, '', [])