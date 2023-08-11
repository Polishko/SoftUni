num = int(input())

for _ in range(1, num + 1):
    string = input()

    string_pure = True
    for k in range(len(string)):# k icin char veya ch diyebilirsin/for ch in string (bu baya yeterli len gereksiz)
        if string[k] == "," or string[k] == "." or string[k] == "_":
            string_pure = False

    if string_pure:
        print(f"{string} is pure.")
    else:
        print(f"{string} is not pure!")
