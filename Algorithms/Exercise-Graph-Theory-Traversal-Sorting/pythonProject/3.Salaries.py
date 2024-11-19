def dfs(node, g, visited, node_salaries):

    if node in visited:
        return

    if len(g[node]) == 0:
        node_salaries[node] +=1

    visited.add(node)

    for child in g[node]:
        dfs(child, g, visited, node_salaries)
        node_salaries[node] += node_salaries[child]


num = int(input())
g = {}
node_salaries = {}
for i in range(num):

    if i not in g:
        g[i] = []
        node_salaries[i] = 0

    line = list(input())
    for j in range(num):
        if line[j] == 'Y':
            g[i].append(j)

visited = set()

for node in g:
    dfs(node, g, visited, node_salaries)

print(sum(node_salaries.values()))