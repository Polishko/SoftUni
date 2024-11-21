def dfs(node, destination, graph, visited):
    if node in visited:
        return

    visited.add(node)

    if node == destination:
        return
    for child in graph[node]:
        dfs(child, destination, graph, visited)
    # a path completed
    # don`t remove node, we need to check if it's in visited in func path_exists

def path_exists(source, destination, graph):
    visited = set()

    # traverse adding visited nodes to set
    dfs(source, destination, graph, visited)

    # if destination in visited returns true: path exists
    return destination in visited

nodes = int(input())

graph = {}
edges = []

for _ in range(nodes):
    parent, children_line = input().split(' -> ')
    children = children_line.split(' ')
    graph[parent] = children

    # store all edges
    for child in children:
        edges.append((parent, child))

removed_edges = []
for source, destination in sorted(edges, key=lambda x: (x[0], x[1])):
    # when we remove an edge from the graph it will be still in the edges list, so to avoid re-removing check
    # if already removed
    if not destination in graph[source] and not source in graph[destination]:
        continue

    graph[source].remove(destination) # remove edge
    graph[destination].remove(source) # remove bidirectionally

    # then check if path from source to destination still exists
    if path_exists(source, destination, graph):
        removed_edges.append(f'{source} - {destination}')
    else:
        graph[source].append(destination)
        graph[destination].append(source)

print(f'Edges to remove: {len(removed_edges)}')
for pair in removed_edges:
    print(pair)
