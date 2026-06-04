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