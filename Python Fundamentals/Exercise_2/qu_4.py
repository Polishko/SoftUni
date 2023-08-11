num_chars = int(input())
sum_chars = 0

for _ in range(1, num_chars + 1):
    letter = input()
    sum_chars += ord(letter)

print(f"The sum equals: {sum_chars}")
