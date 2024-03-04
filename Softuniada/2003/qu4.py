# Rotate Matrix

size = int(input())
final = [[] for _ in range(size)]

for i in range(size):
    row = input().split(' ')
    for idx in range(size):
        final[idx].append(row[idx])

for i in range(size):
    final[i].reverse()
    print(' '.join(final[i]))
