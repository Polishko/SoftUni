from collections import deque


materials = deque(int(num) for num in input().split())
magic_levels = deque([int(num) for num in input().split()])

presents = {150: "Doll", 250: "Wooden train", 300: "Teddy bear", 400: "Bicycle"}
crafted_items = {}

while materials and magic_levels:
    box = materials.pop()
    level = magic_levels.popleft()
    total_magic_level = box * level
    present = presents.get(total_magic_level, False)

    if present:
        if present not in crafted_items:
            crafted_items[present] = 0

        crafted_items[present] += 1

    else:
        if total_magic_level < 0:
            materials.append(box + level)
        elif total_magic_level > 0:
            materials.append(box + 15)
        else:
            if box == 0 and level != 0:
                magic_levels.appendleft(level)
            if level == 0 and box != 0:
                materials.append(box)

if ("Doll" in crafted_items and "Train" in crafted_items)\
        or ("Teddy bear" in crafted_items and "Bicycle" in crafted_items):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    print(f"Materials left: ", end="")
    to_print = []

    while materials:
        to_print.append(materials.pop())

    print(f"{', '.join([str(num) for num in to_print])}")

if magic_levels:
    print(f"Magic left: ", end="")
    to_print = []

    while magic_levels:
        to_print.append(magic_levels.popleft())

    print(f"{', '.join([str(num) for num in to_print])}")

if crafted_items:
    for item in sorted(crafted_items.items()):
        print(f"{item[0]}: {item[1]}")
