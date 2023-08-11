strings = []

while True:   # daha kisa cozum: listeye gerek yok. string input al, break olmadiysa quantity input al,
    string = input() #sonra ya stringi sozluge ekle = miktar ya da string sozlukte varsa miktarini artir

    if string == "stop":
        break

    strings.append(string)

dictionary_strings = {}

for i in range(len(strings)):

    if i % 2 == 0:
        key = strings[i]
        value = int(strings[i + 1])

        if key not in dictionary_strings:
            dictionary_strings[key] = 0

        dictionary_strings[key] += value

for key, value in dictionary_strings.items():
    print(f"{key} -> {value}")
