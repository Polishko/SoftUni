from collections import deque


rows, columns = [int(a) for a in input().split(" ")]
matrix = [[0] * columns for row in range(rows)]

snake = deque(input())

for row in range(rows):
    if row % 2 == 0:
        for column in range(columns):
            current_char = snake.popleft()
            matrix[row][column] = current_char
            snake.append(current_char)

    else:
        for column in range(columns - 1, -1, -1):
            current_char = snake.popleft()
            matrix[row][column] = current_char
            snake.append(current_char)

[print("".join(line)) for line in matrix]

# Dilyan

# from collections import deque
#
# rows, cols = [int(x) for x in input().split()]  # cols = 6
# word = list(input())  # abc => ["a", "b", "c"]
#
# word_copy = deque(word)
#
# for row in range(rows):
#     while len(word_copy) < cols:
#         word_copy.extend(word)
#
#     if row % 2 == 0:
#         print(*[word_copy.popleft() for _ in range(cols)], sep="")
#     else:
#         print(*[word_copy.popleft() for _ in range(cols)][::-1], sep="")

