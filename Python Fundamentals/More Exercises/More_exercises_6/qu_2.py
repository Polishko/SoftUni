contest_results = {}
user_total_points = {}

while True:
    line = input()

    if "->" not in line:
        break

    arg_1, arg_2, arg_3 = line.split(" -> ")
    username, contest, points = arg_1, arg_2, int(arg_3)

    if contest not in contest_results:
        contest_results[contest] = {}

    if username not in user_total_points:
        contest_results[contest][username] = points
        user_total_points[username] = points
    else:
        if username not in contest_results[contest]:
            contest_results[contest][username] = points
            user_total_points[username] += points
        else:
            current_points = contest_results[contest][username]
            if points > current_points:
                contest_results[contest][username] = points
                user_total_points[username] = user_total_points[username] - current_points + points

for contest, results in contest_results.items():
    print(f"{contest}: {len(results)} participants")
    first_sort = dict(sorted(results.items()))
    second_sort = dict(sorted(first_sort.items(), key=lambda item: -item[1]))
    order = 0
    for user in second_sort:
        order += 1
        print(f"{order}. {user} <::> {second_sort[user]}")

print("Individual standings:")
sort_1 = dict(sorted(user_total_points.items()))
sort_2 = dict(sorted(sort_1.items(), key=lambda item: -item[1]))
order_user = 0
for user in sort_2:
    order_user += 1
    print(f"{order_user}. {user} -> {sort_2[user]}")
