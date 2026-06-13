import heapq

class Node:
    def __init__(self, name, priority):
        self.name = name
        self.priority = priority

    def __lt__(self, other):
        return self.priority < other.priority


class PathFinder:
    def __init__(self):
        # Unified graph 
        self.graph = {
            'Bole': {'Arada': 6, 'Lafto': 9},
            'Arada': {'Bole': 6, 'Yeka': 5, 'Kirkos': 12},
            'Lafto': {'Bole': 9, 'Lideta': 7, 'Kolfe': 11},
            'Yeka': {'Arada': 5, 'Kirkos': 4, 'Gulele': 8},
            'Kirkos': {'Arada': 12, 'Yeka': 4, 'Gulele': 3, 'Jemo': 10},
            'Lideta': {'Lafto': 7, 'Jemo': 13},
            'Kolfe': {'Lafto': 11, 'Jemo': 2},
            'Gulele': {'Yeka': 8, 'Kirkos': 3, 'Jemo': 1, 'Akaky': 14},
            'Jemo': {'Lideta': 13, 'Kirkos': 10, 'Kolfe': 2, 'Gulele': 1, 'Akaky': 15},
            'Akaky': {'Gulele': 14, 'Jemo': 15}
        }

        self.heuristic = {
            'Bole': 32, 'Arada': 26, 'Lafto': 24, 'Yeka': 21,
            'Kirkos': 17, 'Lideta': 28, 'Kolfe': 17, 'Gulele': 14,
            'Jemo': 15, 'Akaky': 0
        }

    def get_neighbors_with_cost(self, node):
        return self.graph[node]

    def get_cost(self, from_node, to_node):
        return self.graph[from_node].get(to_node, float('inf'))

    def calculate_path_cost(self, path):
        if not path:
            return 0
        cost = 0
        for i in range(len(path) - 1):
            cost += self.get_cost(path[i], path[i + 1])
        return cost

    def reconstruct_path(self, parent, start, goal):
        current = goal
        path = []
        while current is not None:
            path.append(current)
            current = parent.get(current)
        path.reverse()
        return path

    # 1. Greedy Best-First Search
    def greedy_best_first_search(self, start, goal):
        priority_queue = []
        heapq.heappush(priority_queue, Node(start, self.heuristic[start]))

        visited = set()
        frontier = {start}  # prevents duplicate
        parent = {start: None}
        expansion_order = []

        while priority_queue:
            current_node = heapq.heappop(priority_queue).name
            frontier.discard(current_node)

            if current_node in visited:
                continue

            visited.add(current_node)
            expansion_order.append(current_node)

            if current_node == goal:
                return self.reconstruct_path(parent, start, goal), expansion_order

            for neighbor in self.graph[current_node]:
                if neighbor not in visited and neighbor not in frontier:
                    heapq.heappush(
                        priority_queue,
                        Node(neighbor, self.heuristic[neighbor])
                    )
                    frontier.add(neighbor)
                    parent[neighbor] = current_node

        return None, expansion_order

    # 2. A* Search
    def a_star(self, start, goal):
        open_list = []
        g_score = {start: 0}
        start_f = g_score[start] + self.heuristic[start]
        heapq.heappush(open_list, (start_f, start))

        parent = {start: None}
        expansion_order = []
        visited = set()

        while open_list:
            _, current = heapq.heappop(open_list)

            if current in visited:
                continue

            visited.add(current)
            expansion_order.append(current)

            if current == goal:
                return self.reconstruct_path(parent, start, goal), expansion_order

            for neighbor, cost in self.get_neighbors_with_cost(current).items():
                tentative_g = g_score[current] + cost

                if neighbor not in g_score or tentative_g < g_score[neighbor]:
                    g_score[neighbor] = tentative_g
                    f = tentative_g + self.heuristic[neighbor]
                    parent[neighbor] = current
                    heapq.heappush(open_list, (f, neighbor))

        return None, expansion_order


if __name__ == "__main__":
    pf = PathFinder()
    start_node = "Bole"
    goal_node = "Akaky"

    # Run Greedy Best-First Search
    gb_path, gb_expansion = pf.greedy_best_first_search(start_node, goal_node)
    print("\n=== Greedy Best-First Search ===")
    if gb_path:
        print("Path Found:", " -> ".join(gb_path))
        print("Node Expansion Order:", " -> ".join(gb_expansion))
        print("Total Path Cost:", pf.calculate_path_cost(gb_path))
    else:
        print("No path found.")

    # Run A* Search
    a_path, a_expansion = pf.a_star(start_node, goal_node)
    print("\n=== A* Search ===")
    if a_path:
        print("Path Found:", " -> ".join(a_path))
        print("Node Expansion Order:", " -> ".join(a_expansion))
        print("Total Path Cost:", pf.calculate_path_cost(a_path))
    else:
        print("No path found.")