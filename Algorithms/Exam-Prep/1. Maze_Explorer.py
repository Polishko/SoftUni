# Initial solution
def find_shortest_path(row, col, steps, current_step, matrix, direction):
    # Out of bounds or hit a wall, stop exploring
    if row < 0 or row >= n or col < 0 or col >= n or matrix[row][col] == '#':
        return

    # Destination reached: record steps
    if matrix[row][col] == 'E':
        steps[0] = min(current_step, steps[0])
        return

    # If visited, stop exploring
    if matrix[row][col] == 'v':
        return

    # Mark visited
    original_value = matrix[row][col]
    matrix[row][col] = 'v'

    # Explore all four possible directions
    find_shortest_path(row + 1, col, steps, current_step + 1, matrix, 'D')
    find_shortest_path(row - 1, col, steps, current_step + 1, matrix, 'U')
    find_shortest_path(row, col + 1, steps, current_step + 1, matrix, 'R')
    find_shortest_path(row, col - 1, steps, current_step + 1, matrix, 'L')

    # Backtrack: Unmark the cell
    matrix[row][col] = original_value


n = int(input())
matrix = [list(input()) for _ in range(n)]

steps = [float('inf')]
current_step = 0


find_shortest_path(0, 0, steps, current_step, matrix, '')
print(steps[0])
