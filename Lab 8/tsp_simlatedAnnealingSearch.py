"""
    CS20B1097 HIMANSHU

    SOLVING TRAVELLING SALESMAN PROBLEM USING SIMULATED ANNEALING SEACH
"""

import numpy as np
import random
import copy
import matplotlib.pyplot as plt


def distance(p1: tuple, p2: tuple) -> float:
    dist = (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2
    return np.sqrt(dist)

def dec_temp(current_temperature):
    return current_temperature * alpha

def probablity(current_energy, next_energy, current_temperature):
    return np.exp(-(next_energy-current_energy)/current_temperature)

def calculate_distance(path):
    total_dist = 0
    for i in range(len(path)):
        if i<len(path)-1:
            total_dist += distance_matrix[ord(path[i])-65][ord(path[i+1])-65]
        else:
            total_dist += distance_matrix[ord(path[i])-65][ord(path[0])-65]
    return total_dist

def random_swap(state):
    new_state = copy.deepcopy(state)
    i1, i2 = random.sample(range(len(state)), 2)
    new_state[i1], new_state[i2] = new_state[i2], new_state[i1]
    return new_state

def is_accepted(current_state, new_state, temp):
    current_energy = calculate_distance(current_state)
    new_energy = calculate_distance(new_state)
    random_number = random.uniform(0, 1)
    if new_energy < current_energy:
        return True
    elif probablity(current_energy, new_energy, temp) > random_number:
        return True
    return False



n = 10
number_of_cities = 15
temperature = 1e+10
alpha = 0.97
n_iterations = 1000
grid = np.zeros((n, n), dtype='int')

x = np.random.randint(0, n, number_of_cities)
y = np.random.randint(0, n, number_of_cities)

coords = [(x[i], y[i]) for i in range(len(x))]
coords = list(set(coords))
while len(coords) < number_of_cities:
    x1 = np.random.randint(0, n)
    y1 = np.random.randint(0, n)
    if coords.count((x1, y1)) == 0:
        coords.append((x1, y1))

cities_with_location = {chr(i+65): coords[i] for i in range(len(coords))}
cities = [chr(i+65) for i in range(number_of_cities)]

# Instead of calculating distances again and again, store it in adjacency matrix
distance_matrix = np.zeros((number_of_cities, number_of_cities), dtype='double')
for i in range(len(distance_matrix)):
    for j in range(len(distance_matrix[i])):
        distance_matrix[i][j] = distance(cities_with_location[chr(i+65)], cities_with_location[chr(j+65)])


initial_state = np.random.permutation(cities)
print(f"Initial State : {initial_state}\tEnergy : {calculate_distance(initial_state)}\tTemperature : {temperature}")

best_state = initial_state
best_cost = calculate_distance(initial_state)
best_costs = []
cost = []

i = n_iterations
while i>0:
    new_state = random_swap(initial_state)
    energy_value = calculate_distance(new_state)

    if energy_value < best_cost:
        best_state = new_state
        best_cost = energy_value
    best_costs.append(best_cost)

    if is_accepted(initial_state, new_state, temperature):
        initial_state = copy.deepcopy(new_state)

    cost.append(energy_value)
    temperature = dec_temp(temperature)
    i -= 1
    print(f"Current State : {new_state}\tEnergy : {energy_value}\tTemperature : {temperature}")

print("\n ---------------------------------------------------------------------------------------------------------------- ")
print(f"| Final Solution : {best_state}\tCost : {calculate_distance(best_state)} |")
print(" ---------------------------------------------------------------------------------------------------------------- \n")


plt.subplot(1,2,1)
plt.plot(range(n_iterations), cost)
plt.plot(range(n_iterations), best_costs)
plt.title("Iteration v/s Cost graph")
plt.xlabel("Iterations")
plt.ylabel("Cost")

x_updated = [cities_with_location[i][1]+1 for i in best_state]
y_updated = [n-cities_with_location[i][0] for i in best_state]

plt.subplot(1,2,2)
plt.scatter(x_updated, y_updated, c='red')
for i in range(number_of_cities):
    plt.annotate(best_state[i], (x_updated[i]+0.1, y_updated[i]+0.15))

x_updated.append(x_updated[0])
y_updated.append(y_updated[0])
plt.plot(x_updated, y_updated, color='green')
plt.title(f"Final Solution (cost={round(calculate_distance(best_state), 2)})")

plt.show()