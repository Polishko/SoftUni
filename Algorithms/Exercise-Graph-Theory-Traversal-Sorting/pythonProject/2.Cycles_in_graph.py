# lecturer`s solution with dfs
def dfs(node, g, visited, current_cycle):
    if node in current_cycle:
        raise Exception
    if node in visited:
        return 
    
    visited.add(node)
    current_cycle.add(node)

    for child in g[node]:
        dfs(child, g, visited, current_cycle)

    current_cycle.remove(node)
    
g = {}
visited = set()

while True:
    line = input()
    
    if line == 'End':
        break
        
    source, destination = line.split('-')
    
    if source not in g:
        g[source] = []
    if destination not in g:
        g[destination] = []
    g[source] = destination
    
try:
    for node in g:
        dfs(node, g, visited, set())
    print('Acyclic: Yes')
except Exception:
    print('Acyclic: No')
    


# initial solution
# graph = []
# starting = set()
# ending = set()
# is_acyclic = 'No'
# 
# while True:
#     line = input()
# 
#     if line == 'End':
#         break
# 
#     start, end = line.split('-')
# 
#     starting.add(start)
#     ending.add(end)
# 
# 
# if len(starting - ending) != 0:
#     is_acyclic = 'Yes'
# 
# print(f'Acyclic: {is_acyclic}')
