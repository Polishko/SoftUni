# single component graph

# non-recursive solution
# find all dependencies for each node
def find_dependencies(graph):
    result = {}
    for node, children in graph.items():
        if node not in result:
            result[node] = 0 # set to 0 initially, its the starting point of the edge
        for child in children:
            if child not in result:
                result[child] = 1  # since a child has an incoming edge its dependency is 1
            else:
                result[child] += 1

    return result


def find_node_without_dependencies(dependencies_by_node):
    for node, dependencies in dependencies_by_node.items():
        if dependencies == 0:
            return node
    return None # cycle condition: all nodes remaining in the graph are with dependencies

# Get input and construct the graph
nodes = int(input())
graph = {}

for _ in range(nodes):
    line_parts = input().split('->')
    node = line_parts[0].strip()
    children = line_parts[1].strip().split(', ') if line_parts[1] else []
    graph[node] = children

dependencies_by_node = find_dependencies(graph)
has_cycles = False
sorted_nodes = []

while dependencies_by_node:
    node_to_remove = find_node_without_dependencies(dependencies_by_node)
    if node_to_remove is None:
        has_cycles = True
        break
    dependencies_by_node.pop(node_to_remove)
    sorted_nodes.append(node_to_remove)
    for child in graph[node_to_remove]:
        dependencies_by_node[child] -= 1

if has_cycles:
    print('Invalid topological sorting')
else:
    print(f"Topological sorting: {', '.join(sorted_nodes)}")

# recursive solution with dfs
# from collections import deque
#
#
# def dfs(node, graph, visited, cycles, sorted_nodes):
#     if node in cycles:
#         raise Exception('Invalid topological sorting')
#     if node in visited:
#         return # node already processed
#
#     visited.add(node)
#     cycles.add(node) # add to stack
#     for child in graph[node]:
#         dfs(child, graph, visited, cycles, sorted_nodes)
#
#     cycles.remove(node) # remove from stack
#     sorted_nodes.append(node)
#
# # Get input and construct the graph
# nodes = int(input())
# graph = {}
#
# visited = set()
# cycles = set()
#
# for _ in range(nodes):
#     line_parts = input().split('->')
#     node = line_parts[0].strip()
#     children = line_parts[1].strip().split(', ') if line_parts[1] else []
#     graph[node] = children
#
# sorted_nodes = deque()
# for node in graph:
#     dfs(node, graph, visited, cycles, sorted_nodes)
#
# print(f"Topological sorting: {', '.join(sorted_nodes)}")