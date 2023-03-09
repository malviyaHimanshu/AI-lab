'''
    CS20B1097 HIMANSHU 
    TRAVELLING SALESMAN PROBLEM USING DEPTH FIRST SEARCH (DFS)
'''

import numpy as np

def tsp(graph, start_node, visited, count, cost):
    if count==len(graph) and graph[start_node][0]:
        return cost + graph[start_node][0]

    min_cost = 9999
    for i in range(len(graph)):
        if not visited[i] and graph[start_node][i]:
            visited[i] = True
            min_cost = min(min_cost, tsp(graph, i, visited, count+1, cost+graph[start_node][i]))
            visited[i] = False
    return min_cost

# given graph in the question
graph = [
    [0, 10, 50, 300, 0, 0, 0],
    [10, 0, 30, 40, 0, 0, 65],
    [50, 30, 0, 0, 20, 76, 0],
    [300, 40, 0, 0, 60, 0, 0],
    [0, 0, 20, 60, 0, 0, 37],
    [0, 0, 76, 0, 0, 0, 45],
    [0, 65, 0, 0, 37, 45, 0]
]
visited = [False] * len(graph)
# considering A as starting node
start_node = 0

min_cost = tsp(graph, start_node, visited, 1, 0)
print(np.array(graph))
print("\nMinimun Cost =", min_cost)