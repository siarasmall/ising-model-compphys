from node import Node
import numpy as np
from lattice import Lattice

class AdjacencyMatrix():
    def __init__(self, N, width, height) -> None:
        self.N = N
        self.lattice = Lattice(N, width, height)
        self.AdjacencyMatrix = np.zeros([self.N, self.N], dtype=int)
        self.generate_matrix()

    def generate_matrix(self):
        for node_idx in range(self.N):
            for other_node_idx in range(self.N):
                is_neighbor = self.lattice.is_neighbor(node_idx, other_node_idx)
                self.AdjacencyMatrix[node_idx][other_node_idx] = is_neighbor

    def print_test(self):
        for node_idx in range(self.N):
            print(f"Elem at {node_idx}: {self.AdjacencyMatrix[node_idx]}")