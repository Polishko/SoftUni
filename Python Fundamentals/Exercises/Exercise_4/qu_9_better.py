def validate_password(password):
    error_list = []

    if not is_valid_length(password):
        error_list.append("Password must be between 6 and 10 characters")

    if not contains_valid_chars(password):
        error_list.append("Password must consist only of letters and digits")

    if not contains_valid_digit_count(password):
        error_list.append("Password must have at least 2 digits")

    return error_list


def is_valid_length(password):

    return 6 <= len(password) <= 10


def contains_valid_chars(password):

    return password.isalnum()


def contains_valid_digit_count(password):
    digit_count = 0

    for char in password:
        if char.isdigit():
            digit_count += 1

    return digit_count >= 2


input_str = input()
errors = validate_password(input_str)

if errors:
    for error in errors:
        print(error)
else:
    print("Password is valid")
