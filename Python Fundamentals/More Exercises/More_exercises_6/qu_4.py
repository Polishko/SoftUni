dwarfs = {}

while True:
    line = input()

    if line == "Once upon a time":
        break

    arg_1, arg_2, arg_3 = line.split(" <:> ")
    name, color, physics = arg_1, arg_2, int(arg_3)

    if color not in dwarfs:
        dwarfs[color] = {name: physics}
    else:
        name_found = False
        if name in dwarfs[color]:
            name_found = True
            current_physics = dwarfs[color][name]
            if physics > current_physics:
                dwarfs[color][name] = physics
        if not name_found:
            dwarfs[color][name] = physics

check_list = []

for key, value in dwarfs.items():
    length = len(value)
    hat_color = key
    for dwarf, points in value.items():
        check_list.append((length, hat_color, dwarf, points))

check_list.sort(key=lambda a: (a[3], a[0]), reverse=True)
for item in check_list:
    print(f"({item[1]}) {item[2]} <-> {item[3]}")
