def move_snake(position, movement):
    movements = {
        "up": [-1, 0],
        "down": [1, 0],
        "left": [0, -1],
        "right": [0, 1]
    }

    return [position[0] + movements[movement][0], position[1] + movements[movement][1]]


def is_valid_position(position):
    return {position[0]}.issubset(set(range(size))) and {position[1]}.issubset(set(range(size)))


def lair_movement(position):
    new = lair[1] if position == lair[0] else lair[0]
    territory[new[0]][new[1]] = "S"
    return new


size = int(input())

territory, snake_position = [], []
lair = []

for row in range(size):
    line = list(input())

    if "S" in line:
        snake_position = [row, line.index("S")]
    if "B" in line:
        lair.append([row, line.index("B")])

    territory.append(line)

food_eaten = 0
while True:
    command = input()
    territory[snake_position[0]][snake_position[1]] = "."
    new_position = move_snake(snake_position, command)

    if not is_valid_position(new_position):
        print("Game over!")
        break

    if territory[new_position[0]][new_position[1]] == "*":
        territory[new_position[0]][new_position[1]] = "S"
        food_eaten += 1

    if food_eaten == 10:
        print("You won! You fed the snake.")
        break

    if territory[new_position[0]][new_position[1]] == "B":
        territory[new_position[0]][new_position[1]] = "."
        new_position = lair_movement(new_position)

    snake_position = new_position

print(f"Food eaten: {food_eaten}")
[print("".join(line)) for line in territory]
