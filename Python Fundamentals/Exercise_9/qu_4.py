phonebook = {}

while True:
    user_input = input()

    if "-" not in user_input:
        people_to_search = int(user_input)
        break

    name, phone = user_input.split("-") # split, "" icindeki elemani ariyor. eleman yoksa split etmeden veriyor

    if name not in phonebook: # bu adimi hic kullanmadi, asagidaki hem olusturuyor hem olani guncelliyor
        phonebook[name] = 0

    phonebook[name] = phone

for _ in range(people_to_search):
    search_name = input()

    if search_name not in phonebook:
        print(f"Contact {search_name} does not exist.") # ya da continue yerine alttaki print else
        continue

    print(f"{search_name} -> {phonebook[search_name]}")
