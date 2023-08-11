# rows, columns = [int(a) for a in input().split()]
#
# first_last = [chr(x + 97) for x in range(rows)]
# main_middle = [chr(x + 97) for x in range(rows + columns)]
#
# matrix = []
# for row in range(rows):
#
#     line = []
#     for column in range(columns):
#         middle = main_middle[row:row + columns]
#         element = f"{first_last[row]}{middle[column]}{first_last[row]}"
#         line.append(element)
#
#     matrix.append(line)
#
# [print(" ".join(ele)) for ele in matrix]

rows, columns = [int(a) for a in input().split()]

first_last = [chr(x + 97) for x in range(rows)]
main_middle = [chr(x + 97) for x in range(rows + columns)]

matrix = []

for row in range(rows):
    line = []

    for column in range(columns):
        element = f"{first_last[row]}{main_middle[column + row]}{first_last[row]}"
        line.append(element)

    matrix.append(line)

[print(" ".join(ele)) for ele in matrix]

# Dilyan's solution

# rows, cols = [int(x) for x in input().split()]
#
# start = ord('a')
#
# for row in range(start, start + rows):
#     for col in range(row, row + cols):
#         print(f"{chr(row)}{chr(col)}{chr(row)}", end=" ")
#
#     print()

