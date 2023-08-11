n = int(input())
string = []

for _ in range(1, n + 1):
    entered_input = input()
    string.append(entered_input)

count_open, count_closed = 0, 0 # bracket counts
closed_comes_first = False
open_balanced = False

while len(string) > 0:
    symbol = string.pop(0)
    if symbol == ")":
        count_closed += 1
        if count_closed == 1 and count_open == 0:
            closed_comes_first = True
        elif count_closed == 1 and count_open == 1:
            open_balanced = True
            count_open, count_closed = 0, 0
    if symbol == "(":
        count_open += 1

if open_balanced and not closed_comes_first:
    print("BALANCED")
else:
    print("UNBALANCED")
