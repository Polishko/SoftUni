def math_operations(*args, **kwargs):

    length = min(len(args), len(kwargs))

    for i in range(length):
        if i == 0:
            kwargs["a"] += args[i]
        elif i == 1:
            kwargs["s"] -= args[i]
        elif i == 2 and args[i] != 0:
            kwargs["d"] /= args[i]
        elif i == 3:
            kwargs["m"] *= args[i]

    args = args[length:]

    if not args:
        return "\n".join([f"{key}: {value:.1f}" for key, value in sorted(kwargs.items(), key=lambda x: (-x[1], x[0]))])

    return math_operations(*args, **kwargs)

