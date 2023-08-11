class StackWithMaxMin:
    def __init__(self):
        self.main_stack = []
        self.max_stack = []
        self.min_stack = []

    def length(self):
        return len(self.main_stack)

    def push(self, x):
        self.main_stack.append(x)
        if len(self.main_stack) == 1:
            self.max_stack.append(x)
            self.min_stack.append(x)
            return

        if x > self.max_stack[-1]:
            self.max_stack.append(x)
        else:
            self.max_stack.append(self.max_stack[-1])

        if x < self.min_stack[-1]:
            self.min_stack.append(x)
        else:
            self.min_stack.append(self.min_stack[-1])

    def get_max(self):
        return self.max_stack[-1]

    def get_min(self):
        return self.min_stack[-1]

    def pop(self):
        if len(self.main_stack) != 0:
            self.main_stack.pop()
            self.max_stack.pop()
            self.min_stack.pop()

    def reverse_stack(self):
        rev = []
        while len(self.main_stack) > 0:
            rev.append(str(self.main_stack.pop()))
        return ", ".join(rev)


s = StackWithMaxMin()
n = int(input())

for _ in range(n):
    query = list(map(int, input().split(" ")))

    if query[0] == 1:
        a = query[1]
        s.push(a)

    elif query[0] == 2:
        s.pop()
    elif query[0] == 3:
        if s.length() != 0:
            print(s.get_max())
    else:
        if s.length() != 0:
            print(s.get_min())

print(s.reverse_stack())
