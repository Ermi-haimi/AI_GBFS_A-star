import heapq

graph = {
    'Bole':   {'Arada': 6,  'Lafto': 9},
    'Arada':  {'Bole': 6,   'Yeka': 5,   'Kirkos': 12},
    'Lafto':  {'Bole': 9,   'Lideta': 7, 'Kolfe': 11},
    'Yeka':   {'Arada': 5,  'Kirkos': 4, 'Gulele': 8},
    'Kirkos': {'Arada': 12, 'Yeka': 4,   'Gulele': 3, 'Jemo': 10},
    'Lideta': {'Lafto': 7,  'Jemo': 13},
    'Kolfe':  {'Lafto': 11, 'Jemo': 2},
    'Gulele': {'Yeka': 8,   'Kirkos': 3, 'Jemo': 1,   'Akaky': 14},
    'Jemo':   {'Lideta': 13,'Kirkos': 10,'Kolfe': 2,  'Gulele': 1, 'Akaky': 15},
    'Akaky':  {'Gulele': 14,'Jemo': 15},
}

heuristic_original = {
    'Bole': 32, 'Arada': 26, 'Lafto': 24, 'Yeka': 21,
    'Kirkos': 17, 'Lideta': 28, 'Kolfe': 17,
    'Gulele': 14, 'Jemo': 15, 'Akaky': 0,
}

heuristic_good = {
    'Bole': 28, 'Arada': 22, 'Lafto': 20, 'Yeka': 18,
    'Kirkos': 15, 'Lideta': 14, 'Kolfe': 2,
    'Gulele': 13, 'Jemo': 14, 'Akaky': 0,
}

heuristic_misleading = {
    'Bole': 10, 'Arada': 50, 'Lafto': 5, 'Yeka': 60,
    'Kirkos': 55, 'Lideta': 3, 'Kolfe': 40,
    'Gulele': 50, 'Jemo': 1, 'Akaky': 0,
}


class Node:
    def __init__(self, name, priority):
        self.name = name
        self.priority = priority
    def __lt__(self, other):
        return self.priority < other.priority


def gbfs(graph, start, goal, heuristic):
    pq = []
    heapq.heappush(pq, Node(start, heuristic[start]))
    visited = set()
    parent = {start: None}
    expansion_order = []

    while pq:
        current = heapq.heappop(pq).name
        if current in visited:
            continue
        visited.add(current)
        expansion_order.append(current)

        if current == goal:
            return reconstruct(parent, goal), expansion_order

        for neighbor in graph[current]:
            if neighbor not in visited:
                heapq.heappush(pq, Node(neighbor, heuristic[neighbor]))
                if neighbor not in parent:
                    parent[neighbor] = current

    return None, expansion_order


def a_star(graph, start, goal, heuristic):
    pq = []
    g = {start: 0}
    heapq.heappush(pq, (g[start] + heuristic[start], start))
    parent = {start: None}
    visited = set()
    expansion_order = []

    while pq:
        _, current = heapq.heappop(pq)
        if current in visited:
            continue
        visited.add(current)
        expansion_order.append(current)

        if current == goal:
            return reconstruct(parent, goal), expansion_order

        for neighbor, cost in graph[current].items():
            tentative_g = g[current] + cost
            if neighbor not in g or tentative_g < g[neighbor]:
                g[neighbor] = tentative_g
                parent[neighbor] = current
                heapq.heappush(pq, (tentative_g + heuristic[neighbor], neighbor))

    return None, expansion_order


def reconstruct(parent, goal):
    path, cur = [], goal
    while cur is not None:
        path.append(cur)
        cur = parent[cur]
    path.reverse()
    return path


def path_cost(graph, path):
    if not path:
        return 0
    return sum(graph[path[i]][path[i+1]] for i in range(len(path)-1))


experiments = [
    ("ORIGINAL",   heuristic_original),
    ("GOOD",       heuristic_good),
    ("MISLEADING", heuristic_misleading),
]

START, GOAL = 'Bole', 'Akaky'

print("     EXPERIMENTAL EXPLORATION & TESTING")
print("     Graph: Addis Ababa sub-cities | Bole -> Akaky")


results_table = []

for label, h in experiments:
    
    print(f"  HEURISTIC SET: {label}")
    print(f"{'─'*65}")
    print("  h(n) values:")
    for node, val in h.items():
        print(f"    {node:<10} h = {val}")

    for algo_name, algo_fn in [("GBFS", gbfs), ("A*", a_star)]:
        path, order = algo_fn(graph, START, GOAL, h)
        cost = path_cost(graph, path) if path else None

        print(f"\n  [{algo_name}]")
        if path:
            print(f"    Path Found      : {' -> '.join(path)}")
            print(f"    Total Path Cost : {cost}")
            print(f"    Nodes Expanded  : {len(order)}  ({' -> '.join(order)})")
        else:
            print("    No path found.")

        results_table.append({
            "heuristic": label,
            "algorithm": algo_name,
            "cost": cost,
            "nodes_expanded": len(order),
        })


print("  COMPARISON SUMMARY TABLE")

print(f"{'Heuristic':<12} {'Algo':<6} {'Path Cost':<12} {'Nodes Expanded'}")
print("-" * 50)
for r in results_table:
    cost_str = str(r['cost']) if r['cost'] is not None else "None"
    print(f"{r['heuristic']:<12} {r['algorithm']:<6} {cost_str:<12} {r['nodes_expanded']}")