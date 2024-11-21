# initial solution
def dfs(start, end, graph, visited):
    if start in visited:
        return False

    if start == end:
        return True

    visited.add(start)

    for child in graph[start]:
        if dfs(child, end, graph, visited):
            return True

    return False

def path_exists(start, end, graph):
    visited = set()

    return dfs(start, end, graph, visited)


buildings = int(input())
num_streets = int(input())
graph = {}
streets = []

for i in range(buildings):
    graph[str(i)] = []


for _ in range(num_streets):
    start, end = input().split(' - ')
    if (start, end) not in streets and (end, start) not in streets:
        streets.append((start, end))

    if end not in graph[start]:
        graph[start].append(end)
    if start not in graph[end]:
        graph[end].append(start)

important_streets = set()
for start, end in sorted(streets, key=lambda x: (x[0], x[1])):
    graph[start].remove(end)
    graph[end].remove(start)

    if not path_exists(start, end, graph):
        important_streets.add((min(start, end), max(start, end)))

    graph[start].append(end)
    graph[end].append(start)

print('Important streets:')
for street in sorted(important_streets, key=lambda x: (x[0], x[1])):
    print(' '.join(street))
