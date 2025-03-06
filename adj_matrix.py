from node import Node
import numpy as np
from lattice import Lattice

class AdjacencyMatrix():
    def __init__(self, N: int, lattice: Lattice) -> None:
        self.N = N
        self.lattice = lattice
        self.adjacency_matrix = np.zeros([self.N, self.N], dtype=int)
        self.generate_matrix()

    def generate_matrix(self):
        for node_idx in range(self.N):
            for other_node_idx in range(self.N):
                is_neighbor = self.lattice.is_neighbor(node_idx, other_node_idx)
                self.adjacency_matrix[node_idx][other_node_idx] = is_neighbor

    def get_lattice(self):
        return self.lattice

    def get_row(self, idx):
        return self.adjacency_matrix[idx]

    def get_matrix(self):
        return self.adjacency_matrix

    def get_element(self, row, col):
        return self.adjacency_matrix[row][col]

    def print_test(self):
        for node_idx in range(self.N):
            print(f"Elem at {node_idx}: {self.adjacency_matrix[node_idx]}")