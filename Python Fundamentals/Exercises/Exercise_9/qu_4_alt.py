import re
pattern = r"^|\s([A-Za-z0-9]+([\-\.\_]*[A-Za-z0-9])*@[A-Za-z](\-*[A-Za-z])+(\.(\-*[A-Za-z])+)+)\b"

text = input()

matches = re.findall(pattern, text)
# print(matches)
# print("\n".join(groups[0] for groups in matches))
# findall gruplari aliyo, tumunu paranteze alirsan bu grup 0 oluyo liste icinde, liste de groups adli bu durumda. ama
# match olmayinca bos satir basabiliiyo

# o yuzden bu daha dogru
for groups in matches:
    if not matches:
        continue
    print(groups[0])
