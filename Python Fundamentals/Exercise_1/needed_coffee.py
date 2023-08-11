needed_coffee = 0

while True:
    command = input()

    if command == "END":
        break

    if command != "coding" and command != "CODING" and command != "dog" and command != "DOG" and command != "cat" and \
       command != "CAT" and command != "movie" and command != "MOVIE":
        continue

    if command.isupper():
        needed_coffee += 2
    elif command.islower():
        needed_coffee += 1

if needed_coffee > 5:
    print(f"You need extra sleep")
else:
    print(needed_coffee)

# isupper islower kullanmadan if "kucuk harfliler" kahve += 1 if "buyuk harfliler" if += 2, boyle daha iyi dedi cunku/
# tek kontrol var (if elif) sende uzuun bir if sonra ayri if elif