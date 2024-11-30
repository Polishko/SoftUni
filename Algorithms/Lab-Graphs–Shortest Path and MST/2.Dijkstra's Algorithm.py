## Greedy operation, focuses on connected neighbours and only adds neighbours to queue, connection focused

from collections import deque
from queue import  PriorityQueue


class Edge:
    def __init__(self, source, destination, weight):
        self.source = source
        self.destination =destination
        self.weight = weight


edges = int(input())
graph = {}
for _ in range(edges):
    source, destination, weight = [int(x) for x in input().split(', ')]
    if source not in graph:
        graph[source] = []
    if destination not in graph:
        graph[destination] = []

    graph[source].append(Edge(source, destination, weight))

start = int(input())
target = int(input())

max_node = max(graph.keys()) # counting nodes making use of the fact that for this example nodes are int
distance = [float('inf')] * (max_node + 1) # all undiscovered dist. considered inf. so those discovered will be always smaller
parent = [None] * (max_node + 1)

distance[start] = 0 # mark start node dist as 0 already

pq = PriorityQueue()
pq.put((0, start)) # add start and its dist as tuple to queue -> will be ordered by dist

visited = set()

while not pq.empty():
    min_distance, node = pq.get()

    if node in visited:  # Skip nodes that have already been processed
        continue

    if node == target:
        break

    visited.add(node)

    for edge in graph[node]: # each edge is a combination of source, dest and weight
        new_distance = min_distance + edge.weight # cumulated distance to edge
        if new_distance < distance[edge.destination]: # if new smaller cumulative dist to edge discovered
            distance[edge.destination] = new_distance # update to smaller
            parent[edge.destination] = node # storing the path so final dest.
            pq.put((new_distance, edge.destination)) # add the new edge to the priority queue


if distance[target] == float('inf'):
    print('There is no such path.')
else:
    print(distance[target])

    path = deque()
    node = target
    while node is not None:
        path.appendleft(node)
        node = parent[node] # when we go backwards in parent, parent[node] is next in backward path
    print(*path, sep=' ')
