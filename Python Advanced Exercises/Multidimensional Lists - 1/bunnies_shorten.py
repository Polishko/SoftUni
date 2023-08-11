# Adapted from Dilyan's solution
def check_index(row, col):
    if row >= 0 and row < rows and col >= 0 and col < columns:
        return True


def find_player():
    for r in range(rows):
        if "P" in lair[r]:
            return r, lair[r].index("P")


def find_bunnies():
    positions = []

    for r in range(rows):
        for c in range(columns):
            if lair[r][c] == "B":
                positions.append([r, c])

    return positions


def bunny_moves(bunny_positions):
    for r, c in bunny_positions:
        for move in directions.values():
            new_r, new_c = move[0] + r, move[1] + c

            if check_index(new_r, new_c):
                lair[new_r][new_c] = "B"


def show_results(status="won"):
    [print(*r, sep="") for r in lair]
    print(f"{status}: {player_cur_r} {player_cur_c}")

    exit()


def check_if_dead(cur_r, cur_c):
    if lair[cur_r][cur_c] == "B":
        show_results("dead")


rows, columns = [int(a) for a in input().split()]
lair = [list(input()) for _ in range(rows)]

commands = input()

directions = {
    "U": [-1, 0],
    "D": [1, 0],
    "L": [0, -1],
    "R": [0, 1]
}

player_cur_r, player_cur_c = find_player()
lair[player_cur_r][player_cur_c] = "."

player_won = False
for command in commands:

    player_new_r, player_new_c = player_cur_r + directions[command][0], player_cur_c + directions[command][1]

    if check_index(player_new_r, player_new_c):
        player_cur_r, player_cur_c = player_new_r, player_new_c
    else:
        player_won = True

    bunny_moves(find_bunnies())

    if player_won:
        show_results()

    check_if_dead(player_cur_r, player_cur_c)
