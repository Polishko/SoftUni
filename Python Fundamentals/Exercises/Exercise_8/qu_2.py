str_1, str_2 = input().split(" ")

if len(str_1) <= len(str_2):
    short_str = str_1
    long_str = str_2
else:
    short_str = str_2
    long_str = str_1

total = 0
for i in range(len(short_str)):
    total += (ord(short_str[i]) * ord(long_str[i]))


for k in range(len(short_str), len(long_str)):
    total += ord(long_str[k])

print(total)

# min(len(word1, len(word2) aldi
# tek cycle min len ile her i icin iki kelimeden de char aldi ve ord alip toplama ekledi
# ama sonra iki kalan kelime icin iki ayri cycle yapmasi gerekti, uzun kelime hangisi bilmedigi icin, o yuzden salla
# alternatif olanlar icin iki comprehension yapmis sum([ord(char) for char in word_1[min_len:]])