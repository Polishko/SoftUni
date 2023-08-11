# hocanin cozumu

from string import ascii_letters, digits
allowed_chars = ascii_letters + digits + "_" + "-"

user_names = input().split(", ")

for user_name in user_names:
    if 3 <= len(user_name) <= 16:
        contains_allowed_chars = all(char in allowed_chars for char in user_name)
        if contains_allowed_chars:
            print(user_name)
