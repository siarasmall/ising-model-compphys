import numpy as np
from node import Node

class Lattice():
    """
    Lattice for the Ising model.
    """
    def __init__(self, width: int, height: int) -> None:
        """
        Initializes a Lattice object with the given dimensions.

        Arguments:
            - width: int = Width of the lattice.
            - height: int = Height of the lattice.
        """
        # Initializes dimensions
        self.N = width * height
        self.width = width
        self.height = height
        # Initializes lattice
        self.init_lattice()
    
    def init_lattice(self):
        """
        Initializes the lattice to random configuration of spins in {1, -1}.
        """
        # Initialize lattice with given dimensions
        self.lattice = np.zeros(self.N, dtype= Node)
        for row in range(self.height):
            for col in range(self.width):
                # Randomly generates spin from {1, -1}
                spin = np.random.choice([-1, 1])
                # Calculate one dimensional index from row, col
                idx = (row * self.width) + col
                # Generate a Node to store at one dimensional index
                self.lattice[idx] = Node(row, col, idx, spin)

    def get_node(self, idx):
        """
        Returns the Node at the given one dimensional index.
        """
        return self.lattice[idx]

    def is_neighbor(self, a: int, b: int):
        """
        Determines if two nodes are neighbors (i.e. directly next to each other in 
        the two dimensional lattice)

        Arguments:
            - a: int = One dimensional index of the first node.
            - b: int = One dimensional index of the second node.

        Returns:
            True if the nodes are neighbors, False otherwise.
        """
        if a >= self.N or b >= self.N or a == b:
            # Same node or either index is out of bounds
            return False
        node_1 = self.get_node(a)
        node_2 = self.get_node(b)
        row_diff = abs(node_1.row - node_2.row)
        col_diff = abs(node_1.col - node_2.col)
        if (row_diff == 1 and col_diff == 0) or (row_diff == 0 and col_diff == 1):
            # Neighbors!
            return True
        # Not neighbors :(
        return False

    def flip(self, i):
        """
        Flips spin of Node at given index. 
        """
        self.lattice[i].flip()

    def get_dim(self):
        """
        Gets the total number of elements in the lattice.
        """
        return self.N

    def calc_spin_sum(self):
        return sum(self.get_node(i).spin for i in range(self.N))
            
    def print_test(self):
        """
        Prints lattice
        """
        for i in range(self.N):
            node = self.get_node(i)
            print(f"Row: {node.row}, col: {node.col}, idx: {node.idx}, spin: {node.spin}")

