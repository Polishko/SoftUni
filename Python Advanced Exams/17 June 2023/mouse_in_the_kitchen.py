[rows, cols] = [int(x) for x in input().split(",")]

field, mouse = [], []
cheese = 0
for row in range(rows):
    line = list(input())

    if "M" in line:
        mouse = [row, line.index("M")]

    cheese += line.count("C")
    field.append(line)

field_positions = set((x, y) for x in range(rows) for y in range(cols))
directions = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1]
}

while True:
    command = input()

    if command == "danger":
        field[mouse[0]][mouse[1]] = "M"
        print("Mouse will come back later!")
        break

    new = [mouse[0] + directions[command][0], mouse[1] + directions[command][1]]
    field[mouse[0]][mouse[1]] = "*"

    if not {(new[0], new[1])}.issubset(field_positions):
        field[mouse[0]][mouse[1]] = "M"
        print("No more cheese for tonight!")
        break

    if field[new[0]][new[1]] == "@":
        continue

    elif field[new[0]][new[1]] == "T":
        field[new[0]][new[1]] = "M"
        print("Mouse is trapped!")
        break

    elif field[new[0]][new[1]] == "C":
        cheese -= 1
        field[new[0]][new[1]] = "*"

        if cheese == 0:
            field[new[0]][new[1]] = "M"
            print("Happy mouse! All the cheese is eaten, good night!")
            break

    mouse = new

[print(f"{''.join(row)}") for row in field]
