num_dragons = int(input())
all_dragons = {}

for _ in range(1, num_dragons + 1):
    arg_1, arg_2, arg_3, arg_4, arg_5 = input().split(" ")
    dragon_type, dragon_name = arg_1, arg_2

    if arg_3.isdigit():
        damage = int(arg_3)
    else:
        damage = 45

    if arg_4.isdigit():
        health = int(arg_4)
    else:
        health = 250

    if arg_5.isdigit():
        armor = int(arg_5)
    else:
        armor = 10

    if dragon_type not in all_dragons:
        all_dragons[dragon_type] = [(dragon_name, damage, health, armor)]
    else:
        for item in all_dragons[dragon_type]:
            if item[0] == dragon_name:
                idx_item = all_dragons[dragon_type].index(item)
                all_dragons[dragon_type][idx_item] = (dragon_name, damage, health, armor)
                break
        else:
            all_dragons[dragon_type].append((dragon_name, damage, health, armor))

for key, value in all_dragons.items():
    value.sort()

    ave_damage = sum(i[1] for i in value)/len(value)
    ave_health = sum(i[2] for i in value)/len(value)
    ave_armour = sum(i[3] for i in value)/len(value)
    print(f"{key}::({ave_damage:.2f}/{ave_health:.2f}/{ave_armour:.2f})")

    for i in value:
        print(f"-{i[0]} -> damage: {i[1]}, health: {i[2]}, armor: {i[3]}")
