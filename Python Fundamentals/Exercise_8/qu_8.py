import string
string_lst = input().split()
total = 0

for line in string_lst:

    letter_1 = line[0]
    letter_2 = line[-1]
    num = int(line[1:-1])

    if not 97 <= ord(letter_1.lower()) <= 122 or not 97 <= ord(letter_2.lower()) <= 122:
        continue

    if letter_1.isupper():
        num /= (string.ascii_uppercase.index(letter_1) + 1) # position_1 = olarak if disina alinabilir
    elif letter_1.islower(): # bunlar else
        num *= (string.ascii_lowercase.index(letter_1) + 1)

    if letter_2.isupper():
        num -= (string.ascii_uppercase.index(letter_2) + 1)
    elif letter_2.islower():
        num += (string.ascii_lowercase.index(letter_2) + 1)

    total += num

print(f"{total:.2f}")
