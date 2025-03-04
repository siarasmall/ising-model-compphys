import numpy as np
from node import Node

class SquareLattice():
    def __init__(self, N, width, height) -> None:
        self.N = N
        self.width = width
        self.height = height
        self.init_lattice()
    
    def init_lattice(self):
        self.lattice = np.zeros(self.N, dtype= Node)
        for row in range(self.height):
            for col in range(self.width):
                spin = np.random.choice([-1, 1])
                idx = (row * self.width) + col
                self.lattice[idx] = Node(row, col, idx, spin)

    def get_node(self, idx):
        return self.lattice[idx]

    def is_neighbor(self, a, b):
        # a, b are 1d indices
        if a == b:
            # same node
            return 0
        node_1 = self.get_node(a)
        node_2 = self.get_node(b)
        if node_1.get_row() == node_2.get_row() and node_1.get_col() != node_2.get_col():
            if abs(node_1.get_col() - node_2.get_col()) == 1:
                # neighbors by column
                return 1 

        if node_1.get_row() != node_2.get_row() and node_1.get_col() == node_2.get_col():
            if abs(node_1.get_row() - node_2.get_row()) == 1:
                # neighbors by row
                return 1 
        # not neighbors
        return 0

            
    def print_test(self):
        for i in range(self.N):
            node = self.get_node(i)
            print(f"Row: {node.get_row()}, col: {node.get_col()}, idx: {node.get_idx()}, spin: {node.get_spin()}")

