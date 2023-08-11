size = int(input())
field, position = [], []

for row in range(size):
    line = list(input())

    if "S" in line:
        position = [row, line.index("S")]

    field.append(line)

hits, cruises = 0, 0
directions = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1]
}

while True:
    command = input()
    new = [position[0] + directions[command][0], position[1] + directions[command][1]]
    field[position[0]][position[1]] = "-"
    position = new

    if field[new[0]][new[1]] == "*":
        hits += 1
        field[new[0]][new[1]] = "-"

        if hits == 3:
            print(f"Mission failed, U-9 disappeared! Last known coordinates [{position[0]}, {position[1]}]!")
            field[new[0]][new[1]] = "S"
            break

    elif field[new[0]][new[1]] == "C":
        cruises += 1
        field[new[0]][new[1]] = "-"

        if cruises == 3:
            print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
            field[new[0]][new[1]] = "S"
            break

[print(*row, sep="") for row in field]
