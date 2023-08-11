input_str = input()
encrypted_str = ""

for char in input_str:
    new_char = chr(ord(char) + 3)
    encrypted_str += new_char

print(encrypted_str)


# comprehension encrypted = "".join([chr(ord(char) + 3) for char in input_str])