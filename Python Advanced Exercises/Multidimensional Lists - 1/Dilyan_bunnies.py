def find_player_position():
    for row in range(rows):
        if "P" in matrix[row]:
            return row, matrix[row].index("P")


def check_valid_index(row, col, player=False):
    global wins

    if 0 <= row < rows and 0 <= col < cols:
        return True
    if player:
        wins = True


def check_player_alive(row, col):
    if matrix[row][col] == "B":
        show_results("dead")


def bunnies_positions():
    positions = []

    for row in range(rows):
        for col in range(cols):
            if matrix[row][col] == "B":
                positions.append([row, col])

    return positions


def bunnies_move(bunnies_pos):
    for row, col in bunnies_pos:
        for bunnie_move in directions.values():
            new_row, new_col = row + bunnie_move[0], col + bunnie_move[1]

            if check_valid_index(new_row, new_col):
                matrix[new_row][new_col] = "B"


def show_results(status="won"):
    [print(*row, sep="") for row in matrix]
    print(f"{status}: {player_row} {player_col}")

    raise SystemExit


rows, cols = [int(x) for x in input().split()]
matrix = [list(input()) for _ in range(rows)]

commands = input()

wins = False
directions = {
    "U": (-1, 0),
    "D": (1, 0),
    "L": (0, -1),
    "R": (0, 1),
}

player_row, player_col = find_player_position()
matrix[player_row][player_col] = '.'

for command in commands:
    player_movement_row, player_movement_col = player_row + directions[command][0], player_col + directions[command][1]

    if check_valid_index(player_movement_row, player_movement_col, True):
        player_row, player_col = player_movement_row, player_movement_col

    bunnies_move(bunnies_positions())

    if wins:
        show_results()

    check_player_alive(player_row, player_col)
