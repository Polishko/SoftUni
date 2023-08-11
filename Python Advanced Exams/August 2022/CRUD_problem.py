SIZE = 6

matrix = [[x for x in input().split(" ")] for row in range(SIZE)]
x, y = input().strip("()").split(", ")
position = [int(x), int(y)]

movements = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1]
}

while True:
    tokens = input().split(", ")

    if tokens[0] == "Stop":
        break

    new = [position[0] + movements[tokens[1]][0], position[1] + movements[tokens[1]][1]]

    if tokens[0] == "Create":
        if matrix[new[0]][new[1]] == ".":
            matrix[new[0]][new[1]] = tokens[2]
    elif tokens[0] == "Update":
        if matrix[new[0]][new[1]] != ".":
            matrix[new[0]][new[1]] = tokens[2]
    elif tokens[0] == "Delete":
        if matrix[new[0]][new[1]] != ".":
            matrix[new[0]][new[1]] = "."
    else:
        if matrix[new[0]][new[1]] != ".":
            print(matrix[new[0]][new[1]])

    position = new

[print(f"{' '.join(row)}") for row in matrix]
