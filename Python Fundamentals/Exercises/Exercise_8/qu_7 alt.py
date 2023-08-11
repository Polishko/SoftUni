string = input()
chars_to_delete = 0
output = ""

for idx in range(-len(string), 0):
    char = string[idx]

    if chars_to_delete > 0 and char != ">":
        chars_to_delete -= 1
        continue
    elif char == ">":
        chars_to_delete += int(string[idx + 1])

    output += char

print(output)
