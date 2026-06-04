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

#Visualizer




def visualize_graph(graph, edge_weights, path, pos):
    G = nx.Graph()

    for node, neighbors in graph.items():
        for neighbor in neighbors:
            if (node, neighbor) in edge_weights:
                G.add_edge(node, neighbor, weight=edge_weights[(node, neighbor)])
            elif (neighbor, node) in edge_weights:
                G.add_edge(node, neighbor, weight=edge_weights[(neighbor, node)])

    plt.figure(figsize=(12, 7))

    color_map = {
        'Bole': '#a1d99b',    # Light Green
        'Arada': '#bdd7e7',   # Light Blue
        'Lafto': '#fddaec',   # Pale Yellow/Beige
        'Yeka': '#fbb4ae',    # Pink
        'Kirkos': '#cbd5e8',  # Purple
        'Lideta': '#ccebc5',  # Cyan/Teal
        'Kolfe': '#decbe4',   # Periwinkle Blue
        'Gulele': '#fed9a6',  # Peach/Tan
        'Jemo': '#b3cde3',    # Mint Green
        'Akaky': '#fbb4ae'    # Red/Coral
    }
    
    # alternative fallback
    node_colors = [
        '#adebad' if n == 'Bole' or n == 'Jemo' else
        '#b3d9ff' if n == 'Arada' else
        '#ffe699' if n == 'Lafto' or n == 'Gulele' else
        '#ffb3d9' if n == 'Yeka' else
        '#ccb3ff' if n == 'Kirkos' else
        '#b3f0ff' if n == 'Lideta' else
        '#cce0ff' if n == 'Kolfe' else
        '#ff8080' if n == 'Akaky' else '#skyblue'
        for n in G.nodes()
    ]

    # Draw edges
    nx.draw_networkx_edges(G, pos, edge_color="black", width=1.2)

    # Draw nodes
    nx.draw_networkx_nodes(
        G,
        pos,
        nodelist=list(G.nodes()),
        node_color=node_colors,
        node_size=2500,
        edgecolors='black',
        linewidths=1
    )

    nx.draw_networkx_labels(G, pos, font_size=11, font_weight="bold", font_color="black")

    # Draw Edge Weights 
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_size=11, font_weight="bold")

    if path:
        path_edges = list(zip(path, path[1:]))
        nx.draw_networkx_edges(
            G,
            pos,
            edgelist=path_edges,
            edge_color="#2ca02c",  
            width=4.5
        )

    plt.text(pos['Bole'][0], pos['Bole'][1] + 0.4, "Start Node", color="green", weight="bold", fontsize=12, ha="center")
    plt.text(pos['Akaky'][0], pos['Akaky'][1] - 0.4, "Goal Node", color="red", weight="bold", fontsize=12, ha="center")

    plt.title("Greedy Best-First Search", fontsize=14, weight="bold")
    plt.axis('off')
    plt.tight_layout()
    plt.show()
