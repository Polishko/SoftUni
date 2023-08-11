# bunda da iki ayri sozluk yapti biri urun fiyat oburu urun miktar; fiyatlari guncelledi miktarlari artirdi.
# listede ise iki indeks ayri tur sey sakliyor ve kafa karistirabilir

products = {}

while True:
    command = input()

    if command == "buy":
        break

    arg_1, arg_2, arg_3 = command.split(" ")
    name = arg_1
    price = float(arg_2)
    quantity = float(arg_3)

    if name not in products:
        products[name] = [0.0, 0.0]

    products[name][0] = price
    products[name][1] += quantity


for key, value in products.items():
    print(f"{key} -> {value[0] * value[1]:.2f}")
