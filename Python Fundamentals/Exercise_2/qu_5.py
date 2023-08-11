order_char_1 = int(input())
order_char_2 = int(input())

for order_no in range(order_char_1, order_char_2 + 1):
    print(f"{chr(order_no)} ", end="") # aslinda gerek yok f"", fnc yaz, end="" yeterli
