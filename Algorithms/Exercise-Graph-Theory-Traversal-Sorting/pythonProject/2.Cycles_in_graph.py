graph = []
starting = set()
ending = set()
is_acyclic = 'No'

while True:
    line = input()

    if line == 'End':
        break

    start, end = line.split('-')

    starting.add(start)
    ending.add(end)


if len(starting - ending) != 0:
    is_acyclic = 'Yes'

print(f'Acyclic: {is_acyclic}')
