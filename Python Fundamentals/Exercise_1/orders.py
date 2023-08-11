num_orders = int(input())
total_price = 0

for order in range(1, num_orders + 1):
    cap_price = float(input())
    days = int(input())
    caps_per_day = int(input())
    if cap_price < 0.01 or cap_price > 100.00 or days < 1 or days > 31 or caps_per_day < 1 or caps_per_day > 2000:
        continue  # ayri 3 if yazmak daha iyiymis daha anlasilir cunku, boyle okunakli degil
    coffee_price = caps_per_day * days * cap_price
    total_price += coffee_price
    print(f"The price for the coffee is: ${coffee_price:.2f}")

print(f"Total: ${total_price:.2f}")
