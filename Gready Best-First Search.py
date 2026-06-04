import heapq

# Node representation
class Node:
    def __init__(self, name, heuristic):
        self.name = name
        self.heuristic = heuristic

    def __lt__(self, other):
        return self.heuristic < other.heuristic


# Greedy Best First Search
def greedy_best_first_search(graph, start, goal, heuristic):
    priority_queue = []
    heapq.heappush(priority_queue, Node(start, heuristic[start]))

    visited = set()
    path = {start: None}
    expansion_order = []

    while priority_queue:
        current_node = heapq.heappop(priority_queue).name

        if current_node not in expansion_order:
            expansion_order.append(current_node)

        if current_node == goal:
            return reconstruct_path(path, start, goal), expansion_order

        visited.add(current_node)

        for neighbor in graph[current_node]:
            if neighbor not in visited:
                heapq.heappush(priority_queue, Node(neighbor, heuristic[neighbor]))

                if neighbor not in path:
                    path[neighbor] = current_node

    return None, expansion_order


# Reconstruct path
def reconstruct_path(path, start, goal):
    current = goal
    result_path = []

    while current is not None:
        result_path.append(current)
        current = path[current]

    result_path.reverse()
    return result_path

def calculate_path_cost(path, edge_weights):
    if not path:
        return 0
    total_cost = 0
    for i in range(len(path) - 1):
        u, v = path[i], path[i+1]
        if (u, v) in edge_weights:
            total_cost += edge_weights[(u, v)]
        elif (v, u) in edge_weights:
            total_cost += edge_weights[(v, u)]
    return total_cost




# Graph and heuristic data
graph = {
    'Bole': ['Arada', 'Lafto'],
    'Arada': ['Bole', 'Yeka', 'Kirkos'],
    'Lafto': ['Bole', 'Lideta', 'Kolfe'],
    'Yeka': ['Arada', 'Kirkos', 'Gulele'],
    'Kirkos': ['Arada', 'Yeka', 'Gulele', 'Jemo'],
    'Lideta': ['Lafto', 'Jemo'],
    'Kolfe': ['Lafto', 'Jemo'],
    'Gulele': ['Yeka', 'Kirkos', 'Jemo', 'Akaky'],
    'Jemo': ['Lideta', 'Kirkos', 'Kolfe', 'Gulele', 'Akaky'],
    'Akaky': ['Gulele', 'Jemo']
}

edge_weights = {
    ('Bole', 'Arada'): 6, ('Bole', 'Lafto'): 9,
    ('Arada', 'Yeka'): 5, ('Arada', 'Kirkos'): 12,
    ('Lafto', 'Lideta'): 7, ('Lafto', 'Kolfe'): 11,
    ('Yeka', 'Kirkos'): 4, ('Yeka', 'Gulele'): 8,
    ('Kirkos', 'Gulele'): 3, ('Kirkos', 'Jemo'): 10,
    ('Lideta', 'Jemo'): 13, ('Kolfe', 'Jemo'): 2,
    ('Gulele', 'Jemo'): 1, ('Gulele', 'Akaky'): 14,
    ('Jemo', 'Akaky'): 15
}

heuristic = {
    'Bole': 32, 'Arada': 26, 'Lafto': 24, 'Yeka': 21,
    'Kirkos': 17, 'Lideta': 28, 'Kolfe': 17, 'Gulele': 14,
    'Jemo': 15, 'Akaky': 0
}

# Coordinates for visualization
pos = {
    'Bole': (0.0, 4.0),
    'Arada': (2.0, 4.5),
    'Lafto': (1.2, 2.3),
    'Yeka': (4.5, 4.5),
    'Kirkos': (3.8, 2.7),
    'Lideta': (2.8, 1.8),
    'Kolfe': (2.4, 0.2),
    'Gulele': (6.0, 2.6),
    'Jemo': (5.0, 0.2),
    'Akaky': (7.0, 0.2)
}


# Test the Greedy Best-First Search
start_node = 'Bole'
goal_node = 'Akaky'

result_path, expansion_order = greedy_best_first_search(
    graph,
    start_node,
    goal_node,
    heuristic
)

print("\n=== Greedy Best-First Search ===")
if result_path:
    print("\nPath Found:")
    print(" -> ".join(result_path))
    
    print("\nNode Expansion Order:")
    print(" -> ".join(expansion_order))
    
    print("\nTotal Path Cost:")
    print(calculate_path_cost(result_path, edge_weights))