sequence = input()
letter_part = ""
num_part = ""
output = ""
slice_idx = 0

while len(sequence) > 0:

    for idx in range(len(sequence)):
        char = sequence[idx]
        if not char.isnumeric():
            letter_part += char
        else:
            slice_idx = idx
            break
    sequence = sequence[slice_idx:]

    for idx in range(len(sequence)):
        char = sequence[idx]
        if char.isnumeric():
            num_part += char
        else:
            slice_idx = idx
            break

    sequence = sequence[slice_idx:]
    num = int(num_part)
    output += letter_part.upper() * num
    letter_part = ""
    num_part = ""

unique_chars = len(set(output))

print(f"Unique symbols used: {unique_chars}")
print(output)
