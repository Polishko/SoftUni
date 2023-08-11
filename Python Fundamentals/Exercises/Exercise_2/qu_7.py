INITIAL_TANK_VOL = 255
left_volume = INITIAL_TANK_VOL
n = int(input())

for _ in range(1, n + 1):
    added_volume = int(input())

    if added_volume > left_volume:
        print(f"Insufficient capacity!")
        continue

    left_volume -= added_volume

print(f"{INITIAL_TANK_VOL - left_volume}")
