
contest_passwords = {}
while True:
    line = input()

    if line == "end of contests":
        break

    contest, password = line.split(":")
    contest_passwords[contest] = password

user_contests = {}
while True:
    line = input()

    if line == "end of submissions":
        break

    arg_1, arg_2, arg_3, arg_4 = line.split("=>")
    check_contest, check_password, username, points = arg_1, arg_2, arg_3, int(arg_4)

    if check_contest in contest_passwords and check_password == contest_passwords[check_contest]:
        if username not in user_contests:
            user_contests[username] = {}

        if check_contest not in user_contests[username]:
            user_contests[username][check_contest] = 0

        current_points = user_contests[username][check_contest]
        user_contests[username][check_contest] = max(current_points, points)

best_user = ""
max_points = 0
for user, contest_result in user_contests.items():
    points = sum(contest_result.values())
    if points > max_points:
        max_points = points
        best_user = user

print(f"Best candidate is {best_user} with total {max_points} points.")
print("Ranking:")

sorted_results = dict(sorted(user_contests.items()))
for user, contest_result in sorted_results.items():
    print(f"{user}")
    sorted_contests = dict(sorted(contest_result.items(), key=lambda item: -item[1]))
    for area in sorted_contests:
        print(f"#  {area} -> {sorted_contests[area]}")
