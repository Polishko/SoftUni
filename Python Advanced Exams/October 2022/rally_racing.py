size = int(input())
racing_number = input()

race_route, tunnel = [], [[], []]
tunnel_found = False

for row in range(size):
    line = input().split(" ")

    if not tunnel_found:
        for col in range(len(line)):
            char = line[col]
            if char == "T":
                if not tunnel[0] and not tunnel[1]:
                    tunnel = [[row, col], []]
                elif not tunnel[1]:
                    tunnel = [tunnel[0], [row, col]]
                    tunnel_found = True

    race_route.append(line)

directions = {
    "up": [-1, 0],
    "down": [1, 0],
    "left": [0, -1],
    "right": [0, 1]
}

position = [0, 0]
kilometers = 0
race_complete = False

while True:
    command = input()

    if command == "End":
        break

    new = [position[0] + directions[command][0], position[1] + directions[command][1]]
    km_to_add = 10

    if race_route[new[0]][new[1]] == "T":
        km_to_add = 30
        new = tunnel[1] if tunnel[0] == new else tunnel[0]
        race_route[tunnel[0][0]][tunnel[0][1]] = "."
        race_route[tunnel[1][0]][tunnel[1][1]] = "."

    kilometers += km_to_add
    position = new

    if race_route[new[0]][new[1]] == "F":
        print(f"Racing car {racing_number} finished the stage!")
        race_complete = True
        break

if not race_complete:
    print(f"Racing car {racing_number} DNF.")
print(f"Distance covered {kilometers} km.")

race_route[position[0]][position[1]] = "C"
[print(f"{''.join(row)}") for row in race_route]
