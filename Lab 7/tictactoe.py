"""
    CS20B1097 HIMANSHU 

    TIC TAC TOE USING ALPHA-BETA PRUNING ALOGRITHM
"""

import copy

# Constants
row_matched = [[(i+1, j+1) for j in range(3)] for i in range(3)]
column_matched = [[(j+1, i+1) for j in range(3)] for i in range(3)]
diagonal_match = [[(i+1, i+1) for i in range(3)]]
anti_diagonal_match = [[(i+1, 3-i) for i in range(3)]]
alpha = 'alpha'
beta = 'beta'
winning_array = row_matched + column_matched + diagonal_match + anti_diagonal_match

def empty_places(board):
    empty_place = 0
    for i in range(3):
        empty_place += board[i].count('_')
    return empty_place

def display_state(board):
    for i in range(3):
        for j in range(3):
            print(board[i][j], end=" ")
        print()
    print()

def winner(board, player):
    for i in winning_array:
        count = 0
        for j in i:
            if board[j[0]-1][j[1]-1] == player:
                count += 1
        if count==3:
            return 1
    return -1

def game_over(board):
    """
        -10 -> X wins
        10 -> O wins
        1 -> Draw
    """
    if winner(board, 'X')==1:
        return -10
    elif winner(board, 'O')==1:
        return 10
    else:
        empty_values = 0
        for i in range(3):
            empty_values += board[i].count('_')
        if empty_values == 0:
            return 1
    return False


class StateNode:
    def __init__(self, state, type, value, no_of_child) -> None:
        self.state = state  # current state of that node
        self.type = type    # type of node (alpha/beta)
        self.value = value
        self.child = no_of_child

    def display(self):
        display_state(self.state)
        print(f"<{self.type}, {self.value}, {self.child}>")


def alpha_beta_pruning(board, flag):
    visited = []
    stack = []
    stack.append(StateNode(board, alpha, -9999, empty_places(board)))

    count = 0
    visited.append(StateNode(board, alpha, -9999, empty_places(board)))
    while len(visited)>0:
        if count==0:
            visited.pop()
        count=1

        if game_over(stack[-1].state):
            stack[-1].value = game_over(stack[-1].state)
            stack[-1].child = 0
        state = stack.pop()
        visited.append(state)
        # board = visited[-1].state

        if visited[-1].child == 0:
            while visited[-1].child == 0:
                node = visited.pop()

                if len(visited) == 0:
                    # value of root node
                    return node.value
                
                if visited[-1].type == alpha:
                    visited[-1].value = max(visited[-1].value, node.value)
                    if visited[-1].value == 10:
                        while visited[-1].child > 1:
                            stack.pop()
                            visited[-1].child -= 1
                elif visited[-1].type == beta:
                    visited[-1].value = min(visited[-1].value, node.value)
                    if visited[-1].value == -10:
                        while visited[-1].child > 1:
                            stack.pop()
                            visited[-1].child -= 1
                visited[-1].child -= 1
                flag = beta if flag==alpha else alpha
            continue
        
        board = visited[-1].state
        flag = beta if flag==alpha else alpha
        if not game_over(board):
            for i in range(3):
                for j in range(3):
                    if board[i][j] == '_':
                        if flag == alpha:
                            # X turn
                            board[i][j] = 'X'
                            newstate = copy.deepcopy(StateNode(board, alpha, -9999, empty_places(board)))
                            stack.append(newstate)
                            board[i][j] = '_'

                        elif flag == beta:
                            # O turn
                            board[i][j] = 'O'
                            newstate = copy.deepcopy(StateNode(board, beta, 9999, empty_places(board)))
                            stack.append(newstate)
                            board[i][j] = '_'


def mapping(move):
    if move.lower()=='o': return 'O'
    elif move.lower()=='x': return 'X'
    else: return '_'

board = []
choice = input("Would you like to add initial configuration manually? (y/N) : ")
if choice.lower()=='y':
    print('\n> for players use \'X\' and \'O\'')
    print('> for empty spaces write \'n\'')
    for i in range(3):
        play = list(map(mapping, (input(f"Enter row {i+1} : ").strip().split(" "))))
        board.append(play)
    print()
else:
    board = [
        ['O', 'O', 'X'],
        ['_', 'X', '_'],
        ['O', 'X', '_'],
    ]

display_state(board)

will_win = alpha_beta_pruning(board, alpha)
if will_win==10:
    print("O wins")
elif will_win==-10:
    print("X wins")
elif will_win==1:
    print("Draw")
else:
    print("Goli beta, Masti nahi.")