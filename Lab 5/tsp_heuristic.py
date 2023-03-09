"""
    CS20B1097 HIMANSHU

    TRAVELLING SALESMAN PROBLEM USING HEURISTIC BY A* ALGORITHM

    The heuristic function is as follows:
    h(n) = COST OF MINIMUM COST SPANNING TREE OF REMAINING NODES
"""

import heapq

# HEURISTIC COST USING MINIMUM SPANNING TREE
def heuristic_cost(graph, remaining_nodes, current_node, minimum_spanning_tree_cost):
    return minimum_spanning_tree_cost + sum(graph[current_node][j] for j in remaining_nodes)


# USING A*
def tsp_a_star(graph, heuristic, visited, start_node):
    cost = 0
    f = heuristic[start_node]

    pq = [(f, start_node, visited[:], cost)]

    while pq:
        f, node, visited, cost = heapq.heappop(pq)

        if all(visited) and node == start_node:
            cost += graph[node][start_node]
            return cost

        for i in range(len(graph)):
            if not visited[i] and i != node:
                g = cost + graph[node][i]
                h = heuristic[i]
                f = g + h

                visited[i] = True
                heapq.heappush(pq, (f, i, visited[:], g))
                visited[i] = False

    return 9999


graph = [
    [0, 12, 10, 19, 8],
    [12, 0, 3, 7, 6],
    [10, 3, 0, 2, 20],
    [19, 7, 2, 0, 4],
    [8, 6, 20, 4, 0]
]
visited = [False] * len(graph)
start_node = 0

# heuristic = heuristic_cost(graph, [1, 2, 3, 4], 0, 0)
# print(heuristic)
heuristic = [9, 14, 18, 17, 15]

min_cost_using_a_star = tsp_a_star(graph, heuristic, visited, 0)
print("\nMinimun Cost Using A* =", min_cost_using_a_star)