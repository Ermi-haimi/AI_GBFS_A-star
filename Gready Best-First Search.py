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