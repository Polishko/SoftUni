char_1 = input()
char_2 = input()


def chars_in_range(a, b):
    min_limit = ord(a)
    max_limit = ord(b)
    char_list = []

    for order in range(min_limit + 1, max_limit):
        char_list.append(chr(order))

    return " ".join(char_list)


print(chars_in_range(char_1, char_2))
