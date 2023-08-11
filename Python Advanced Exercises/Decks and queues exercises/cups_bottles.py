from collections import deque

cups = deque(map(int, input().split(" ")))
bottles = deque(map(int, input(). split(" ")))

water_wasted = 0
while cups:
    current_bottle = bottles.pop()
    current_cup = cups.popleft()

    if current_bottle >= current_cup:
        added = current_cup
        water_wasted += current_bottle - added
    else:
        added = current_bottle
        current_cup -= added
        cups.appendleft(current_cup)

    if not bottles:
        break

if not cups:
    print("Bottles: ", end="")
    while len(bottles) > 0:
        bottle = bottles.popleft()
        if len(bottles) == 0:
            print(f"{bottle}")
        else:
            print(f"{bottle}", end=' ')

else:
    print("Cups: ", end="")
    while len(cups) > 0:
        cup = cups.popleft()
        if len(cups) == 0:
            print(f"{cup}")
        else:
            print(f"{cup}", end=' ')

print(f"Wasted litters of water: {water_wasted}")
