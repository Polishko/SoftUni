# Draw Rocket

n = int(input())

# The head
last_line = ''
underscores_initial = int((n + 5 - 1) / 2)
underscores = underscores_initial
vertical = 0

for i in range(underscores_initial + 1):
    if i == 1:
        vertical = 1
    elif i > 1:
        vertical = 3

    left = 1 if i >= 1 else 0
    right_symbol = '\\'
    right = 1 if i >= 1 else 0
    cap = 1 if i == 0 else 0
    dots = int((n + 5 - (underscores * 2 + vertical + left + right + cap)) / 2) if i > 2 else 0
    line = (f'{underscores * "_"}{left * "/"}{dots * "."}{vertical * "|"}'
            f'{cap * "^"}{dots * "."}{right * right_symbol}{underscores * "_"}')

    if i == underscores_initial - 1:
        last_line = line
    print(line)

    underscores -= 1

print(last_line)

# The body
underscores = int(((n + 5) - 3) / 2) * '_'
vertical = '|||'
[print(f'{underscores}{vertical}{underscores}') for i in range(n)]

# The tail
line = 0
underscores_initial = int(((n + 5) - 3) / 2)
underscores = underscores_initial

while underscores > 0:
    curly = 3 if line == 0 else 0
    exclamation = 1 if line > 0 else 0
    left = 2 if line > 0 else 0
    right = 2 if line > 0 else 0
    right_symbol = right * '\\'
    dots = int(((n + 5) - (underscores * 2 + left + right + exclamation + curly)) / 2)

    print(f'{underscores * "_"}{curly * "~"}{left * "/"}'
          f'{dots * "."}{exclamation * "!"}{dots * "."}{right_symbol}{underscores * "_"}')
    line += 1
    underscores -= 1
