from collections import deque


def find_new_position(position, action, r, c):
    if action == "U" and position[0] != 0:
        position[0] -= 1
    elif action == "D" and position[0] != r - 1:
        position[0] += 1
    elif action == "L" and position[1] != 0:
        position[1] -= 1
    elif action == "R" and position[1] != c - 1:
        position[1] += 1

    return position


rows, columns = [int(a) for a in input().split(" ")]
lair = []
player_current_position = [0, 0]
bunny_coordinates_list = set()

for row in range(rows):
    line = list(input())

    for i in range(len(line)):
        char = line[i]
        if char == "P":
            player_current_position = [row, line.index("P")]

        if char == "B":
            bunny_coordinates_list.add((row, i))

    lair.append(line)

movements = deque(input())
player_copy = player_current_position.copy()
player_won = False

while True:
    command = movements.popleft()
    bunnies_copy = deque(bunny_coordinates_list.copy())

    player_new_position = find_new_position(player_copy, command, rows, columns)
    lair[player_current_position[0]][player_current_position[1]] = "."

    while bunnies_copy:
        bunny = bunnies_copy.popleft()
        row_low_limit, row_high_limit = max(0, bunny[0] - 1), min(bunny[0] + 1, rows - 1)
        column_low_limit, column_high_limit = max(0, bunny[1] - 1), min(bunny[1] + 1, columns - 1)
        new_coordinates = [(row_low_limit, bunny[1]), (bunny[0], column_low_limit),
                           (bunny[0], bunny[1]), (bunny[0], column_high_limit), (row_high_limit, bunny[1])]

        bunny_coordinates_list.update(new_coordinates)

    for bunny in bunny_coordinates_list:
        r, c = bunny[0], bunny[1]
        lair[r][c] = "B"

    if (player_current_position[0], player_current_position[1]) == (player_new_position[0], player_new_position[1]):
        player_won = True
        break

    if lair[player_new_position[0]][player_new_position[1]] == "B":
        break

    for bunny in bunny_coordinates_list:
        if (player_new_position[0], player_new_position[1]) == bunny:
            break

    player_current_position = [player_new_position[0], player_new_position[1]]

    lair[player_current_position[0]][player_current_position[1]] = "P"

[print("".join(r)) for r in lair]
if player_won:
    print(f"won: {player_new_position[0]} {player_new_position[1]}")
else:
    print(f"dead: {player_new_position[0]} {player_new_position[1]}")
