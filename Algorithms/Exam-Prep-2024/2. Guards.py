# Lecturer`s optimal solution: Early exit, don't loop visited neighbour branch
def dfs(graph, node, visited):
    if node in visited:
        return

    visited.add(node)
    for child in graph[node]:
        dfs(graph, child, visited)

nodes = int(input())
edges = int(input())

graph = {i: [] for i in range(1, nodes + 1)}
for _ in range(edges):
    source, destination = [int(x) for x in input().split(' ')]
    graph[source].append(destination)

start_node = int(input())
visited = set()
dfs(graph, start_node, visited)

unvisited = []
for node in graph.keys():
    if node not in visited:
        unvisited.append(node)

print(*sorted(unvisited), sep=' ')

# initial solution
# def find_path(graph, start_node, visited):
#     for neighbour in graph[start_node]:
#         if neighbour in visited:
#             continue
#         visited.add(neighbour)
#         find_path(graph, neighbour, visited)
#
# nodes = int(input())
# edges = int(input())
#
# node_set = set()
# graph = {i: [] for i in range(1, nodes + 1)}
# for _ in range(edges):
#     source, destination = [int(x) for x in input().split(' ')]
#     graph[source].append(destination)
#
# start_node = int(input())
# visited = {start_node}
# find_path(graph, start_node, visited)
#
# unvisited = sorted(set(range(1, nodes + 1)) - visited)
# print(*unvisited, sep=' ')
