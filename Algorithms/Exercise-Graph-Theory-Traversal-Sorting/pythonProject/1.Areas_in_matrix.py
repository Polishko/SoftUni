def find_connected_areas(matrix, rows, columns):
    visited = [[False for _ in range(columns)] for _ in range(rows)]
    connected_areas = {}

    def dfs(row, col, letter):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        visited[row][col] = True

        for dc, dr in directions:
            new_row, new_col = row + dr, col + dc

            if (0 <= new_row < rows
                    and 0 <= new_col < columns
                    and visited[new_row][new_col] == False
                    and matrix[new_row][new_col] == letter
            ):
                dfs(new_row, new_col, letter)

    for row in range(rows):
        for col in range(columns):
            if not visited[row][col]:
                letter = matrix[row][col]
                if letter not in connected_areas:
                    connected_areas[letter] = 0
                connected_areas[letter] += 1
                dfs(row, col, letter)

    print(f'Areas: {sum(connected_areas.values())}')
    for letter, count in sorted(connected_areas.items()):
        print(f"Letter '{letter}' -> {count}")

rows = int(input())
columns = int(input())
matrix = [list(input()) for row in range(rows)]

find_connected_areas(matrix, rows, columns)
