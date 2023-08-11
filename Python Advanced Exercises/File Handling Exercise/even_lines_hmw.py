import re


replace_chars = r"[-,.!?]"

with open("files/text.txt", "r") as file:
    lines = file.readlines()

for i in range(0, len(lines), 2):
    line = re.sub(replace_chars, "@", lines[i])
    print(" ".join(line.split()[::-1]))
