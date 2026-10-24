def dls(graph, node, goal, limit, path):
    if node == goal:
        return path + [node]
    if limit <= 0:
        return None
    for neighbor in graph.get(node, []):
        if neighbor not in path:
            result = dls(graph, neighbor, goal, limit - 1, path + [node])
            if result is not None:
                return result
    return None

def iterative_deepening_search(graph, start, goal, max_depth=10):
    for depth in range(max_depth + 1):
        print(f"Trying depth limit = {depth}")
        result = dls(graph, start, goal, depth, [])
        if result is not None:
            return result, depth
    return None, None

def read_graph():
    print("Enter the graph as edges. Format: node neighbor1 neighbor2 ...")
    print("Enter a blank line when done.\n")
    graph = {}
    while True:
        line = input().strip()
        if line == "":
            break
        parts = line.split()
        node, neighbors = parts[0], parts[1:]
        graph[node] = neighbors
    return graph

if __name__ == "__main__":
    # Replace this block with the graph given in lab, or use read_graph() to enter it manually
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['G'],
        'F': ['G'],
        'G': []
    }

    use_custom = input("Enter custom graph? (y/n): ").strip().lower()
    if use_custom == 'y':
        graph = read_graph()

    start = input("Enter start node: ").strip()
    goal = input("Enter goal node: ").strip()
    max_depth = int(input("Enter max depth to try: ").strip())

    path, depth_found = iterative_deepening_search(graph, start, goal, max_depth)
    if path:
        print(f"\nPath found at depth {depth_found}: {' -> '.join(path)}")
    else:
        print("\nNo path found within max depth.")
