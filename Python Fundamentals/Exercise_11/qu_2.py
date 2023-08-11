import re

pattern = r"\b_(?P<var>[A-Za-z0-9]+)\b"
text = input()

matches = re.finditer(pattern, text)
match_count = len(re.findall(pattern, text))
count = 0

for match in matches:
    count += 1
    if count < match_count:
        print(match.group("var"), end=",")
    else:
        print(match.group("var"))

# ya da matches = findall(pattern, text) sonra direk print(",".join(matches))