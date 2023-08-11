from collections import deque

operations = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b,
}

bees = deque(int(num) for num in input().split())
flowers = deque(int(num) for num in input().split())
processes = deque(input().split())

honey = 0
while bees and flowers:
    bee_match = bees.popleft()
    nectar_match = flowers.pop()

    if nectar_match < bee_match:
        bees.appendleft(bee_match)
        continue

    if nectar_match == 0:
        continue

    process = processes.popleft()
    honey += abs(operations[process](bee_match, nectar_match))

print(f"Total honey made: {honey}")

if bees:
    print(f"Bees left: {', '.join([str(bee) for bee in bees])}")
if flowers:
    print(f"Nectar left: {', '.join([str(nectar) for nectar in flowers])}")


# За тази задача не разбирам логиката зад това че "от една
# страна когато нектара не достига трябва да върнем пчелата в дека и да оставим нектара,
# пък от друга страна когато нектара е 0 трябва да оставим и пчелата".
# Аз бих върнала пчелата в дека и за този случай, но така не минава в Judge.