def shop_from_grocery_list(arg_1, needed_items, *item_info):
    budget = int(arg_1)

    for item in item_info:
        if item[0] not in needed_items:
            continue
        if float(item[1]) > budget:
            break

        needed_items.remove(item[0])
        budget -= item[1]

    if not needed_items:
        return f"Shopping is successful. Remaining budget: {budget:.2f}."
    else:
        return f"You did not buy all the products. Missing products: {', '.join(needed_items)}."
