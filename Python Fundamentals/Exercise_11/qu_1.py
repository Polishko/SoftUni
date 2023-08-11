import re
pattern = r"\d+"

text = "" # bunu list yapabilirsin

while True:
    line = input()
    if len(line) > 0: # if not line: break dogru olan
        text += f" {line}" # bunu hic yapma
    else:
        break

matches = re.findall(pattern, text) # bunu while icinde yapip altta extend ile liste ekleyebilirsin
#hemen altina da text.extend(matches) bos line'i da aliyor yoksa bos bos enter basiyon bitene kadar run
# neden extend ama append degil debug ile bak buna
print(*matches, end=" ") # bunda da list elemanlarini print edersin
