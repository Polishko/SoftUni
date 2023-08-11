from collections import deque


def move(position, command):
    field[position[0]][position[1]] = "-"

    if position[0] == 0 and command == "up":
        return [SIZE - 1, position[1]]
    elif position[0] == SIZE - 1 and command == "down":
        return [0, position[1]]
    elif position[1] == 0 and command == "left":
        return [position[0], SIZE - 1]
    elif position[1] == SIZE - 1 and command == "right":
        return [position[0], 0]
    else:
        return [position[0] + directions[command][0], position[1] + directions[command][1]]


SIZE = 6
field, rover_position = [], []

for i in range(SIZE):
    line = [x for x in input().split(" ")]

    if "E" in line:
        rover_position = [i, line.index("E")]

    field.append(line)

directions = {"up": [-1, 0],
              "down": [1, 0],
              "left": [0, -1],
              "right": [0, 1]
              }

movements = deque(input().split(", "))
deposits = {"W": "Water", "C": "Concrete", "M": "Metal"}
found = set()

while movements:
    movement = movements.popleft()

    new_position = move(rover_position, movement)
    current = field[new_position[0]][new_position[1]]

    if current in deposits:
        found.add(current)
        print(f"{deposits[current]} deposit found at ({new_position[0]}, {new_position[1]})")

    elif current == "R":
        print(f"Rover got broken at ({new_position[0]}, {new_position[1]})")
        break

    field[new_position[0]][new_position[1]] = "E"
    rover_position = [new_position[0], new_position[1]]

if len(found) == 3:
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")
