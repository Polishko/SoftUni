[rows, cols] = [int(x) for x in input().split(" ")]

field, position = [], []
for row in range(rows):
    line = input().split(" ")

    if "B" in line:
        position = [row, line.index("B")]

    field.append(line)

field_positions = [(x, y) for x in range(rows) for y in range(cols)]

directions = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1]
}

touched_players, movements = 0, 0
while True:
    command = input()

    if command == "Finish" or touched_players == 3:
        break

    new = [position[0] + directions[command][0], position[1] + directions[command][1]]
    if not {(new[0], new[1])}.issubset(set(field_positions)) or field[new[0]][new[1]] == "O":
        continue

    if field[new[0]][new[1]] == "P":
        touched_players += 1
        field[new[0]][new[1]] = "-"

    movements += 1
    position = new

print("Game over!")
print(f"Touched opponents: {touched_players} Moves made: {movements}")
