from collections import deque


def match_gift(value):
    for gift in presents_magic:
        if presents_magic[gift][0] <= value <= presents_magic[gift][1]:
            presents[gift] += 1
            break


materials = deque(int(x) for x in input().split(" "))
magic_values = deque(int(x) for x in input().split(" "))

presents_magic = {
    "Gemstone": [100, 199],
    "Porcelain Sculpture": [200, 299],
    "Gold": [300, 399],
    "Diamond Jewellery": [400, 499]
}

presents = {
    "Diamond Jewellery": 0,
    "Gemstone": 0,
    "Gold": 0,
    "Porcelain Sculpture": 0,
}

while materials and magic_values:
    material = materials.pop()
    magic = magic_values.popleft()

    product = material + magic

    if product < 100:
        if product % 2 == 0:
            product = 2 * material + 3 * magic
        else:
            product *= 2
    elif product > 499:
        product *= 0.5

    if product < 100 or product > 499:
        continue

    match_gift(product)

if (presents["Gemstone"] >= 1 and presents["Porcelain Sculpture"] >= 1) \
        or (presents["Gold"] >= 1 and presents["Diamond Jewellery"] >= 1):
        print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")

if materials:
    print(f"Materials left: {', '.join(str(x) for x in materials)}")
if magic_values:
    print(f"Magic left: {', '.join(str(x) for x in magic_values)}")


for present in presents:
    if presents[present] >= 1:
        print(f"{present}: {presents[present]}")
