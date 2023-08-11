budget = float(input())
price_kg_flour = float(input())
price_pack_eggs = price_kg_flour * 0.75
price_liter_milk = price_kg_flour * 1.25
price_milk_per_bread = price_liter_milk * 0.25

cost_per_loaf = price_pack_eggs + price_kg_flour + price_milk_per_bread

colored_eggs = 0
baked_loafs = 0

while True:
    if cost_per_loaf > budget:
        break
    baked_loafs += 1
    budget -= cost_per_loaf
    colored_eggs += 3

    if baked_loafs % 3 == 0:
        colored_eggs -= (baked_loafs - 2)

print(f"You made {baked_loafs} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")
