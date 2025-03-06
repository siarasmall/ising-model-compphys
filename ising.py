import numpy as np 
from lattice import Lattice
from adj_matrix import AdjacencyMatrix

class Ising():
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height
        self.N = width*height
        self.lattice = Lattice(self.N, width, height)
        self.adj_matrix = AdjacencyMatrix(self.N, self.lattice)

    def get_matrix(self):
        return self.adj_matrix

    def get_lattice(self):
        return self.lattice

    def hamiltonian(self, i, J = 1):
        # TODO: ask where J is coming from/how to calc
        sigma = sum((self.adj_matrix.get_element(i, j) * self.lattice.get_node(i).spin * self.lattice.get_node(j).spin) for j in range(self.N) if i != j)
        return -J * sigma

    def magnetization(self):
        pass

    def temperature(self):
        pass

    def print_test(self):
        # TODO: print both and make pretty
        self.adj_matrix.print_test()