n = int(input())

for _ in range(n):
    name = ""
    age = ""
    line = input()

    for i in range(len(line)):
        char = line[i]

        if char == "@":
            for ch in line[i + 1:]:
                if ch == "|":
                    break
                name += ch
        elif char == "#":
            for ch in line[i + 1:]:
                if ch == "*":
                    break
                age += ch

    print(f"{name} is {age} years old.")
