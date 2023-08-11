player_results = {}
positions_by_player = {}
player_total_skills = {}

while True:
    line = input()

    if line == "Season end":
        break

    if "->" in line:
        arg_1, arg_2, arg_3 = line.split(" -> ")
        player, position, skill = arg_1, arg_2, int(arg_3)

        if player not in player_results:
            player_results[player] = {position: skill}
            positions_by_player[player] = [position]
            player_total_skills[player] = skill
        else:
            if position not in player_results[player]:
                player_results[player][position] = skill
                positions_by_player[player].append(position)
                player_total_skills[player] += skill
            else:
                current_skill = player_results[player][position]
                if skill > current_skill:
                    player_results[player][position] = skill
                    player_total_skills[player] = player_total_skills[player] - current_skill + skill
    else:
        player_1, player_2 = line.split(" vs ")
        if player_1 not in player_results or player_2 not in player_results:
            continue

        for position in positions_by_player[player_1]:
            if position in positions_by_player[player_2]:
                player_1_total = player_total_skills[player_1]
                player_2_total = player_total_skills[player_2]

                if player_1_total > player_2_total:
                    del player_results[player_2]
                    del positions_by_player[player_2]
                    del player_total_skills[player_2]
                elif player_2_total > player_1_total:
                    del player_results[player_1]
                    del positions_by_player[player_1]
                    del player_total_skills[player_1]
                break

first_sort = dict(sorted(player_total_skills.items()))
second_sort = dict(sorted(first_sort.items(), key=lambda item: -item[1]))

sorted_results = {}
for player in player_results:
    sort_1 = dict(sorted(player_results[player].items()))
    sort_2 = dict(sorted(sort_1.items(), key=lambda item: -item[1]))
    sorted_results[player] = sort_2

for player in second_sort:
    print(f"{player}: {second_sort[player]} skill")
    for position in sorted_results[player]:
        print(f"- {position} <::> {sorted_results[player][position]}")
