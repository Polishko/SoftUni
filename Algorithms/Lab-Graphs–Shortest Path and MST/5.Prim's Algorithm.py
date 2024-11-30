from queue import PriorityQueue


class Edge:
    def __init__(self, first, second, weight):
        self.first = first
        self.second = second
        self.weight = weight

    # Allows edges to be compared by weight in the PriorityQueue, so edges with smaller weights are prioritized.
    def __gt__(self, other):
        return self.weight > other.weight


def prim(node, graph, forest, forest_edges):
    forest.add(node)

    pq = PriorityQueue() # stores edges stored by weight
    for edge in graph[node]:
        pq.put(edge) # add all initial edges of node to queue

    # process edges in queue
    while not pq.empty():
        min_edge = pq.get()
        non_tree_node = -1  # select some default value, so later we can store what node to add and get its children

        # check if edge expands the MST (has node not in MST)
        if min_edge.first in forest and min_edge.second not in forest:
            non_tree_node = min_edge.second  # new node to be added to MST
        elif min_edge.second in forest and min_edge.first not in forest:
            non_tree_node = min_edge.first  # new node to be added to MST

        if non_tree_node == -1:  # both nodes are in forest
            continue  # avoid cycles

        forest.add(non_tree_node)  # add to MST
        forest_edges.append(min_edge)  # add to list of MST edges

        # add the edges of the new node as you added the initial edges of starting node
        # these will be processed till pq is empty
        for edge in graph[non_tree_node]:
            pq.put(edge)


edges = int(input())
graph = {} # adjacency list graph

for _ in range(edges):
    first, second, weight = [int(x) for x in input().split(', ')]
    if first not in graph:
        graph[first] = []
    if second not in graph:
        graph[second] = []

    # store for each node each edge it has
    edge = Edge(first, second, weight)
    graph[first].append(edge)
    graph[second].append(edge)

forest = set() # keep all nodes that are part of the spanning tree
forest_edges = [] # keep all edges that are part of the forest

# graph might be disconnected so iterate over each node to ensure you cover all
for node in graph:
    if node in forest: # avoid duplicated trees
        continue
    prim(node, graph, forest, forest_edges)

for edge in forest_edges:
    print(f'{edge.first} - {edge.second}')


# PriorityQueue: Ensures edges are processed in ascending order of weight.
# Forest: Tracks which nodes are already part of the MST to avoid cycles.
# Adding New Edges: Continuously adds new edges from the newly included nodes to explore new connections.
