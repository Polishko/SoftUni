# lecturer`s solution

def dfc(node, graph, visited, component):
    if visited[node]:
        return

    visited[node] = True
    for child in graph[node]:
        dfc(child, graph, visited, component)

    component.append(node)

n = int(input())
graph = []

for i in range(n):
    line_parts = input()
    graph.append([] if line_parts == '' else [int(x) for x in line_parts.split()])

visited = [False] * n

for node in range(n):
    component = []

    if visited[node]:
        continue

    dfc(node, graph, visited, component)
    print(f"Connected component: {' '.join(str(x) for x in component)}")



# initial solution

# def dfc(node, graph, visited, result):
#     if node in visited:
#         return
#
#     visited.add(node)
#     for child in graph[node]:
#         dfc(child, graph, visited, result)
#
#     result.append(node)
#
# n = int(input())
# graph = {}
#
# for i in range(n):
#     line_parts = input()
#     graph[i] = [] if line_parts == '' else [int(x) for x in line_parts.split()]
#
# visited = set()
# result = []
#
# for node in graph:
#     if not node in visited:
#         dfc(node, graph, visited, result)
#         print(f"Connected component: {' '.join(str(x) for x in result)}")
#         result = []
