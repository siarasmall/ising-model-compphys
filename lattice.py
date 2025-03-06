import numpy as np
from node import Node

class Lattice():
    def __init__(self, N: int, width: int, height: int) -> None:
        self.N = N
        self.width = width
        self.height = height
        self.init_lattice()
    
    def init_lattice(self):
        self.lattice = np.zeros(self.N, dtype= Node)
        for row in range(self.height):
            for col in range(self.width):x
                spin = np.random.choice([-1, 1])
                idx = (row * self.width) + col
                self.lattice[idx] = Node(row, col, idx, spin)

    def get_node(self, idx):
        return self.lattice[idx]

    def is_neighbor(self, a, b):
        # a, b are 1d indices
        if a == b:
            return 0 # Same node
        node_1 = self.get_node(a)
        node_2 = self.get_node(b)
        row_diff = abs(node_1.row - node_2.row)
        col_diff = abs(node_1.col - node_2.col)

        if (row_diff == 1 and col_diff == 0) or (row_diff == 0 and col_diff == 1):
            return 1 # Neighbors

        return 0  # Not neighbors

    def flip(self, i):
        self.lattice[i].flip()
            
    def print_test(self):
        for i in range(self.N):
            node = self.get_node(i)
            print(f"Row: {node.row}, col: {node.col}, idx: {node.idx}, spin: {node.spin}")

