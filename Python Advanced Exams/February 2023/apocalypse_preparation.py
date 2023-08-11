from collections import deque


textiles = deque(int(x) for x in input().split(" "))
medicaments = deque(int(x) for x in input().split(" "))

items = {
    30: ["Patch", 0],
    40: ["Bandage", 0],
    100: ["MedKit", 0]
}

while medicaments and textiles:
    textile = textiles.popleft()
    medicament = medicaments.pop()
    total = textile + medicament

    if total in items:
        items[total][1] += 1
    elif total > 100:
        items[100][1] += 1
        medicaments.append(medicaments.pop() + total - 100)
    else:
        medicaments.append(medicament + 10)

if not medicaments and not textiles:
    print("Textiles and medicaments are both empty.")
elif not medicaments:
    print("Medicaments are empty.")
else:
    print("Textiles are empty.")

for item in sorted(items.items(), key=lambda x: (-x[1][1], x[1][0])):
    if item[1][1] != 0:
        print(f"{item[1][0]} - {item[1][1]}")

if medicaments:
    print(f"Medicaments left: {', '.join(str(x) for x in reversed(medicaments))}")
if textiles:
    print(f"Textiles left: {', '.join(str(x) for x in textiles)}")
