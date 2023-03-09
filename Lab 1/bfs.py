'''
    CS20B1097 HIMANSHU
    - Python program for BFS (breadth first search)
'''

class AdjacencyNode:
    def __init__(self, value) -> None:
        self.data = value
        self.next = None

class Graph:
    def __init__(self, noOfVertices) -> None:
        self.vis = []
        self.q = []
        self.s = []
        self.V = noOfVertices
        self.graph = [None] * self.V # 2D array which represent the graph using adjacency list

    # function for adding the edge to the graph
    def add_edge(self, source, destination) -> None:
        destNode = AdjacencyNode(destination)
        destNode.next = self.graph[source]
        self.graph[source] = destNode

        srcNode = AdjacencyNode(source)
        srcNode.next = self.graph[destination]
        self.graph[destination] = srcNode

    # function for printing the graph
    def print_graph(self) -> None:
        for i in range(self.V):
            print()
            print(i, end="")
            temp = self.graph[i]
            while temp:
                print(" ->", temp.data, end="")
                temp = temp.next
        print()

    def BFS(self):
        visited = []
        queue = []
        queue.append(0)
        visited.append(0)
        while len(queue):
            temp = self.graph[queue[0]]
            queue.pop(0)
            while temp:
                if temp.data not in visited:
                    queue.append(temp.data)
                    visited.append(temp.data)
                temp = temp.next
        print(visited)

    def BFS_recursive(self, start_node):
        self.q.append(start_node)
        self.vis.append(start_node)
        temp = self.graph[start_node]
        self.q.pop(0)
        while temp:
            if temp.data not in self.vis:
                self.BFS_recursive(temp.data)
            temp = temp.next


    def DFS(self):
        visited = []
        stack = []
        stack.append(0)
        while len(stack):
            if stack[-1] not in visited:
                visited.append(stack[-1])
            temp = self.graph[stack[-1]]
            stack.pop()
            while temp:
                if temp.data not in visited:
                    stack.append(temp.data)
                temp = temp.next
        print(visited)


if __name__ == "__main__":
    V = int(input("Enter the number of vertices : "))
    graph = Graph(V)

    E = int(input("Enter the number of edges : "))
    while E>0:
        s, d = [int(x) for x in input("Enter an edge to add : ").split()]
        while s >= V or d >= V:
            print("[ERROR]: Value of the vertex must be between 0 and {}, Try again!\n".format(V-1))
            s, d = [int(x) for x in input("Enter an edge to add : ").split()]
        graph.add_edge(s, d)
        E -= 1

    graph.print_graph()
    graph.BFS()
    graph.DFS()
    