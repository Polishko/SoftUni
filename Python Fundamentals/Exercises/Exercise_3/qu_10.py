from decimal import Decimal
INITIAL_ENERGY = 100
INITIAL_COINS = 100
energy = Decimal(INITIAL_ENERGY)
coins = Decimal(INITIAL_COINS)
cannot_afford = False

events_string = input()
events_list = events_string.split("|")

for i in range(len(events_list)):
    single_event_str = events_list[i]
    single_event_list = single_event_str.split("-")
    energy_gain = 0
    earned_coins = 0

    if single_event_list[0] == "rest":

        if energy + Decimal(single_event_list[1]) > INITIAL_ENERGY:
            energy_gain = INITIAL_ENERGY - energy
            energy = INITIAL_ENERGY
        else:
            energy_gain = Decimal(single_event_list[1])
            energy += energy_gain

        print(f"You gained {energy_gain} energy.")
        print(f"Current energy: {energy}.")

    elif single_event_list[0] == "order":

        if energy < 30:
            print(f"You had to rest!")
            energy_gain = 50
            energy += energy_gain
        else:
            earned_coins = Decimal(single_event_list[1])
            coins += earned_coins
            print(f"You earned {earned_coins} coins.")
            energy -= 30

    else:
        cost_ingredient = Decimal(single_event_list[1])
        ingredient = single_event_list[0]

        if cost_ingredient > coins:
            print(f"Closed! Cannot afford {ingredient}.")
            cannot_afford = True
            break

        coins -= cost_ingredient
        print(f"You bought {ingredient}.")

if not cannot_afford:
    print(f"Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")
