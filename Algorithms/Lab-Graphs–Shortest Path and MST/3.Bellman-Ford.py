## Focuses on edge relaxation, doesn`t need connection info, edge focused
"""
Breadth-First Search:
Processes nodes layer by layer in strict levels, based on distance.
Focuses on neighbor relationships.
Bellman-Ford:
Processes edges globally in each iteration, updating distances as new shorter paths are found.
Works indirectly layer by layer because of the way edge relaxation propagates shortest path information.
"""

from collections import deque


class Edge:
    def __init__(self, source, destination, weight):
        self.source = source
        self.destination =destination
        self.weight = weight


nodes = int(input())
edges = int(input())

graph = []

for _ in range(edges):
    source, destination, weight = [int(x) for x in input().split()]
    graph.append(Edge(source, destination, weight))

start = int(input())
target = int(input())

distance = [float('inf')] * (edges + 1)
distance[start] = 0
parent = [None] * (edges + 1)

for _ in range(edges - 1): # because longest dist could be v - 1 for v nodes
    updated = False
    for edge in graph:
        if distance[edge.source] == float('inf'):
            continue

        new_distance = distance[edge.source] + edge.weight # new dist for destination is source weight + edge weight
        if new_distance < distance[edge.destination]:
            distance[edge.destination] = new_distance
            parent[edge.destination] = edge.source
            updated = True # A shorter path to this node was found, so exploration must continue to propagate this update further.
    if not updated: # No distances were updated in this iteration, meaning all shortest paths are finalized. Stop iterating and continue to next edge
        break

# after exploring all possible paths by iterating  v-1 times iterate once more
# if shorted path, there`s a negative cycle
for edge in graph:
    new_distance = distance[edge.source] + edge.weight
    if new_distance < distance[edge.destination]:
        print('Negative Cycle Detected')
        break
else:
    path = deque()
    node = target
    while node is not None:
        path.appendleft(node)
        node = parent[node]
    print(*path, sep=' ')
    print(distance[target])
