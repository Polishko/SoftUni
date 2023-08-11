num = int(input())

for ord_1 in range(97, 97 + num):
    for ord_2 in range(97, 97 + num):
        for ord_3 in range(97, 97 + num):
            print(f"{chr(ord_1)}{chr(ord_2)}{chr(ord_3)}")

# 97 yerine start = 97 dedi;  ayni sey fark etmiyor, sadece baslangicin degismesi ihtimaline karsi iyi bir uygulama, \
# tum kodu degistirmek gerekmez
