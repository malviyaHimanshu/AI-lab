'''
    CS20B1097 HIMANSHU 
    TRAVELLING SALESMAN PROBLEM
'''

import numpy as np

# USING DEPTH FIRST SEARCH
def tsp_dfs(graph, start_node, visited, count, cost):
    if count==len(graph) and graph[start_node][0]:
        return cost + graph[start_node][0]

    min_cost = 9999
    for i in range(len(graph)):
        if not visited[i] and graph[start_node][i]:
            visited[i] = True
            min_cost = min(min_cost, tsp_dfs(graph, i, visited, count+1, cost+graph[start_node][i]))
            visited[i] = False
    return min_cost

# USING BREADTH FIRST SEARCH
def tsp_bfs(graph):
    queue = []
    queue.append([0])
    while len(queue[0]) != len(graph):
        path = queue.pop(0)
        for i in range(len(graph)):
            if i not in path:
                path2 = path[:]
                path2.append(i)
                queue.append(path2)

    min_cost = 9999
    for i in queue:
        cost = 0
        k = 0
        for j in i:
            cost += graph[k][j]
            k = j
        cost += graph[k][0]
        if min_cost > cost:
            min_cost = cost
    return min_cost

# USING ITERATIVE DEEPENING SEARCH
def tsp_ids_dfs(graph, start_node, visited, count, cost, depth):
    if count==len(graph):
        return cost + graph[start_node][0]
    elif count==depth:
        return 9999

    min_cost = 9999
    for i in range(len(graph)):
        if not visited[i] and graph[start_node][i]:
            visited[i] = True
            min_cost = min(min_cost, tsp_ids_dfs(graph, i, visited, count+1, cost+graph[start_node][i], depth))
            visited[i] = False
    return min_cost

def tsp_ids(graph, start_node):
    best_cost = 9999
    for depth in range(1, len(graph)+1):
        cost = tsp_ids_dfs(graph, start_node, visited, 0, 0, depth)
        best_cost = min(best_cost, cost)
    return best_cost



graph = [
    [0, 12, 10, 19, 8],
    [12, 0, 3, 7, 6],
    [10, 3, 0, 2, 20],
    [19, 7, 2, 0, 4],
    [8, 6, 20, 4, 0]
]
visited = [False] * len(graph)
start_node = 0

print(np.array(graph))

min_cost_using_dfs = tsp_dfs(graph, start_node, visited, 1, 0)
print("\nMinimun Cost Using DFS =", min_cost_using_dfs)

min_cost_using_bfs = tsp_bfs(graph)
print("\nMinimun Cost Using BFS =", min_cost_using_bfs)

min_cost_using_ids = tsp_ids(graph, start_node)
print("\nMinimun Cost Using IDS =", min_cost_using_ids)