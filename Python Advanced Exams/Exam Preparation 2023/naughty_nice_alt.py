def naughty_or_nice_list(*args, **kwargs):
    group_kids = {"Nice": [],
                  "Naughty": [],
                  "Not found": []
                  }

    kids, rest = args[0], []
    rest.extend(args[1:])
    rest.extend(kwargs.items())

    def take_kid(x, y):
        if type(x) == str:
            return y[0]
        elif type(x) == tuple:
            return y[1]

    def take_check(x):
        arg = ""
        if type(x) == str:
            tokens = x.split("-")
            arg = int(tokens[0]), tokens[1]
        elif type(x) == tuple:
            arg = x[0], x[1]
        return arg

    for item in rest:
        check, kid_type = take_check(item)[0], take_check(item)[1]

        count, current = 0, ""
        for kid in kids:
            if take_kid(item, kid) == check:
                count += 1
                current = kid

        if count == 1:
            group_kids[kid_type].append(current[1])
            kids.remove(current)

    for kid in kids:
        group_kids["Not found"].append(kid[1])

    result = []
    for group in group_kids:
        if group_kids[group]:
            result.append(f"{group}: {', '.join(group_kids[group])}")

    return "\n".join(result)
