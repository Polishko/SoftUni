presents = int(input())
size = int(input())
neighbourhood, santa = [], []
directions = {
    "left": [0, -1],
    "right": [0, 1],
    "up": [-1, 0],
    "down": [1, 0]}


def is_index_valid(a, b):
    if 0 <= a < 5 and 0 <= b < 5:
        return True
    return False


def move_to_house(text, position):
    new_position = directions[text][0] + position[0], directions[text][1] + position[1]
    if is_index_valid(new_position[0], new_position[1]):
        position = new_position
    return position


nice_kids = 0
for r in range(size):
    line = input().split()

    if "S" in line:
        santa = [r, line.index("S")]

    if "V" in line: # alttaki yeter ifsiz
        nice_kids += line.count("V")

    neighbourhood.append(line)

nice_kids_waiting = nice_kids
while True:
    command = input()

    if command == "Christmas morning":
        break

    house = move_to_house(command, santa)
    in_the_house = neighbourhood[house[0]][house[1]]
    neighbourhood[house[0]][house[1]] = "S"
    neighbourhood[santa[0]][santa[1]] = "-"
    santa = [house[0], house[1]]

    if in_the_house == "V":
        nice_kids_waiting -= 1
        presents -= 1

    elif in_the_house == "C":
        house_locations = [move_to_house(direction, santa) for direction in directions]

        for location in house_locations:

            if neighbourhood[location[0]][location[1]] != "V" and neighbourhood[location[0]][location[1]] != "X":
                continue
            elif neighbourhood[location[0]][location[1]] == "V":
                nice_kids_waiting -= 1

            presents -= 1
            neighbourhood[location[0]][location[1]] = "-"

            if presents == 0:
                break

    if presents == 0:
        break

if presents == 0 and nice_kids_waiting > 0:
    print("Santa ran out of presents!")

[print(*line) for line in neighbourhood]

if nice_kids_waiting == 0:
    print(f"Good job, Santa! {nice_kids} happy nice kid/s.")
else:
    print(f"No presents for {nice_kids_waiting} nice kid/s.")
