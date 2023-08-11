population_wealth = [int(num) for num in input().split(", ")]
min_limit = int(input())
max_wealth = max(population_wealth)
min_wealth = min(population_wealth)
needed_wealth = min_limit - min_wealth

all_reached_limit = False

while max_wealth - needed_wealth >= min_limit:
    index_max = population_wealth.index(max_wealth)
    max_wealth -= needed_wealth
    population_wealth[index_max] = max_wealth
    index_min = population_wealth.index(min_wealth)
    min_wealth += needed_wealth
    population_wealth[index_min] = min_wealth

    max_wealth = max(population_wealth)
    min_wealth = min(population_wealth)
    needed_wealth = min_limit - min_wealth

    if min_wealth == min_limit:
        all_reached_limit = True
        break

if all_reached_limit:
    print(population_wealth)
else:
    print(f"No equal distribution possible")
