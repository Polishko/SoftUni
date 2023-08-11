def flights(*args):
    collection = {}
    final = ""

    for arg in args:
        if arg == "Finish":
            return collection

        if type(arg) == str:
            if arg not in collection:
                collection[arg] = 0
            final = arg
        elif type(arg) == int:
            collection[final] += arg
