import re

pattern = r"%(?P<name>[A-Z][a-z]+)%([^\|\$\%\.]*)<(?P<product>[\w]+)>([^\|\$\%\.]*)\|" \
          r"(?P<count>[\d]+)\|([^\|\$\%\.]*)(?P<price>[1-9]+[.0-9]*)\$"

total_price = 0
while True:

    line = input()

    if line == "end of shift":
        break

    matches = re.finditer(pattern, line)

    for match in matches:
        name = match.group("name")
        product = match.group("product")
        count = int(match.group("count"))
        price = float(match.group("price"))
        current_price = count * price
        total_price += current_price
        print(f"{name}: {product} - {current_price:.2f}")

print(f"Total income: {total_price:.2f}")