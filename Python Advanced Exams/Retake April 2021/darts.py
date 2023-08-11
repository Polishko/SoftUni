from collections import deque


SIZE = 7
player_1, player_2 = input().split(", ")
players = deque([[player_1, 501, 0], [player_2, 501, 0]])

field = [[int(x) if x[-1].isdigit() else x for x in input().split(" ")] for row in range(SIZE)]
field_points = set((x, y) for x in range(7) for y in range(7))

bulls_eye = False
while True:
    arg_1, arg_2 = input().strip("()").split(",")
    coordinates = (int(arg_1), int(arg_2))
    players[0][2] += 1

    if {coordinates}.issubset(field_points):
        target = field[coordinates[0]][coordinates[1]]

        to_reduce = 0
        if target == "B":
            bulls_eye = True
        elif type(target) == int:
            to_reduce = target
        elif target == "D":
            to_reduce = (field[coordinates[0]][0] + field[coordinates[0]][-1] + field[0][coordinates[1]]
                         + field[-1][coordinates[1]]) * 2
        elif target == "T":
            to_reduce = (field[coordinates[0]][0] + field[coordinates[0]][-1] + field[0][coordinates[1]]
                         + field[-1][coordinates[1]]) * 3

        players[0][1] -= to_reduce

        if bulls_eye or players[0][1] <= 0:
            print(f"{players[0][0]} won the game with {players[0][2]} throws!")
            break

    players.rotate(-1)
