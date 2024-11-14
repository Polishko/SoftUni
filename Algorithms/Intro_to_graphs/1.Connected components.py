def dfc(node, graph, visited, result):
    if node in visited:
        return

    visited.add(node)
    for child in graph[node]:
        dfc(child, graph, visited, result)

    result.append(node)

n = int(input())
graph = {}

for i in range(n):
    line = input()
    graph[i] = [] if line == '' else [int(x) for x in line.split()]

visited = set()
result = []

for node in graph:
    if not node in visited:
        dfc(node, graph, visited, result)
        print(f"Connected component: {' '.join(str(x) for x in result)}")
        result = []
