from decimal import Decimal
TICKET = 150
main_string = input()
initial_budget = Decimal(input())
budget = initial_budget

main_list = main_string.split("|")
price_list = []

for i in range(len(main_list)):
    item_string = main_list[i]
    item_list = item_string.split("->")

    if "Clothes" in item_list and not(50 >= Decimal(item_list[1]) > 0):
        continue
    elif "Shoes" in item_list and not(35 >= Decimal(item_list[1]) > 0):
        continue
    elif "Accessories" in item_list and not(20.50 >= Decimal(item_list[1]) > 0):
        continue

    price_list.append(item_list[1])

mark_up_rate = 1.40
sum_initial_prices = 0
sum_final_prices = 0

for k in range(len(price_list)):
    price = Decimal(price_list[k])

    if price > budget:
        continue

    budget -= price
    sum_initial_prices += price
    price *= Decimal(mark_up_rate)
    sum_final_prices += price
    print(f"{price:.2f}", end=" ")

print()
profit = sum_final_prices - sum_initial_prices
print(f"Profit: {profit:.2f}")

budget = initial_budget + profit

if budget >= TICKET:
    print("Hello, France!")
else:
    print("Not enough money.")
