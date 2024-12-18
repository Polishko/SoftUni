# Lecturer's solution
def extract_path(node, parent):
    first_node = node
    result = [node]

    while True:
        node = parent[node]
        result.append(node)
        if node == first_node:
            break

    return result[::-1]

nodes = set()
edges = int(input())

graph = []
for _ in range(edges):
    source, destination, weight_str = input().split()
    weight = float(weight_str)
    graph.append((source, destination, weight))
    nodes.add(source)
    nodes.add(destination)

start_node = input()

distances = {node: float('-inf') for node in nodes} # we start from smallest and try find highest result
distances[start_node] = 1 # best result for node if no better found

parent = {node: None for node in nodes}

# Bellman-Ford
for _ in range(len(nodes) - 1):
    for (source, destination, weight) in graph:
        new_distance = distances[source] * weight
        if new_distance > distances[destination]:
            distances[destination] = new_distance
            parent[destination] = source

for (source, destination, weight) in graph:
    new_distance = distances[source] * weight
    if new_distance > distances[destination]:
        print(True)
        path = extract_path(start_node, parent)
        print(*path, sep=' ')
        break
else:
    print(False)
    for node, best_price in distances.items():
        print(f'{node}: {best_price:.3f}')


# Initial solution (missing edge cases, not optimal)
# def find_paths_and_sums(currency, graph, visited, curr_path, curr_sum, paths, sums):
#     for relation in graph[currency]:
#         target_currency, rate = relation
#
#         if target_currency == starting and len(curr_path) > 1:
#             curr_path.append(target_currency)
#             new_sum = curr_sum * rate
#             paths.append(list(curr_path))
#             sums.append(new_sum)
#             curr_path.pop()
#             continue
#
#         if (currency, target_currency) in visited:
#             continue
#
#         visited.add((currency, target_currency))
#         curr_path.append(target_currency)
#         new_sum = curr_sum * rate
#
#         find_paths_and_sums(target_currency, graph, visited, curr_path, new_sum, paths, sums)
#         curr_path.pop()
#         visited.remove((currency, target_currency))
#
#
#
# trading_pairs = int(input())
# graph = {}
#
#
# for _ in range(trading_pairs):
#     base, target, rate_info = input().split(' ')
#     rate = float(rate_info)
#
#     if base not in graph:
#         graph[base] = []
#
#     graph[base].append((target, rate))
#
# starting = input()
# visited = set()
# curr_path = [starting]
# curr_sum = 1
# paths = []
# sums = []
#
# find_paths_and_sums(starting, graph, visited, curr_path, curr_sum, paths, sums)
#
# arbitrage_exists = False
# for i in range(len(sums)):
#     if sums[i] > 1:
#         print('True')
#         print(' '.join(paths[i]))
#         arbitrage_exists = True
#         break
#
# if not arbitrage_exists:
#     print('False')
#     best_rate = max(sums)
#     idx_best = sums.index(best_rate)
#     rate = 1
#     print(f'{starting}: {rate:.3f}')
#     best_path = paths[idx_best]
#     current = starting
#
#     for k in range(1, len(best_path) - 1):
#         rate_list = graph[current]
#         current = best_path[k]
#         for pair in rate_list:
#             if pair[0] == current:
#                 rate *= pair[1]
#                 print(f'{current}: {rate:.3f}')
