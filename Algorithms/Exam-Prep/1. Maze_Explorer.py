# bfs solution
from collections import deque

def bfs(matrix, start):
    end = None
    for i in range(n):
        line = matrix[i]
        if 'E' in line:
            j = line.index('E')
            end = (i, j)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    queue = deque([(start[0], start[1], 0)]) #(row, col, steps)
    visited = {(start)}

    while queue:
        row, col, steps = queue.popleft()

        if (row, col) == end:
            return steps

        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < n and 0 <= new_col < n and (new_row, new_col) not in visited:
                if matrix[new_row][new_col] != '#':
                    visited.add((new_row, new_col))
                    queue.append((new_row, new_col, steps + 1))

    return -1


n = int(input())
start = (0, 0)

matrix = [list(input()) for _ in range(n)]
print(bfs(matrix, start))


# Initial solution
# def find_shortest_path(row, col, steps, current_step, matrix, direction):
#     # Out of bounds or hit a wall, stop exploring
#     if row < 0 or row >= n or col < 0 or col >= n or matrix[row][col] == '#':
#         return
#
#     # Destination reached: record steps
#     if matrix[row][col] == 'E':
#         steps[0] = min(current_step, steps[0])
#         return
#
#     # If visited, stop exploring
#     if matrix[row][col] == 'v':
#         return
#
#     # Mark visited
#     original_value = matrix[row][col]
#     matrix[row][col] = 'v'
#
#     # Explore all four possible directions
#     find_shortest_path(row + 1, col, steps, current_step + 1, matrix, 'D')
#     find_shortest_path(row - 1, col, steps, current_step + 1, matrix, 'U')
#     find_shortest_path(row, col + 1, steps, current_step + 1, matrix, 'R')
#     find_shortest_path(row, col - 1, steps, current_step + 1, matrix, 'L')
#
#     # Backtrack: Unmark the cell
#     matrix[row][col] = original_value
#
#
# n = int(input())
# matrix = [list(input()) for _ in range(n)]
#
# steps = [float('inf')]
# current_step = 0
#
#
# find_shortest_path(0, 0, steps, current_step, matrix, '')
# print(steps[0])
