def find_new_position(position, movement):
    directions = {
        "up": [-1, 0],
        "down": [1, 0],
        "left": [0, -1],
        "right": [0, 1]
    }

    return [position[0] + directions[movement][0], position[1] + directions[movement][1]]


def is_valid_idx(position):
    field_range = set(range(size))
    return {position[0]}.issubset(field_range) and {position[1]}.issubset(field_range)


text = input()
size = int(input())
field, player_position = [], []

for row in range(size):
    line = list(input())

    if "P" in line:
        player_position = [row, line.index("P")]

    field.append(line)

for _ in range(int(input())):
    command = input()
    target_position = find_new_position(player_position, command)

    if not is_valid_idx(target_position):
        text = text[:-1]
        continue

    target = field[target_position[0]][target_position[1]]
    if target != "-":
        text += target

    field[player_position[0]][player_position[1]] = "-"
    field[target_position[0]][target_position[1]] = "P"
    player_position = target_position

print(text)
[print(f"{''.join(row)}") for row in field]
