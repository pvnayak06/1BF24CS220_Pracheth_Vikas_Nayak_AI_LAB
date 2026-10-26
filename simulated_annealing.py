import math
import random

def cost_function(state):
    # Example: minimize (x - 3)^2 + (y + 5)^2
    # Replace with the actual objective function given in lab
    x, y = state
    return (x - 3) ** 2 + (y + 5) ** 2

def neighbor_function(state):
    x, y = state
    new_x = x + random.uniform(-1, 1)
    new_y = y + random.uniform(-1, 1)
    return (new_x, new_y)

def simulated_annealing(initial_state, initial_temp=1000, cooling_rate=0.95, min_temp=0.01):
    current_state = initial_state
    current_cost = cost_function(current_state)
    temp = initial_temp
    step = 0

    while temp > min_temp:
        new_state = neighbor_function(current_state)
        new_cost = cost_function(new_state)
        delta = new_cost - current_cost

        if delta < 0:
            current_state = new_state
            current_cost = new_cost
        else:
            probability = math.exp(-delta / temp)
            if random.random() < probability:
                current_state = new_state
                current_cost = new_cost

        if step % 20 == 0:
            print(f"Step {step}: Temp = {temp:.3f}, State = {current_state}, Cost = {current_cost:.3f}")

        temp *= cooling_rate
        step += 1

    return current_state, current_cost

if __name__ == "__main__":
    start_x = float(input("Enter starting x: "))
    start_y = float(input("Enter starting y: "))

    initial_temp = float(input("Enter initial temperature (e.g. 1000): "))
    cooling_rate = float(input("Enter cooling rate (e.g. 0.95): "))

    initial_state = (start_x, start_y)
    best_state, best_cost = simulated_annealing(initial_state, initial_temp, cooling_rate)

    print(f"\nBest state found: {best_state}")
    print(f"Best cost: {best_cost:.3f}")
