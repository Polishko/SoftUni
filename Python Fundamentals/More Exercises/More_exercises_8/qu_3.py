from math import ceil
num_lst = [int(num) for num in input().split(" ")]

while True:
    line = input()
    output = ""
    type_treasure = ""
    coordinates = ""
    current_idx = 0

    if line == "find":
        break

    if len(line) > len(num_lst):
        factor = ceil(len(line) / len(num_lst))
    else:
        factor = 1

    current_nums = factor * num_lst

    for i in range(len(line)):
        ch = line[i]
        num = current_nums[i]
        output += chr(ord(ch) - num)

    for i in range(len(output)):
        sym = output[i]
        current_idx = i
        found = False

        if sym == "&":
            for char in output[i + 1:]:
                current_idx += 1
                if char == "&":
                    found = True
                    break
                type_treasure += char
        if found:
            break

    output = output[current_idx + 1:]

    for i in range(len(output)):
        sym = output[i]

        if sym == "<":
            for char in output[i + 1:]:
                if char == ">":
                    break
                coordinates += char

    print(f"Found {type_treasure} at {coordinates}")
