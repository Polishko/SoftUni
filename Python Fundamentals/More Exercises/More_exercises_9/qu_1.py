import re

participants = input().split(", ")
pattern_1 = r"[^A-Za-z]+"
pattern_2 = r"[^0-9]+"

results = {}
while True:
    line = input()

    if line == "end of race":
        break

    name = re.sub(pattern_1, "", line)
    distance_str = re.sub(pattern_2, "", line)

    distance = 0
    for num in distance_str:
        distance += int(num)

    if name in participants:
        if name not in results:
            results[name] = 0
        results[name] += distance

results = dict(sorted(results.items(), key=lambda x: -x[1]))

count = 0
for participant in results:
    count += 1

    if count > 3:
        break

    if count == 1:
        print(f"1st place: {participant}")
    elif count == 2:
        print(f"2nd place: {participant}")
    else:
        print(f"3rd place: {participant}")
