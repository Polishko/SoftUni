input_str = input()


def password_validator(a):
    password_valid = True
    invalid_chars = False

    if len(a) < 6 or len(a) > 10:
        password_valid = False
        print(f"Password must be between 6 and 10 characters")

    digit_count = 0

    for idx in range(len(a)):

        if not (48 <= ord(a[idx]) <= 57) and not (65 <= ord(a[idx]) <= 90) \
                and not (97 <= ord(a[idx]) <= 122):
            password_valid = False
            invalid_chars = True

        if 48 <= ord(a[idx]) <= 57:
            digit_count += 1

    if invalid_chars:
        print(f"Password must consist only of letters and digits")

    if digit_count < 2:
        password_valid = False
        print(f"Password must have at least 2 digits")

    if password_valid:
        print("Password is valid")


password_validator(input_str)
# ayri fonksiyonlar kullaniyor her validation icin
# isdigit isalfanum kullandi