string = input()
characters = {}

for char in string:
    if char == " ":
        continue

    if char not in characters:
        characters[char] = 0

    characters[char] += 1

for key, value in characters.items():  # veya for key in dict print key --> dict[key]
    print(f"{key} -> {value}")
