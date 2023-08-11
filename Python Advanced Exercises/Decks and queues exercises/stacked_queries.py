# bu soruda hata veren max ve minde de stack icinin bos olmasiymis yani yine max(stack) kullanabilirsin ama bu fonksiyonlarin
# acaba stack yapisina uygun mu ondan emin olamadim yani zaman complexity ne?
stack = []
max_stack = []
min_stack = []

n = int(input())

for _ in range(n):
    query = list(map(int, input().split(" ")))

    if query[0] == 1:
        stack.append(query[1])
        if len(stack) == 1:
            max_stack.append(query[1])
            min_stack.append(query[1])
        else:
            if query[1] > max_stack[-1]:
                max_stack.append(query[1])
            else:
                max_stack.append(max_stack[-1])
            if query[1] < min_stack[-1]:
                min_stack.append(query[1])
            else:
                min_stack.append(min_stack[-1])
    elif query[0] == 2:
        if len(stack) != 0:
            stack.pop()
            max_stack.pop()
            min_stack.pop()
    elif query[0] == 3:
        if len(stack) > 0:
            print(max_stack[-1])
    else:
        if len(stack) > 0:
            print(min_stack[-1])

if len(stack) > 0:
    rev = []
    while len(stack) > 0:
        rev.append(str(stack.pop()))
    print(", ".join(rev))
