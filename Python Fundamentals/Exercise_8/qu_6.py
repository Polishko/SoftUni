line = input()
new_line = line[0]
current_idx = -1

for char in line:
    current_idx += 1
    if char != new_line[-1]:
        new_line += char

print(new_line)
