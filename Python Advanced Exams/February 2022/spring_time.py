def start_spring(**kwargs):
    flowers = {}
    result = []

    for name, plant_type in kwargs.items():
        if plant_type not in flowers:
            flowers[plant_type] = []
        flowers[plant_type].append(name)

    sorted_collection = sorted(flowers.items(), key= lambda x: (-len(x[1]), x[0]))
    for item in sorted_collection:
        result.append(f"{item[0]}:")
        for flower in sorted(item[1]):
            result.append(f"-{flower}")

    return "\n".join(result)
