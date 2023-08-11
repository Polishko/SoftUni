size = int(input())
bunny = [0, 0]

matrix = []
for r in range(size):
    line = input().split()

    if "B" in line:
        bunny = [r, line.index("B")]

    matrix.append(line)

up_side = [matrix[r][0] for r in range(bunny[0] - 1, 0, -1) if bunny[0] != 0]
down_side = [matrix[r] for r in range(bunny[0 + 1], size)]

# left_string, right_string = matrix[bunny[0]].split("X")
# up_string, down_string = inverted_matrix[bunny[1]].split("X")
#
# eggs = {"up": 0, "down": 0, "left": 0, "right": 0}
# positions = {"up": [], "down": [], "left": [], "right": []}
