import re
pattern = r"\s[A-Za-z0-9]+([\-\.\_]*[A-Za-z0-9])*@[A-Za-z](\-*[A-Za-z])+(\.(\-*[A-Za-z])+)+\b"
# bunun basinda \s|^ daha dogru

text = input()

matches = re.finditer(pattern, text)

for match in matches:
    print(match.group().lstrip())

   # findall gruplari aliyo cok olunca tuple yapabiliyo ic iceyse

   # print(" ".join(groups[0] for groups in matches)) bu findall ile ve tum pattern bir gruba alinirsa

