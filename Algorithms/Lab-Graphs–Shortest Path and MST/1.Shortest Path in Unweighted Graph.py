from collections import deque


nodes = int(input())
edges = int(input())

graph = [[] for _ in range(nodes + 1)]

for _ in range(edges):
    source, destination = [int(x) for x in input().split()]
    graph[source].append(destination)


start = int(input())
end = int(input())

visited = [False] * (nodes + 1)
parent = [None] * (nodes + 1)

visited[start] = True
queue = deque([start])

while queue:
    node = queue.popleft()

    if node == end:
        break

    for child in graph[node]:
        if visited[child]:
            continue

        visited[child] = True
        queue.append(child)
        parent[child] = node # the different part from the original bfs

# to print shortest path from end to start
node = end
path = []
while node is not None: # or not starting node
    path.append(node)
    node = parent[node] # go to parent

print(f'Shortest path length is: {len(path) - 1}')
print(*reversed(path), sep=' ')
