def shopping_list(budget, **products):
    bag = set()
    bought = []

    if budget < 100:
        return "You do not have enough budget."

    for product in products:
        price, quantity = products[product][0], products[product][1]
        cost = price * quantity

        if budget >= cost:
            bought.append(f"You bought {product} for {cost:.2f} leva.")
            bag.add(product)
            budget -= cost

        if len(bag) == 5:
            break

    return '\n'.join(line for line in bought)
