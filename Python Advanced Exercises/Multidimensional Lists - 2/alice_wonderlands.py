def is_valid_index(a, n):
    if a in range(n):
        return True
    return False


def is_rabbit_hole(r, c, m):
    if m[r][c] == "R":
        m[r][c] = "*"
        return True
    return False


size = int(input())
matrix, alice = [], []
movements = {"up": [-1, 0], "down": [1, 0], "left": [0, -1], "right": [0, 1]}

for r in range(size):
    line = [int(a) if a[-1].isdigit() else a for a in input().split()]

    if "A" in line:
        alice = [r, line.index("A")]

    matrix.append(line)

tea_bags = 0
while True:
    command = input()
    movement = movements[command]
    matrix[alice[0]][alice[1]] = "*"
    new_r, new_c = alice[0] + movement[0], alice[1] + movement[1]

    if not is_valid_index(new_r, size) or not is_valid_index(new_c, size) or is_rabbit_hole(new_r, new_c, matrix):
        print("Alice didn't make it to the tea party.")
        break

    alice = [new_r, new_c]

    if matrix[new_r][new_c] == "." or matrix[new_r][new_c] == "*":
        continue

    tea_bags += matrix[new_r][new_c]

    if tea_bags >= 10:
        matrix[new_r][new_c] = "*"
        print("She did it! She went to the party.")
        break

[print(*row) for row in matrix]
