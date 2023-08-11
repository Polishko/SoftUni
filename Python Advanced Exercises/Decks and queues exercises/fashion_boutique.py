box_clothes = list(map(int, input().split(" ")))
capacity = int(input())

current_sum = 0
racks_needed = 0

if len(box_clothes) != 1:
    while len(box_clothes) > 0:

        item = box_clothes.pop()
        current_sum += item

        if current_sum > capacity:
            current_sum = item
            racks_needed += 1
        elif current_sum == capacity:
            current_sum = 0
            racks_needed += 1

else:
    item = box_clothes.pop()
    current_sum += item

if current_sum != 0:
    racks_needed += 1

print(racks_needed)
