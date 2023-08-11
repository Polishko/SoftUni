from collections import deque


box_clothes = deque([int(num) for num in input().split(" ")])
capacity = int(input())

current_capacity = capacity
racks = 1

while box_clothes:
    item = box_clothes[-1]

    if item > current_capacity:
        racks += 1
        current_capacity = capacity
    else:
        current_capacity -= item
        box_clothes.pop()

print(racks)
