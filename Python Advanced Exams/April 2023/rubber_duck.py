from collections import deque


durations_sequence = deque(int(x) for x in input().split(" "))
tasks_sequence = deque(int(x) for x in input().split(" "))

duckies = {
    "Darth Vader Ducky": [set(range(0, 61)), 0],
    "Thor Ducky": [set(range(61, 121)), 0],
    "Big Blue Rubber Ducky": [set(range(121, 181)), 0],
    "Small Yellow Rubber Ducky": [set(range(181, 241)), 0]
}

while durations_sequence and tasks_sequence:
    duration = durations_sequence.popleft()
    number_tasks = tasks_sequence.pop()
    product = duration * number_tasks

    if product > 240:
        tasks_sequence.append(number_tasks - 2)
        durations_sequence.append(duration)
        continue

    for ducky in duckies:
        if {product}.issubset(duckies[ducky][0]):
            duckies[ducky][1] += 1
            break

print("Congratulations, all tasks have been completed! Rubber ducks rewarded:")
for duck_info in duckies:
    print(f"{duck_info}: {duckies[duck_info][1]}")
