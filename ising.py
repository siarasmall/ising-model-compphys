import numpy as np 
from lattice import Lattice
from adj_matrix import AdjacencyMatrix

class Ising():
    def __init__(self, dim: int) -> None:
        self.adj_matrix = AdjacencyMatrix((dim * dim), dim, dim)

    def get_matrix(self):
        return self.adj_matrix

    def get_lattice(self):
        return self.adj_matrix.get_lattice()

    def print_test(self):
        self.adj_matrix.print_test()