import heapq

def heuristic(state, goal):
    return sum(1 for i in range(9) if state[i] != 0 and state[i] != goal[i])

def get_neighbors(state):
    neighbors = []
    idx = state.index(0)
    row, col = idx // 3, idx % 3
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right

    for dr, dc in moves:
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_idx = new_row * 3 + new_col
            new_state = list(state)
            new_state[idx], new_state[new_idx] = new_state[new_idx], new_state[idx]
            neighbors.append(tuple(new_state))

    return neighbors

def print_state(state):
    for i in range(0, 9, 3):
        print(state[i:i+3])
    print()

def solve_8_puzzle(start, goal):
    counter = 0  # tie-breaker for heapq
    open_list = [(heuristic(start, goal), 0, counter, start, [])]
    visited = {}

    while open_list:
        f, g, _, state, path = heapq.heappop(open_list)

        if state == goal:
            return path + [state]

        if state in visited and visited[state] <= g:
            continue
        visited[state] = g

        for neighbor in get_neighbors(state):
            new_g = g + 1
            new_f = new_g + heuristic(neighbor, goal)
            counter += 1
            heapq.heappush(open_list, (new_f, new_g, counter, neighbor, path + [state]))

    return None

def read_state(prompt):
    print(prompt + " (enter 9 numbers 0-8, space-separated, 0 = blank):")
    while True:
        try:
            values = list(map(int, input().split()))
            if len(values) == 9 and sorted(values) == list(range(9)):
                return tuple(values)
            print("Invalid input. Enter exactly 9 numbers, each from 0-8, with no repeats.")
        except ValueError:
            print("Invalid input. Enter numbers only, space-separated.")

if __name__ == "__main__":
    start = read_state("Enter start state")
    goal = read_state("Enter goal state")

    solution = solve_8_puzzle(start, goal)

    if solution:
        print(f"\nSolved in {len(solution) - 1} moves:\n")
        for step in solution:
            print_state(step)
    else:
        print("No solution found.")
