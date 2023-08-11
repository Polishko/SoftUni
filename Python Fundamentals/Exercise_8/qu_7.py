string = input()
chars_to_check = len(string)
idx_char = -len(string)
chars_to_delete = 0
output_string = ""

while chars_to_check > 0:
    char = string[idx_char]

    if chars_to_delete > 0 and char != ">":
        chars_to_delete -= 1
        chars_to_check -= 1
        idx_char += 1
        continue

    elif char == ">":
        chars_to_delete += int(string[idx_char + 1])

    output_string += char
    chars_to_check -= 1
    idx_char += 1

print(output_string)
