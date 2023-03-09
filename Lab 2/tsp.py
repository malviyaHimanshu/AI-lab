'''
    CS20B1097 HIMANSHU 
    TRAVELLING SALESMAN PROBLEM
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
    [0, 12, 10, 19, 8],
    [12, 0, 3, 7, 6],
    [10, 3, 0, 2, 20],
    [19, 7, 2, 0, 4],
    [8, 6, 20, 4, 0]
]
visited = [False] * len(graph)
# considering A as starting node
start_node = 0

min_cost = tsp(graph, start_node, visited, 1, 0)
print(np.array(graph))
print("\nMinimun Cost =", min_cost)