# Lecturer`s optimized solution
def dfs(node, graph, salaries):
    # if node salary already set, return to get value
    if salaries[node] is not None:
        return salaries[node]
    # else if node with no children, set salary 1 as per requirements
    if len(graph[node]) == 0:
        salaries[node] = 1
        return 1 # then return its value

    # now apply dfs to traverse children
    salary = 0 # salary from all children
    for child in graph[node]:
        salary += dfs(child, graph, salaries)

    salaries[node] = salary # set node salary
    return salary # return value


nodes = int(input())
graph = []

for i in range(nodes):
    line = input()
    children = []
    for idx, state in enumerate(line):
        if state == 'Y':
            children.append(idx)
    graph.append(children)

salaries = [None] * nodes

result = 0
for node in range(nodes):
    salary_node = dfs(node, graph, salaries)
    result += salary_node

print(result)


# initial solution
# def dfs(node, g, visited, node_salaries):
#
#     if node in visited:
#         return
#
#     if len(g[node]) == 0:
#         node_salaries[node] +=1
#
#     visited.add(node)
#
#     for child in g[node]:
#         dfs(child, g, visited, node_salaries)
#         node_salaries[node] += node_salaries[child]
#
#
# num = int(input())
# g = {}
# node_salaries = {}
# for i in range(num):
#
#     if i not in g:
#         g[i] = []
#         node_salaries[i] = 0
#
#     line = list(input())
#     for j in range(num):
#         if line[j] == 'Y':
#             g[i].append(j)
#
# visited = set()
#
# for node in g:
#     dfs(node, g, visited, node_salaries)
#
# print(sum(node_salaries.values()))