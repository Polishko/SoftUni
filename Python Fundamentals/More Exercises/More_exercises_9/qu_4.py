import re
spaces = r"\s"
health_pattern = re.compile(r"[^0-9\+\-\*\/\.]+")
damage_pattern = re.compile(r"(\-*\d+(?<=\d)\.(?=\d)\d+|\-*\d+(?!\.))")
operator_pattern = re.compile(r"([\*\/]*)")

demons = input().split(",")

demon_collection = {}
for name in demons:
    demon_name = re.sub(spaces, "", name)
    health = 0
    health_chars = []
    base_damage = 0.0
    operators = ""

    matches_health = re.findall(health_pattern, demon_name)
    for match_health in matches_health:
        health += sum([ord(char) for char in match_health])

    matches_damage = re.findall(damage_pattern, demon_name)
    for match_damage in matches_damage:
        if not match_damage:
            continue
        base_damage += float(match_damage)

    matches_operator = re.findall(operator_pattern, demon_name)
    for match_operator in matches_operator:
        if not match_operator:
            continue
        operators += match_operator
    for operator in operators:
        if operator == "*":
            base_damage *= 2
        elif operator == "/":
            if base_damage == 0:
                continue
            base_damage /= 2

    demon_collection[demon_name] = {health: base_damage}
    if len(demon_collection) > 1:
        demon_collection = dict(sorted(demon_collection.items()))

for demon, demon_info in demon_collection.items():
    for health, damage in demon_info.items():
        print(f"{demon} - {health} health, {damage:.2f} damage")
