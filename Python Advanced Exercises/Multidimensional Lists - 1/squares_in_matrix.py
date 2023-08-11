rows, columns = [int(a) for a in input().split(" ")]
matrix = [input().split(" ") for x in range(rows)]

found = 0

for row in range(rows - 1):
    for column in range(columns - 1):
        current = [matrix[row][column], matrix[row][column + 1], matrix[row + 1][column], matrix[row + 1][column + 1]]

        if len(set(current)) == 1:
            found += 1

print(found)


