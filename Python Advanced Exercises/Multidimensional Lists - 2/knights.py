from collections import deque


def available_moves(row, column, x):
    # dict move 1, 2.... [-2, 1], [-2, -1], [2, 1], [2, -1], [-1, 2], [1, 2], [-1, -2], [2, -1]
    # for range 2 times and set combinations?

    lst = deque([(row - 2, column + 1), (row - 2, column - 1), (row + 2, column + 1), (row + 2, column - 1),
           (row - 1, column + 2), (row + 1, column + 2), (row - 1, column - 2), (row + 1, column - 2)])

    for _ in range(len(lst)):
        item = lst.popleft()

        if item[0] in range(len(x)) and item[1] in range(len(x)):
            if x[item[0]][item[1]] == "K":
                lst.append(item)

    return lst


matrix = [list(input()) for a in range(int(input()))]

removed_k = 0
while len(matrix) != 0:
    k_with_moves = {}

    for r in range(len(matrix)):
        line = matrix[r]

        for c in range(len(matrix[r])):
            char = line[c]

            if char == "K":
                k_with_moves[(r, c)] = len(available_moves(r, c, matrix))

    sorted_k = sorted(k_with_moves.items(), key=lambda k: -k[1])
    k_with_max_moves, max_moves = sorted_k[0][0], sorted_k[0][1]

    if max_moves == 0:
        break

    matrix[k_with_max_moves[0]][k_with_max_moves[1]] = "0"
    removed_k += 1

print(removed_k)
