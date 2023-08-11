def valid_username(line):
    if valid_chars(line) and valid_length(line) and no_redundant_symbols(line):
        return line


def valid_length(line):
    if 3 <= len(line) <= 16:
        return True
    return False


def valid_chars(line):
    for char in line:
        if not char.isalnum() and char != "_" and char != "-":
            return False
    return True


def no_redundant_symbols(line):
    for char in line:
        if char == " ":
            return False
    return True


user_names = input().split(", ")
for user_name in user_names:
    if valid_username(user_name):
        print(user_name)

