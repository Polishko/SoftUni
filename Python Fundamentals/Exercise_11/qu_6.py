import re

pattern = r"(?P<link>w{3}\.[A-Za-z0-9]+[A-Za-z0-9\-]*[A-Za-z0-9]+(?:\.[a-z]+)+)"
# hocanin regexine ve cozumune bak sorun --- lerden olusan domain name degilmis

lst = []
while True:
    user_input = input()
    if not user_input:
        break
    else:
        lst.append(user_input)

for text in lst:
    matches = re.finditer(pattern, text)

    for match in matches:
        print(str(match.group("link")))

