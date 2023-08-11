from collections import deque


seats = input().split(", ")
num_set1 = deque(int(x) for x in input().split(", "))
num_set2 = deque(int(x) for x in input().split(", "))

rotations = 0
unique_seats = []

while True:
    if len(unique_seats) == 3 or rotations == 10:
        break

    num_1 = num_set1.popleft()
    num_2 = num_set2.pop()
    check_1 = str(num_1) + chr(num_1 + num_2)
    check_2 = str(num_2) + chr(num_1 + num_2)

    if check_1 in seats and check_1 not in unique_seats:
        unique_seats.append(check_1)
    elif check_2 in seats and check_2 not in unique_seats:
        unique_seats.append(check_2)
    else:
        num_set1.append(num_1)
        num_set2.appendleft(num_2)

    rotations += 1

print(f"Seat matches: {', '.join(list(unique_seats))}")
print(f"Rotations count: {rotations}")
