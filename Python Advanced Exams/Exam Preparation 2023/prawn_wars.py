# This solution applies to a board with even number of rows or columns
from math import ceil


SIZE = 8
board = []
pawn_positions = [[], []]
r = ["a", "b", "c", "d", "e", "f", "g", "h"]
c = [8, 7, 6, 5, 4, 3, 2, 1]

for row in range(SIZE):
    line = input().split(" ")

    if "b" in line:
        pawn_positions = [pawn_positions[0], [row, line.index("b")]]
    if "w" in line:
        pawn_positions = [[row, line.index("w")], pawn_positions[1]]

    board.append(line)

if abs(pawn_positions[0][1] - pawn_positions[1][1]) != 1 or pawn_positions[0][0] <= pawn_positions[1][0]:
    if abs(0 - pawn_positions[0][0]) <= abs(SIZE - 1 - pawn_positions[1][0]):
        print(f"Game over! White pawn is promoted to a queen at {r[pawn_positions[0][1]]}{c[0]}.")
    else:
        print(f"Game over! Black pawn is promoted to a queen at {r[pawn_positions[1][1]]}{c[SIZE - 1]}.")

else:
    diff_positions = pawn_positions[0][0] - pawn_positions[1][0] - 1
    capture = ceil(diff_positions / 2)

    if diff_positions % 2 == 0:
        print(f"Game over! White win, capture on {r[pawn_positions[1][1]]}{c[pawn_positions[1][0] + capture]}.")
    else:
        print(f"Game over! Black win, capture on {r[pawn_positions[0][1]]}{c[pawn_positions[0][0] - capture]}.")
