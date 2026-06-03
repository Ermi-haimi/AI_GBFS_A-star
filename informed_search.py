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
            'Bole': 35,
            'Arada': 29,
            'Lafto': 28,
            'Yeka': 25,
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