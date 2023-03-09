"""
    CS20B1097 HIMANSHU
    WATER JUG PROBLEM

        Given two water jugs with capacities X and Y litres. Initially, both the jugs are empty. 
        Also given that there is an infinite amount of water available. 
        The jugs do not have markings to measure smaller quantities.

        One can perform the following operations on the jug:
        - Fill any of the jugs completely with water.
        - Pour water from one jug to the other until one of the jugs is either empty or full, (X, Y) -> (X - d, Y + d)
        - Empty any of the jugs
        - The task is to determine whether it is possible to measure Z litres of water using both the jugs. And if true, print any of the possible ways.
"""

def measure_using_two_jug(x, y, z):
    queue = [((0,0), [])]
    visited = set()

    while queue:
        state, steps = queue.pop(0)
        if state[0] == z or state[1] == z:
            print(f"\nIt is possible to measure {z} litres of water using following steps : ")
            for step in steps:
                print(step)
            return state

        if state not in visited:
            visited.add(state)
            states = [
                (x, state[1]),
                (state[0], y),
                (0, state[1]),
                (state[0], 0),
                (state[0] - min(state[0], y-state[1]), state[1] + min(state[0], y-state[1])),
                (state[0] + min(state[1], x-state[0]), state[1] - min(state[1], x-state[0]))
            ]

            for next_state in states:
                if next_state[0] >= 0 and next_state[1] >= 0:
                    next_steps = steps.copy()
                    next_steps.append(next_state)
                    queue.append((next_state, next_steps))

    print(f"\nSorry, it is not possible to measure {z} litres of water using both the jugs.")

x = int(input("Enter the capacity of First Jug : "))
y = int(input("Enter the capacity of Second Jug : "))
z = int(input("Enter the water amount to be measured : "))

measure_using_two_jug(x, y, z)