"""
    CS20B1097 HIMANSHU
    TOWER OF HANOI
"""

def move(source, destination, disk):
    print(f"move top plate of {source} to {destination} tower.")

def move_disk(source_arr, destination_arr, source, destination):
    if len(source_arr)==0 and len(destination_arr)==0:
        pass

    elif len(source_arr)==0 or len(destination_arr)==0:
        if len(source_arr)==0:
            destination_top = destination_arr.pop(0)
            source_arr.append(destination_top)
            move(destination, source, destination_top)
        
        if len(destination_arr)==0:
            source_top = source_arr.pop(0)
            destination_arr.append(source_top)
            move(source, destination, source_top)

    else:
        source_top = source_arr.pop(0)
        destination_top = destination_arr.pop(0)
        if source_top > destination_top:
            source_arr.append(source_top)
            source_arr.append(destination_top)
            move(destination, source, destination_top)
        else:
            destination_arr.append(destination_top)
            destination_arr.append(destination_top)
            move(source, destination, source_top)

# Iterative approach to solve tower of hanoi
def toh_iterative(source, helper, destination, n):
    noOfMoves = pow(2, n) - 1
    source = [i for i in range(1, n+1)]
    helper = []
    destination = []

    if n%2==0:
        t = helper
        helper = destination
        destination = t

    for i in range(1, noOfMoves+1):
        if i%3==1:
            move_disk(source, destination, 'A', 'C')

        if i%3==2:
            move_disk(source, helper, 'A', 'B')

        if i%3==0:
            move_disk(destination, helper, 'C', 'B')

# Recursive approach to solve the tower of hanoi
def toh_recursive(source, helper, destination, n):
    if n==0:
        return

    toh_recursive(source, destination, helper, n-1)
    print(f"move plate {n} from {source} to {destination} tower.")
    toh_recursive(helper, source, destination, n-1)

print("------------RECURSIVE--------------")
toh_recursive('A', 'B', 'C', 3)

print("\n------------ITERATIVE--------------")
A = []
B = []
C = []
toh_iterative(A, B, C, 3)
