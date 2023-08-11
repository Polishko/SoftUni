quantity = int(input())
days = int(input())
ornament_price = 2
ornament_spirit = 5
tree_skirt_price = 5
tree_skirt_spirit = 3
tree_garland_price = 3
tree_garland_spirit = 10
tree_lights_price = 15
tree_lights_spirit = 17
total_cost = 0
spirit_points = 0

for day in range(1, days + 1):
    if day % 11 == 0:
        quantity += 2
    if day % 2 == 0:
        total_cost += quantity * ornament_price
        spirit_points += ornament_spirit
    if day % 3 == 0:
        total_cost += quantity * (tree_skirt_price + tree_garland_price)
        spirit_points += tree_skirt_spirit + tree_garland_spirit
    if day % 5 == 0:
        total_cost += quantity * tree_lights_price
        spirit_points += tree_lights_spirit
    if day % 10 == 0:
        spirit_points -= 20
        total_cost += 23
    if day % 15 == 0:
        spirit_points += 30
    if day == days and day % 10 == 0:
        spirit_points -= 30

print(f"Total cost: {total_cost}\nTotal spirit: {spirit_points}")
