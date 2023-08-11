from collections import deque


def is_item_valid(a, type_a):
    item_found = False
    item = ""

    while not item_found and a:
        if type_a == "fire":
            item = a.popleft()
        else:
            item = a.pop()

        if item <= 0:
            item = ""
        else:
            item_found = True

    return item


firework_effects = deque(int(x) for x in input().split(", "))
explosive_powers = deque(int(x) for x in input().split(", "))
fireworks = {
    "Palm Fireworks": 0,
    "Willow Fireworks": 0,
    "Crossette Fireworks": 0,
}

all_fireworks_made = False
while firework_effects and explosive_powers:
    effect = is_item_valid(firework_effects, type_a="fire")
    power = is_item_valid(explosive_powers, type_a="power")

    if not effect or not power:
        if power:
            explosive_powers.append(power)
        elif effect:
            firework_effects.appendleft(effect)
        break

    sum_items = effect + power
    if sum_items % 15 == 0:
        fireworks["Crossette Fireworks"] += 1
    elif sum_items % 3 == 0:
        fireworks["Palm Fireworks"] += 1
    elif sum_items % 5 == 0:
        fireworks["Willow Fireworks"] += 1
    else:
        firework_effects.append(effect - 1)
        explosive_powers.append(power)

    if all([val >= 3 for val in fireworks.values()]):
        print("Congrats! You made the perfect firework show!")
        all_fireworks_made = True
        break

if not all_fireworks_made:
    print("Sorry. You can't make the perfect firework show.")

if firework_effects:
    print(f"Firework Effects left: {', '.join(str(x) for x in firework_effects)}")
if explosive_powers:
    print(f"Explosive Power left: {', '.join(str(x) for x in explosive_powers)}")

[print(f"{firework}: {fireworks[firework]}") for firework in fireworks]
