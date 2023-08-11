text = input()
emoticons = []
current_idx = -1

for char in text:
    current_idx += 1
    if char == ":":
        emoticons.append(text[current_idx:current_idx + 2])

print(*emoticons, sep="\n")
