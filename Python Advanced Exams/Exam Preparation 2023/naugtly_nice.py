from collections import deque


def naughty_or_nice_list(*args, **kwargs):
    group_kids = {"Nice": [],
                  "Naughty": [],
                  "Not found": []
                  }

    kids, *commands = args

    for command in commands:
        num, kid_type = command.split("-")

        count = 0
        current = ""

        for kid in kids:
            if kid[0] == int(num):
                count += 1
                current = kid
        if count == 1:
            group_kids[kid_type].append(current[1])
            kids.remove(current)

    for name in kwargs:

        count = 0
        current = ""

        for kid in kids:
            if kid[1] == name:
                count += 1
                current = kid
        if count == 1:
            group_kids[kwargs[name]].append(current[1])
            kids.remove(current)

    while kids:
        kids = deque(kids)
        current = kids.popleft()
        group_kids["Not found"].append(current[1])

    result = []
    for group in group_kids:
        if group_kids[group]:
            result.append(f"{group}: {', '.join(group_kids[group])}")

    return "\n".join(result)
