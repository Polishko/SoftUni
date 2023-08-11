def naughty_or_nice_list(kids_list, *args, **kwargs):
    group_kids = {
        "Nice": [],
        "Naughty": [],
        "Not found": []}

    def add_kid():
        if len(kids) == 1:
            group_kids[kid_type].append(kids[0][1])
            kids_list.remove(*kids)

    for arg in args:
        num, kid_type = arg.split("-")
        kids = [kid for kid in kids_list if kid[0] == int(num)]
        add_kid()

    for name, kid_type in kwargs.items():
        kids = [kid for kid in kids_list if kid[1] == name]
        add_kid()

    if kids_list:
        group_kids["Not found"] = [kid[1] for kid in kids_list]

    result = []
    for group in group_kids:
        if group_kids[group]:
            result.append(f"{group}: {', '.join(group_kids[group])}")

    return "\n".join(result)
