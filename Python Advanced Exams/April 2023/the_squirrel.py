directions = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1]
}

size = int(input())
movements = [move for move in input().split(", ")]
field = [[x for x in list(input())] for row in range(size)]
field_positions = set([(x, y) for x in range(size) for y in range(size)])
squirrel = [(x, y) for x in range(size) for y in range(size) if field[x][y] == "s"][0]

hazelnuts = 0
for move in movements:
    new = (squirrel[0] + directions[move][0], squirrel[1] + directions[move][1])

    if not {new}.issubset(field_positions):
        print("The squirrel is out of the field.")
        break

    if field[new[0]][new[1]] == "t":
        print("Unfortunately, the squirrel stepped on a trap...")
        break
    elif field[new[0]][new[1]] == "h":
        hazelnuts += 1
        field[new[0]][new[1]] = "*"

    if hazelnuts == 3:
        print("Good job! You have collected all hazelnuts!")
        break

    squirrel = new

else:
    print("There are more hazelnuts to collect.")

print(f"Hazelnuts collected: {hazelnuts}")
