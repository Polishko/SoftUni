import re
pattern = r"^\s*>>(?P<furniture>[A-Za-z]+[A-Za-z0-9]*|[A-Za-z]+[A-Za-z0-9]*_*[A-Za-z0-9]+)<<(?P<price>0\." \
          r"[0-9]+|[1-9][0-9]*\.*[0-9]+)!(?P<quantity>[0-9]|[1-9][0-9]*)\s*$"

# bu cok uzun bi regex ve gereksiz sanirim


total_spent = 0
line = input()
print("Bought furniture:")
while line != "Purchase":

    matches = re.finditer(pattern, line)

    for match in matches:
        print(match.group("furniture"))
        total_spent += float(match.group("price")) * float(match.group("quantity"))
    line = input()

print(f"Total money spend: {total_spent:.2f}")

# evet findall yapinca sonra groups[] kullaniyosun bu da listeden cekiyor degerleri

# bunda 21.20'deki cozumu dene match ve matchdict ile yapti
