"""
    CS20B1097 HIMANSHU

    8-PUZZLE PROBLEM USING A* SEARCH
"""

import copy

n = 3
goal = [
    ['1', '2', '3'],
    ['8', '_', '4'],
    ['7', '6', '5']
]

"""
here, g(n) = depth of the node
      h(n) = number of misplace tiles
      f(n) = g(n) + h(n)
"""
class StateNode:
    def __init__(self, puzzle, depth) -> None:
        self.state = puzzle
        self.gn = depth
        self.hn = self.calculate_heuristic()
        self.fn = self.gn + self.hn

    def calculate_heuristic(self) -> int:
        matrix = self.state
        misplaced_tiles = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] != goal[i][j] and matrix[i][j] != '_':
                    misplaced_tiles+=1
        return misplaced_tiles
    
    def generate_child(self):
        x,y = self.find(self.state, '_')
        moves = [[x,y-1],[x,y+1],[x-1,y],[x+1,y]]
        children = []
        for i in moves:
            child = self.move(x,y,i[0],i[1])
            if child is not None:
                child_node = StateNode(child, self.gn+1)
                children.append(child_node)
        return children

    def find(self, puzzle, x):
        for i in range(len(puzzle)):
            for j in range(len(puzzle)):
                if puzzle[i][j] == x:
                    return i,j
                
    def move(self, x1, y1, x2, y2):
        if 0 <= x2 < len(self.state) and 0 <= y2 < len(self.state):
            temp_puzzle = copy.deepcopy(self.state)
            temp = temp_puzzle[x1][y1]
            temp_puzzle[x1][y1] = temp_puzzle[x2][y2]
            temp_puzzle[x2][y2] = temp
            return temp_puzzle
        else:
            return None
        
    def display(self):
        print("--------")
        for i in self.state:
            for j in i:
                print(j, end=" ")
            print()
        print("--------")
        print(f"g(n) = {self.gn}\nf(n) = {self.fn}")
        print("--------\n\n")


def A_Star_search(initial_state):
    initial_node = StateNode(initial_state, 0)
    initial_node.display()

    OPEN = []
    CLOSED = []
    OPEN.append(initial_node)

    while True:
        current = OPEN[0]
        current.display()

        if(current.calculate_heuristic() == 0):
            print("GOAL REACHED")
            break

        for i in current.generate_child():
            OPEN.append(i)
        CLOSED.append(current)
        del OPEN[0]

        OPEN.sort(key = lambda x:x.fn, reverse=False)


initial_state = [
    ['2', '8', '3'],
    ['1', '6', '4'],
    ['7', '_', '5']
]

A_Star_search(initial_state)


