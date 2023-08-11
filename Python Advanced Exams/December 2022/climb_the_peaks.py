from collections import deque


food_pack = deque(int(x) for x in input().split(", "))
stamina_pack = deque(int(x) for x in input().split(", "))

peaks = deque([["Vihren", 80], ["Kutelo", 90], ["Banski Suhodol", 100], ["Polezhan", 60], ["Kamenitza", 70]])
conquered = []
days = 0

while food_pack and stamina_pack and peaks:
    food = food_pack.pop()
    stamina = stamina_pack.popleft()
    peak = peaks[0]

    if food + stamina < peak[1]:
        continue

    conquered.append(peak[0])
    peaks.popleft()
    days += 1

    if days == 7:
        break

if len(conquered) == 5:
    print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
else:
    print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")

if conquered:
    print("Conquered peaks:")
    print(*conquered, sep="\n")
