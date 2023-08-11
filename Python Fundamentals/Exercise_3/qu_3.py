team_a = ["A-1", "A-2", "A-3", "A-4", "A-5", "A-6", "A-7", "A-8", "A-9", "A-10", "A-11"]
team_b = ["B-1", "B-2", "B-3", "B-4", "B-5", "B-6", "B-7", "B-8", "B-9", "B-10", "B-11"]
cards = input()
card_list = cards.split(" ")
count_a = 11
count_b = 11
a_team_lost = False

for card in card_list:
    if card in team_a:
        team_a.remove(card)
        count_a -= 1
    elif card in team_b:
        team_b.remove(card)
        count_b -= 1

    if len(team_a) < 7 or len(team_b) < 7:
        a_team_lost = True
        break

print(f"Team A - {count_a}; Team B - {count_b}")

if a_team_lost:
    print(f"Game was terminated")
