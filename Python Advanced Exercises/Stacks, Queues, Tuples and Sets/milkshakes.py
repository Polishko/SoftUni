from collections import deque


def enough_ingredients(a, b):
    if a and b:
        return True
    return False


chocolate_bars = deque(int(num) for num in input().split(","))
milk_cups = deque(int(num) for num in input().split(","))

shakes = 0

while True: # tum break conditionlar burada
    if shakes == 5: # dolayisiyla bu kosullar disarida ilk print, 5 ise ilki else ikincisi
        print("Great! You made all the chocolate milkshakes needed!")
        break

    if not enough_ingredients(chocolate_bars, milk_cups):
        print("Not enough milkshakes.")
        break

    choco_bar = chocolate_bars.pop()
    cup = milk_cups.popleft()

    if choco_bar <= 0 and cup > 0: # ikisi de sifir ise basta sonra biri sonra oburu
        milk_cups.appendleft(cup)
        continue
    elif cup <= 0 and choco_bar > 0:
        chocolate_bars.append(choco_bar)
        continue
    elif choco_bar <= 0 and cup <= 0:
        continue

    if choco_bar == cup:
        shakes += 1
    else:
        choco_bar -= 5
        chocolate_bars.append(choco_bar) # -5 burada olabilir
        milk_cups.append(cup)

if chocolate_bars:
    print("Chocolate: ", end="") # bunu f strin join yaparsan chocolate olmadiginda bu string empty yani false bu yuzden
    print(*chocolate_bars, sep=", ") # or "empty" diye hemen yanina yazabilirsin
else:                                   # yani print(f"False or 'something'") yazdiginda something basiyor
    print("Chocolate: empty")

if milk_cups:
    print("Milk: ", end="")
    print(*milk_cups, sep=", ")
else:
    print("Milk: empty")
