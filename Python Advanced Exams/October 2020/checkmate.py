def check_capture(queen_pos, king_pos):
    r_q, r_k = queen_pos[0], king_pos[0]
    c_q, c_k = queen_pos[1], king_pos[1]
    r_min, r_max = min(r_q, r_k), max(r_q, r_k)
    c_min, c_max = min(c_q, c_k), max(c_q, c_k)

    if r_q == r_k:
        horizontal = board[r_q][c_min + 1:c_max]
        if all([x == "." for x in horizontal]):
            capturing.append([r_q, c_q])
    elif c_q == c_k:
        vertical = [board[r][c_q] for r in range(r_min + 1, r_max)]
        if all([x == "." for x in vertical]):
            capturing.append([r_q, c_q])
    elif r_q - c_q == r_k - c_k:
        dia_one = [board[r][c] for r in range(r_min + 1, r_max) for c in range(c_min + 1, c_max) if r - c == r_q - c_q]
        if all(x == "." for x in dia_one):
            capturing.append([r_q, c_q])
    elif r_q + c_q == r_k + c_k:
        dia_two = [board[r][c] for r in range(r_min + 1, r_max) for c in range(c_min + 1, c_max) if r + c == r_q + c_q]
        if all(x == "." for x in dia_two):
            capturing.append([r_q, c_q])


SIZE = 8

board, queens, capturing, king_position = [], [], [], []
king_found = False

for row in range(SIZE):
    line = input().split(" ")

    for i in range(len(line)):
        if line[i] == "Q":
            queens.append([row, i])

    if not king_found:
        if "K" in line:
            king_position = [row, line.index("K")]
            king_found = True

    board.append(line)

for queen in queens:
    check_capture(queen, king_position)

if capturing:
    print(*capturing, sep="\n")
else:
    print("The king is safe!")
