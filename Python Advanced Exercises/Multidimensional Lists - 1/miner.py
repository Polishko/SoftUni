# optimize et

from collections import deque


def find_new_position(position, action, field_size):
    if action == "up" and position[0] != 0:
        position[0] -= 1
    elif action == "down" and position[0] != field_size - 1:
        position[0] += 1
    elif action == "left" and position[1] != 0:
        position[1] -= 1
    elif action == "right" and position[1] != field_size - 1:
        position[1] += 1

    return position


size = int(input())

if size == 0:
    exit()

movements = deque(input().split(" "))

field = []
miner_position = [0, 0]
total_coal = 0

for row in range(size):
    line = input().split(" ")

    if "s" in line:
        miner_position = [row, line.index("s")]

    total_coal += line.count("c")
    field.append(line)

collected = 0
while movements:
    command = movements.popleft()

    miner_position = find_new_position(miner_position, command, size)

    if field[miner_position[0]][miner_position[1]] == "e":
        print(f"Game over! ({miner_position[0]}, {miner_position[1]})")
        break

    if field[miner_position[0]][miner_position[1]] == "c":
        field[miner_position[0]][miner_position[1]] = "*"
        collected += 1

    if collected == total_coal and collected != 0:
        print(f"You collected all coal! ({miner_position[0]}, {miner_position[1]})")
        break

else:
    print(f"{total_coal - collected} pieces of coal left. ({miner_position[0]}, {miner_position[1]})")
