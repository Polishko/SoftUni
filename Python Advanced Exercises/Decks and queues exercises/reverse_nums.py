stack = input().split(" ")

while len(stack) > 1: # for len(stack) deck daha hizli ayrica
    print(stack.pop(), end=" ")
print(stack.pop())
