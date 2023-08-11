def take_position(a):
    arg_1, arg_2 = a.strip("()").split(", ")
    return [int(arg_1), int(arg_2)]
    
    # part_1, part_2 = a.split(",")
    # r = int(part_1[1:])
    # c = int(part_2[1:len(part_2) - 1])
    # return [r, c]


def find_mines(pos):
    check_positions = set((r + pos[0], c + pos[1]) for r in range(-1, 2) for c in range(-1, 2))
    valid_positions = check_positions.intersection(field_positions)
    return [field[pos[0]][pos[1]] for pos in valid_positions].count("*")


size = int(input())
bomb_count = int(input())
field = [[0] * size for row in range(size)]
field_positions = set([(x, y) for x in range(size) for y in range(size)])

for _ in range(bomb_count):
    position = take_position(input())
    field[position[0]][position[1]] = "*"

for row in range(size):
    for col in range(size):
        if field[row][col] != "*":
            field[row][col] = find_mines([row, col])

[print(f"{' '.join(str(x) for x in row)}") for row in field]
