from collections import deque


def best_list_pureness(*args):
    lst, rotations = deque(args[0]), args[1]
    pureness_values = {0: sum([i * lst[i] for i in range(len(lst))])}

    for i in range(1, rotations + 1):
        lst.rotate(1)
        pureness_values[i] = (sum([i * lst[i] for i in range(len(lst))]))

    sorted_pureness = sorted(pureness_values.items(), key=lambda x: -x[1])

    return f"Best pureness {sorted_pureness[0][1]} after {sorted_pureness[0][0]} rotations"
