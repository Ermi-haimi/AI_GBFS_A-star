import heapq

class PathFinder:
    def __init__(self):
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

        # Good heuristic toward Akaky
        self.heuristic = {
            'Bole': 32,
            'Arada': 26,
            'Lafto': 24,
            'Yeka': 21,
            'Kirkos': 17,
            'Lideta': 28,
            'Kolfe': 17,
            'Gulele': 14,
            'Jemo': 15,
            'Akaky': 0
        }

    def get_neighbors(self, node):
        return list(self.graph[node].keys())

    def get_neighbors_with_cost(self, node):
        return self.graph[node]

    def get_cost(self, from_node, to_node):
        return self.graph[from_node].get(to_node, float('inf'))

    def display_graph(self):
        print("Graph Adjacency List:")
        for node, neighbors in self.graph.items():
            print(f"{node}: {neighbors}")

    def calculate_path_cost(self, path):
        cost = 0

        for i in range(len(path) - 1):
            cost += self.get_cost(path[i], path[i + 1])

        return cost
    
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
                path = []

                while current is not None:
                    path.append(current)
                    current = parent[current]

                path.reverse()

                return path, expansion_order

            for neighbor, cost in self.get_neighbors_with_cost(current).items():

                tentative_g = g_score[current] + cost

                if neighbor not in g_score or tentative_g < g_score[neighbor]:

                    g_score[neighbor] = tentative_g

                    h = self.heuristic[neighbor]

                    f = tentative_g + h

                    parent[neighbor] = current

                    heapq.heappush(open_list, (f, neighbor))

        return None, expansion_order
    
    
if __name__ == "__main__":

    pf = PathFinder()

    start = "Bole"
    goal = "Akaky"

    path, expansion_order = pf.a_star(start, goal)

    print("\n=== A* Search ===")

    if path:

        print("\nPath Found:")
        print(" -> ".join(path))

        print("\nNode Expansion Order:")
        print(" -> ".join(expansion_order))

        print("\nTotal Path Cost:")
        print(pf.calculate_path_cost(path))

    else:
        print("No path found.")