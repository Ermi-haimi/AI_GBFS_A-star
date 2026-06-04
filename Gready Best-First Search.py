import heapq
import networkx as nx
import matplotlib.pyplot as plt

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