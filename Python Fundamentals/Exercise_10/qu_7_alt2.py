# hocanin cozumu

text = input()
parts = text.split(">")
left_power = 0 # kullanilmayan poweri sakliyor

result = [parts[0]] # ilk > oncesindeki kismi direk initial olarak aldi listeye
for part in parts[1:]:

    # power digit olsaydi bir for  cycle ile is digit olmayana kadar digitleri alacaktik sonra power = int(rakam stringi)
    power = part[0] # rakamin kendisi patlama gucu
    left_power += power

    formatted_part = part[left_power:] # yani atiyorum left powwer 3 ise parttan 3 idx sil: 0, 1, 2 ve 3'ten basla
    left_power = max(left_power - len(part), 0) # yani kalan powerin tamami kullanilirsa kalan 0
    result.append(formatted_part)

print(">".join(result))



