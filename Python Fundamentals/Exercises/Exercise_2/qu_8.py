group_size = int(input())
days_adventure = int(input())
gain = 0

for day in range(1, days_adventure + 1):

    if day % 15 == 0:
        group_size += 5
    if day % 10 == 0:
        group_size -= 2

    if day % 3 == 0:
        gain -= 3 * group_size
    if day % 5 == 0:
        gain += 20 * group_size
    if day % 15 == 0:
        gain -= 2 * group_size

    gain += 50 - 2 * group_size

gain_per_companion = int(gain / group_size)
print(f"{group_size} companions received {gain_per_companion} coins each.")
