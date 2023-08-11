def is_index_valid(a, b):
    if 0 <= a < 5 and 0 <= b < 5:
        return True
    return False


def shoot_target(text, matrix, position, movements):
    new_r, new_c = movements[text][0] + position[0], movements[text][1] + position[1]

    while is_index_valid(new_r, new_c):

        if matrix[new_r][new_c] == "x":
            matrix[new_r][new_c] = "."
            return [new_r, new_c]
        new_r, new_c = new_r + movements[text][0], new_c + movements[text][1]

    return False


def movement(text, matrix, position, movements, steps):

    new_r, new_c = position[0], position[1]
    for _ in range(steps):
        new_r, new_c = movements[text][0] + new_r, movements[text][1] + new_c

    if is_index_valid(new_r, new_c) and matrix[new_r][new_c] == ".":
        matrix[position[0]][position[1]] = "."
        matrix[new_r][new_c] = "A"
        return [new_r, new_c]

    return position


my_matrix, my_position = [], []
total_targets = 0
directions = {"up": [-1, 0], "down": [1, 0], "left": [0, -1], "right": [0, 1]}
targets_shot = {"coordinates": [], "count": 0}

for r in range(5):
    line = input().split()

    if "A" in line:
        my_position = [r, line.index("A")]

    total_targets += line.count("x")

    my_matrix.append(line)


for _ in range(int(input())):
    tokens = input().split()

    if tokens[0] == "shoot":
        result = shoot_target(tokens[1], my_matrix, my_position, directions)

        if result:
            targets_shot["coordinates"].append(result)
            targets_shot["count"] = targets_shot.get("count", 0) + 1

        if targets_shot.get("count", 0) == total_targets:
            print(f"Training completed! All {total_targets} targets hit.")
            break

    elif tokens[0] == "move":
        my_position = movement(tokens[1], my_matrix, my_position, directions, int(tokens[2]))

else:
    print(f"Training not completed! {total_targets - targets_shot['count']} targets left.")

if len(targets_shot["coordinates"]) != 0:
    print(*targets_shot["coordinates"], sep="\n")
