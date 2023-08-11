text = input()
unique_chars = set((char, text.count(char)) for char in text)

for pair in sorted(unique_chars):
    print(f"{pair[0]}: {pair[1]} time/s")

# aslinda count yavas dict daha iyi