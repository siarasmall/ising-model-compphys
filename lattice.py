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
        # Initialize lattice with given length
        self.lattice = np.zeros(self.N, dtype= Node)
        for row in range(self.height):
            for col in range(self.width):
                # Randomly generates spin from {1, -1}
                spin = np.random.choice([-1, 1])
                # Calculate one dimensional index from row, col
                idx = self.get_1d_idx(row, col)
                # Generate a Node to store at one dimensional index
                self.lattice[idx] = Node(row, col, idx, spin)

    def get_node_1d(self, idx):
        """
        Returns the Node at the given one dimensional index.
        """
        if idx < self.N:
            return self.lattice[idx]
        else: 
            raise IndexError

    def get_node_2d(self, i, j):
        """
        Returns the Node at the given two dimensional indices.
        """
        idx = self.get_1d_idx(i, j)
        self.get_node_1d(idx)

    def get_1d_idx(self, row, col):
        """
        Calculates the one dimensional index corresponding to a pair of two dimensional 
        indices of an element in the lattice.
        """
        return col + (row * self.width)

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
        node_1 = self.get_node_1d(a)
        node_2 = self.get_node_1d(b)
        row_diff = abs(node_1.row - node_2.row)
        col_diff = abs(node_1.col - node_2.col)
        if (row_diff == 1 and col_diff == 0) or (row_diff == 0 and col_diff == 1):
            # Neighbors!
            return True
        # Not neighbors :(
        return False

    def flip(self, i, j):
        """
        Flips spin of Node at given index. 
        """
        idx = self.get_1d_idx(i, j)
        self.lattice[idx].flip()

    def get_dim(self):
        """
        Gets the total number of elements in the lattice.
        """
        return self.N

    def magnetization(self):
        """
        Calculates the magnetization of the lattice.
        """
        return sum(self.get_node_1d(i).spin for i in range(self.N)) / self.N
            
    def get_spin_matrix(self):
        """
        Returns a 2D array of the lattice spins.
        """
        spin_matrix = np.zeros((self.height, self.width), dtype=int)
        for node in self.lattice:
            spin_matrix[node.row, node.col] = node.spin
        return spin_matrix

    def hamiltonian(self, i, j):
        """
        Calculates the energy at a given site in the lattice. 

        Huge thanks to Professor Atherton for sharing his solution- the wraparound of the 
        indices in the lattice when calculating energies fixed the bug we came to him with :)       
        """
        il=i-1 if i > 0 else self.width-1
        ir=i+1 if i < self.width else 0
        jl=j-1 if j > 0 else self.height-1
        jr=j+1 if j < self.height else 0
        return -self.get_node_2d(i,j).spin * (self.get_node_2d(il,j).spin + self.get_node_2d(ir,j).spin +self.get_node_2d(i,jl).spin + self.get_node_2d(i,jr).spin)

    def print_test(self):
        """
        Prints lattice.
        """
        i = 0
        for row in range(self.height):
            row_list = []
            for col in range(self.width):
                node = self.get_node_1d(i)
                row_list.append(node.spin)
                i += 1
            print(row_list)