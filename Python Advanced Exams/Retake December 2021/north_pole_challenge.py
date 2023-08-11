def move_player(position, move, steps):
    global collected_all
    workshop[position[0]][position[1]] = "x"
    new = []

    for i in range(steps):
        r = position[0] + directions[move][0]
        c = position[1] + directions[move][1]
        new = [r % rows if r != 0 else 0, c % columns if c != 0 else 0]
        item = workshop[new[0]][new[1]]

        if item == "D":
            items["Christmas decorations"][1] += 1
        elif item == "G":
            items["Gifts"][1] += 1
        elif item == "C":
            items["Cookies"][1] += 1

        workshop[new[0]][new[1]] = "x" if i < steps - 1 else "Y"
        position = new

        if all(ele[1][1] - ele[1][0] == 0 for ele in items.items()):
            collected_all = True
            workshop[new[0]][new[1]] = "Y"
            return

    return new


[rows, columns] = [int(x) for x in input().split(", ")]
items = {
    "Christmas decorations": [0, 0],
    "Gifts": [0, 0],
    "Cookies": [0, 0],
}

directions = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1]
}

workshop, my_position = [], []
for row in range(rows):
    line = input().split(" ")

    if "Y" in line:
        my_position = [row, line.index("Y")]

    items["Christmas decorations"][0] += line.count("D")
    items["Gifts"][0] += line.count("G")
    items["Cookies"][0] += line.count("C")

    workshop.append(line)

collected_all = False
while True:
    line = input().split("-")

    if line[0] == "End":
        break

    movement, step_no = line[0], int(line[1])
    my_position = move_player(my_position, movement, step_no)

    if collected_all:
        print("Merry Christmas!")
        break

print("You've collected:")
for item in items:
    print(f"- {items[item][1]} {item}")
[print(f"{' '.join(x for x in line)}") for line in workshop]
