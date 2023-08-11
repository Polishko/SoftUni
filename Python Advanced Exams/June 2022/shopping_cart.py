def shopping_cart(*items):
    meals = {
        "Pizza": [set(), 4],
        "Soup": [set(), 3],
        "Dessert": [set(), 2]
    }

    result = []
    for item in items:
        if item == "Stop":
            if all([len(meals[meal][0]) == 0 for meal in meals]):
                return "No products in the cart!"

            sorted_meals = sorted(meals.items(), key=lambda x: (-len(x[1][0]), x[0]))
            for meal in sorted_meals:
                result.append(f"{meal[0]}:")
                for product in sorted(list(meal[1][0])):
                    result.append(f" - {product}")

            return "\n".join(result)

        meal, product = item[0], item[1]

        if len(meals[meal][0]) < meals[meal][1]:
            meals[meal][0].add(product)
