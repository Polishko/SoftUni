class Edge:
    def __init__(self, first, second, weight):
        self.first = first
        self.second = second
        self.weight = weight


# effectively combining direct or indirectly connected nodes to one tree
# root here: logical starting point of building connections or anchor for tracking
def find_root(parent, node):
    while node != parent[node]:
        node = parent[node]
    return node


edges = int(input())
graph = []

max_node = float('-inf')
for _ in range(edges):
    first, second, weight = [int(x) for x in input().split(', ')]
    graph.append(Edge(first, second, weight))
    max_node = max(first, second, max_node) # since in the problem the nodes are nums we get count of nodes this way

parent = [num for num in range(max_node + 1)] # on index 0 we have 0, each node is its own parent 0: 0 (parent is latter)
forest = []
for edge in sorted(graph, key=lambda e: e.weight):
    # Apply Find-Union concept
    first_node_root = find_root(parent, edge.first)
    second_node_root = find_root(parent, edge.second)
    if first_node_root != second_node_root: # these belong to different trees and we will connect them
        parent[first_node_root] = second_node_root # order doesn`t matter
        forest.append(edge)

for edge in forest:
    print(f'{edge.first} - {edge.second}')

# so in the final result we actually don`t know which of the edges in forest belong to which MST
# if we want to track edges we can store these in mst_edges list
