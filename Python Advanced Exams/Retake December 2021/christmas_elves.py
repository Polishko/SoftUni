from collections import deque


elves = deque(int(x) for x in input().split(" "))
boxes = deque(int(x) for x in input().split(" "))
total_energy, total_toys, taken_boxes = 0, 0, 0

while boxes and elves:
    elf = elves.popleft()

    if elf < 5:
        continue

    box = boxes.pop()
    box_energy = box
    taken_boxes += 1

    toys_to_make = 1
    if taken_boxes != 0 and taken_boxes % 3 == 0:
        box_energy *= 2
        toys_to_make = 2

    if elf >= box_energy:
        elf -= box_energy
        total_energy += box_energy
        if taken_boxes % 5 != 0:
            total_toys += toys_to_make
            elf += 1
    else:
        elf *= 2
        boxes.append(box)

    elves.append(elf)

print(f"Toys: {total_toys}")
print(f"Energy: {total_energy}")

if elves:
    print(f"Elves left: {', '.join(str(elf) for elf in elves)}")
if boxes:
    print(f"Boxes left: {', '.join(str(box) for box in boxes)}")
