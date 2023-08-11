# iki sozluk yapti biri junk icin biri o uc ozel item icin (hepsine 0 verdi burada fromkeys() kullanilabilir mi)
# hatta sonra legendary item sozlugu de yapti material: legendary_item bunu direk printte dict[material] olarak kullandi

def get_legendary_item(item_collection):

    if "shards" in item_collection and item_collection["shards"] >= 250:
        legendary_item = "Shadowmourne"
        item_collection["shards"] -= 250
        print(f"{legendary_item} obtained!")
        return True

    elif "fragments" in item_collection and item_collection["fragments"] >= 250:
        legendary_item = "Valanyr"
        item_collection["fragments"] -= 250
        print(f"{legendary_item} obtained!")
        return True

    elif "motes" in item_collection and item_collection["motes"] >= 250:
        legendary_item = "Dragonwrath"
        item_collection["motes"] -= 250
        print(f"{legendary_item} obtained!")
        return True

    return False


def item_quantity(item_collection, item):
    if item_collection.get(item) is None:
        return 0
    return item_collection.get(item)


collected_items = {}
legendary_item_found = False

while not legendary_item_found:
    main_input = input().split(" ")

    for i in range(len(main_input)): # 2 adimda iterate edip birini miktar birini yani i + 1: malzeme aldi

        if i % 2 == 0:
            quantity = (int(main_input[i]))
            material = main_input[i + 1].lower() # malzeme special malzeme sozlugunde mi bakti varsa sozlukte miktarini artirdi
            # ve 250yi asiyorsa break ve boolean ile craft bulundu seninki gibi while kirmak icin ama son miktari bulmak icin -250

            if material not in collected_items:   # junklari da ayri ekledi topladi
                collected_items[material] = 0

            collected_items[material] += quantity

            legendary_item_found = get_legendary_item(collected_items)

            if legendary_item_found:
                break

print(f"shards: {item_quantity(collected_items, 'shards')}")
print(f"fragments: {item_quantity(collected_items, 'fragments')}")
print(f"motes: {item_quantity(collected_items, 'motes')}")

for key, value in collected_items.items():
    if key != "shards" and key != "fragments" and key != "motes":
        print(f"{key}: {value}")
