# Last row in Pascal's triangle

num = int(input())

current = []
initial_steps = [[1], [1, 1], [1, 2, 1]]

if num < 3:
    current = initial_steps[num]
else:
    initial = initial_steps[-1]

    for line in range(3, num + 1):
        current = [1]
        for i in range(1, line):
            middle = [initial[i] + initial[i - 1]]
            current.extend(middle)
        current.extend([1])
        initial = current

print(' '.join([str(num) for num in current]))
