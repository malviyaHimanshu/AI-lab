"""
    CS20B1097 HIMANSHU

    KNAPSACK PROBLEM USING HEURISTIC SEARCH

    Given, 
    Max Capacity : 400
        Value   Weight
    1   1000    10
    2   4000    300
    3   2000    100
    4   5000    1
    5   5000    200
"""

def sort_by_heuristic(e):
    return 1/e[2]

def knapsack(items, bag, max_capacity):
    for i in range(len(items)):
        # take the item if it doesn't exceed capacity
        if bag["weight"] + items[i][1] < max_capacity:
            bag["value"] += items[i][0]
            bag["weight"] += items[i][1]
            print(f"Item with value {items[i][0]} and weight {items[i][1]} added to the bag.")

    print(f"Bag Value = {bag['value']} and Weight = {bag['weight']}")

items = [
    [1000, 10],
    [4000, 300],
    [2000, 100],
    [5000, 1],
    [5000, 200],
]

bag = {"value": 0, "weight": 0}
max_capacity = 400

# Finding the Heuristic Values (value/weight)
items_with_heuristic = [(i + [round(i[0]/i[1])]) for i in items]
items_with_heuristic.sort(key=sort_by_heuristic)

knapsack(items_with_heuristic, bag, max_capacity=400)