import heapq

def a_star(graph, heuristic, start, goal):
    open_list = [(heuristic[start], 0, start, [start])]
    visited = {}

    while open_list:
        f, g, node, path = heapq.heappop(open_list)

        if node == goal:
            return path, g

        if node in visited and visited[node] <= g:
            continue
        visited[node] = g

        for neighbor, cost in graph.get(node, []):
            new_g = g + cost
            new_f = new_g + heuristic.get(neighbor, 0)
            heapq.heappush(open_list, (new_f, new_g, neighbor, path + [neighbor]))

    return None, float('inf')

def read_graph():
    print("Enter edges. Format: node neighbor cost  (one edge per line)")
    print("Enter a blank line when done.\n")
    graph = {}
    while True:
        line = input().strip()
        if line == "":
            break
        node, neighbor, cost = line.split()
        cost = float(cost)
        graph.setdefault(node, []).append((neighbor, cost))
    return graph

def read_heuristic():
    print("Enter heuristic values. Format: node value")
    print("Enter a blank line when done.\n")
    heuristic = {}
    while True:
        line = input().strip()
        if line == "":
            break
        node, value = line.split()
        heuristic[node] = float(value)
    return heuristic

if __name__ == "__main__":
    # Replace this block with the graph and heuristics given in lab,
    # or use read_graph()/read_heuristic() to enter them manually
    graph = {
        'A': [('B', 1), ('C', 4)],
        'B': [('D', 2), ('E', 5)],
        'C': [('F', 3)],
        'D': [],
        'E': [('G', 1)],
        'F': [('G', 2)],
        'G': []
    }
    heuristic = {'A': 6, 'B': 4, 'C': 4, 'D': 3, 'E': 1, 'F': 2, 'G': 0}

    use_custom = input("Enter custom graph and heuristic? (y/n): ").strip().lower()
    if use_custom == 'y':
        graph = read_graph()
        heuristic = read_heuristic()

    start = input("Enter start node: ").strip()
    goal = input("Enter goal node: ").strip()

    path, cost = a_star(graph, heuristic, start, goal)
    if path:
        print(f"\nPath: {' -> '.join(path)}")
        print(f"Total cost: {cost}")
    else:
        print("\nNo path found.")
