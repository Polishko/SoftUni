from collections import deque


def stock_availability(arg, *args):
    inventory = deque(arg)

    if args[0] == "delivery":
        for item in args[1:]:
            inventory.append(item)

    elif args[0] == "sell":
        if len(args) == 1:
            if inventory:
                inventory.popleft()
            return list(inventory)

        elif type(args[1]) == int:
            for _ in range(args[1]):
                if inventory:
                    inventory.popleft()
        else:
            for item in args[1:]:
                for i in range(len(inventory) - 1, -1, -1):
                    if inventory[i] == item:
                        del inventory[i]

    return list(inventory)
