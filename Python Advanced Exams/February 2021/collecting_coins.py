from math import floor


def find_new_position(position, movement):
    field[player_position[0]][player_position[1]] = 0
    return [(position[0] + directions[movement][0]) % size, (position[1] + directions[movement][1]) % size]


size = int(input())
field, player_position = [], []

directions = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1]
    }

for row in range(size):
    line = [int(x) if x[-1].isdigit() else x for x in input().split(" ")]

    if "P" in line:
        player_position = [row, line.index("P")]

    field.append(line)

player_route = [player_position]
total_coins = 0

while True:
    command = input()
    if command not in directions:
        continue

    new_position = find_new_position(player_position, command)
    target = field[new_position[0]][new_position[1]]

    if target == "X":
        total_coins = floor(total_coins * 0.5)
        player_route.append(new_position)
        print(f"Game over! You've collected {total_coins} coins.")
        break

    total_coins += target
    field[new_position[0]][new_position[1]] = "P"
    player_position = new_position
    player_route.append(player_position)

    if total_coins >= 100:
        print(f"You won! You've collected {total_coins} coins.")
        break

print("Your path:")
print(*player_route, sep="\n")
