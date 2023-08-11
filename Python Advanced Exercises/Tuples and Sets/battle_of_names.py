num_rows = int(input())

odd_set = set()
even_set = set()
for row in range(1, num_rows + 1): # input burada
    name = input()
    value = sum([ord(char) for char in name]) // row # inout burada

    if value % 2 != 0:
        odd_set.add(value)
    else:
        even_set.add(value)

to_print = []
if sum(odd_set) == sum(even_set):
    to_print = list(map(str, odd_set.union(even_set))) # direk print ediyor * unpack ve sep=", " ile
elif sum(odd_set) > sum(even_set):
    to_print = list(map(str, odd_set.difference(even_set)))
else:
    to_print = list(map(str, odd_set.symmetric_difference(even_set)))

print(", ".join(to_print))
