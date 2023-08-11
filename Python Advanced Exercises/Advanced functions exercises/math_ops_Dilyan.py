
def math_operations(*args, **kwargs):

    for i in range(len(args)):
        key = list(kwargs.keys())[i % 4]

        if key == "a":
            kwargs[key] += args[i]
        elif key == "s":
            kwargs[key] -= args[i]
        elif key == "d" and args[i] != 0:
            kwargs[key] /= args[i]
        elif key == "m":
            kwargs[key] *= args[i]

    return "\n".join([f"{key}: {value:.1f}" for key, value in sorted(kwargs.items(), key=lambda x: (-x[1], x[0]))])

