from collections import deque
MAX = 300


caffeine_seq = deque(int(x) for x in input().split(", "))
energy_seq = deque(int(x) for x in input().split(", "))

taken_caffeine = 0
while caffeine_seq and energy_seq:
    caffeine = caffeine_seq.pop()
    energy = energy_seq.popleft()
    drink_energy = caffeine * energy

    if drink_energy + taken_caffeine <= 300:
        taken_caffeine += drink_energy
    else:
        energy_seq.append(energy)
        taken_caffeine = max(0, taken_caffeine - 30)

if energy_seq:
    print(f"Drinks left: {', '.join(str(x) for x in energy_seq)}")
else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")

print(f"Stamat is going to sleep with {taken_caffeine} mg caffeine.")
