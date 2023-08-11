size = int(input())


# matrix = [[int(x) if x.isdigit() else x for x in input().split()] for _ in range(size)]
# print(matrix)

matrix = []
bunny = [0, 0]
for r in range(size):
    line = input().split()

    if "B" in line:
        bunny = [r, line.index("B")]

    matrix.append(line)

r_u, r_d, c_l, c_r = bunny[0], bunny[0], bunny[1], bunny[1]
eggs = {}
positions = {"up": [], "down": [], "left": [], "right": []}

ele = ""
while r_u != 0:
    r_u -= 1
    ele = matrix[r_u][bunny[1]]

    if ele == "X":
        break

    eggs["up"] = eggs.get("up", 0) + int(ele)
    positions["up"].append([r_u, bunny[1]])


while r_d != size - 1:
    r_d += 1
    ele = matrix[r_d][bunny[1]]

    if ele == "X":
        break

    eggs["down"] = eggs.get("down", 0) + int(ele)
    positions["down"].append([r_d, bunny[1]])

while c_l != 0:
    c_l -= 1
    ele = matrix[bunny[0]][c_l]

    if ele == "X":
        break

    eggs["left"] = eggs.get("left", 0) + int(ele)
    positions["left"].append([bunny[0], c_l])

while c_r != size - 1:
    c_r += 1
    ele = matrix[bunny[0]][c_r]

    if ele == "X":
        break

    eggs["right"] = eggs.get("right", 0) + int(ele)
    positions["right"].append([bunny[0], c_r])

best_route = sorted(eggs.items(), key=lambda x: -x[1])[0]
direction, max_eggs = best_route[0], best_route[1]


print(direction)
print(*positions[direction], sep="\n")
print(max_eggs)
