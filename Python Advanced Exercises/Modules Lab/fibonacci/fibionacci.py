def give_fibonacci(a):
    sequence = [0] if a == 0 else [0, 1]
    if a > 2:
        for i in range(2, a):
            sequence.append(sequence[i - 1] + sequence[i - 2])
    print(*sequence, sep=" ")

    return sequence


def locate_number(a, b):
    idx = None
    try:
        if a < 2:
            idx = b.index(a)
        else:
            idx = b[2:].index(a) + 2
    except ValueError:
        print(f"The number {a} is not in the sequence")
    else:
        print(f"The number - {a} is at index {idx}")
