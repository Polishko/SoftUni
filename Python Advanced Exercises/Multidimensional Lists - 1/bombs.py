# optimize et
from collections import deque


size = int(input())
matrix = [[int(a) for a in input().split()] for row in range(size)]
coordinates = deque([[int(x) for x in group.split(",")] for group in input().split()])

while coordinates:
    r, c = [int(b) for b in coordinates.popleft()]
    bomb_value = matrix[r][c]

    if bomb_value <= 0:
        continue

    matrix[r][c] = 0

    row_low_limit, row_high_limit = max(0, r - 1), min(r + 1, size - 1)
    column_low_limit, column_high_limit = max(0, c - 1), min(c + 1, size - 1)

    for row in range(row_low_limit, row_high_limit + 1):
        for column in range(column_low_limit, column_high_limit + 1):
            target_cell = matrix[row][column]

            if (row == r and column == c) or target_cell <= 0:
                continue

            matrix[row][column] -= bomb_value

active, active_sum = 0, 0
for r in matrix:
    active_cells = list(filter(lambda x: x > 0, r))
    active += len(active_cells)
    active_sum += sum(active_cells)

print(f"Alive cells: {active}")
print(f"Sum: {active_sum}")
[print(" ".join(str(x) for x in r)) for r in matrix]
