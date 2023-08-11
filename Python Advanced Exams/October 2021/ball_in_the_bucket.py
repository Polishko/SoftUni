SIZE = 6

board = [[x if x.isalpha() else int(x) for x in input().split(" ")] for row in range(SIZE)]
board_positions = set((x, y) for x in range(SIZE) for y in range(SIZE))
total_points = 0

for _ in range(3):
    arg_1, arg_2 = input().strip("()").split(", ")
    coordinates = (int(arg_1), int(arg_2))

    if not {coordinates}.issubset(board_positions) or board[coordinates[0]][coordinates[1]] != "B":
        continue

    board[coordinates[0]][coordinates[1]] = 0
    total_points += sum([board[r][coordinates[1]] if board[r][coordinates[1]] != "B" else 0 for r in range(SIZE)])

if total_points < 100:
    print(f"Sorry! You need {100 - total_points} points more to win a prize.")
else:
    if total_points < 200:
        prize = "Football"
    elif total_points < 300:
        prize = "Teddy Bear"
    else:
        prize = "Lego Construction Set"

    print(f"Good job! You scored {total_points} points, and you've won {prize}.")
