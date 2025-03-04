from node import Node
import numpy as np
from lattice import SquareLattice

class Adjacency_matrix():
    # list of lists
    def __init__(self, N, width, height) -> None:
        self.N = N
        self.lattice = SquareLattice(N, width, height)
        self.adjacency_matrix = np.zeros([self.N, self.N], dtype=int)
        self.generate_matrix()

    def generate_matrix(self):
        for node_idx in range(self.N):
            for other_node_idx in range(self.N):
                is_neighbor = self.lattice.is_neighbor(node_idx, other_node_idx)
                self.adjacency_matrix[node_idx][other_node_idx] = is_neighbor

    def print_test(self):
        for node_idx in range(self.N):
            print(f"Elem at {node_idx}: {self.adjacency_matrix[node_idx]}")