SIZE = 6

player_1, player_2 = input().split(", ")
players = [[player_1, 0], [player_2, 0]]
maze = [[x for x in input().split(" ")] for row in range(SIZE)]

while True:
    x, y = input().strip("()").split(", ")
    point = maze[int(x)][int(y)]

    if players[0][1] == 1:
        players[0][1] = 0
        players[0], players[1] = players[1], players[0]
        continue

    if point == "E":
        print(f"{players[0][0]} found the Exit and wins the game!")
        break

    if point == "T":
        print(f"{players[0][0]} is out of the game! The winner is {players[1][0]}.")
        break

    if point == "W":
        print(f"{players[0][0]} hits a wall and needs to rest.")
        players[0][1] += 1

    players[0], players[1] = players[1], players[0]
