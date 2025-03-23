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
        # TODO doc
        return sum(self.get_node(i).spin for i in range(self.N))
            
    def print_test(self):
        """
        Prints lattice
        """
        i = 0
        for row in range(self.height):
            row_list = []
            for col in range(self.width):
                node = self.get_node(i)
                row_list.append(node.spin)
                i += 1
            print(row_list)
    
    def get_spin_matrix(self):
        """
        Returns a 2D NumPy array of the lattice spins with shape (height, width).
        """
        spin_matrix = np.zeros((self.height, self.width), dtype=int)
        for node in self.lattice:
            spin_matrix[node.row, node.col] = node.spin
        return spin_matrix


    def energy(self, i,j):
        il=i-1 if i>0 else self.N-1
        ir=i+1 if i<self.N else 0
        jl=j-1 if j>0 else self.N-1
        jr=j+1 if j<self.N else 0
        return -self.lattice[i,j]*(self.lattice[il,j]+self.lattice[ir,j]+self.lattice[i,jl]+self.lattice[i,jr])

    def magnetization(self):
        m=0
        for i in range(self.N):
            for j in range(self.N):
                m+=self[i,j]
        return m/(self.N*self.N)

# import numpy as np
# from node import Node

# class Lattice():
#     """
#     Lattice for the Ising model.
#     """
#     def __init__(self, width: int, height: int) -> None:
#         """
#         Initializes a Lattice object with the given dimensions.

#         Arguments:
#             - width: int = Width of the lattice.
#             - height: int = Height of the lattice.
#         """
#         # Initializes dimensions
#         self.N = width * height
#         self.width = width
#         self.height = height
#         # Initializes lattice
#         self.init_lattice()
    
#     def init_lattice(self):
#         """
#         Initializes the lattice to random configuration of spins in {1, -1}.
#         """
#         # Initialize lattice with given dimensions
#         self.lattice = np.zeros((self.width, self.height), dtype= int)
#         for row in range(self.height):
#             for col in range(self.width):
#                 # Randomly generates spin from {1, -1}
#                 spin = np.random.choice([-1, 1])
#                 # Generate a Node to store at one dimensional index
#                 self.lattice[row][col] = spin

#     def get_2d_idx(self, idx):
#         row = idx % self.width
#         col = int(idx / self.width)
#         return row, col

#     def get_node(self, idx):
#         """
#         Returns the Node at the given one dimensional index.
#         """
#         row, col = self.get_2d_idx(idx)
#         print(f"row: {row}. col: {col}")
#         return self.lattice[row][col]

#     def is_neighbor(self, a: int, b: int):
#         """
#         Determines if two nodes are neighbors (i.e. directly next to each other in 
#         the two dimensional lattice)

#         Arguments:
#             - a: int = One dimensional index of the first node.
#             - b: int = One dimensional index of the second node.

#         Returns:
#             True if the nodes are neighbors, False otherwise.
#         """
#         if a >= self.N or b >= self.N or a == b:
#             # Same node or either index is out of bounds
#             return False
#         row_a, col_a = self.get_2d_idx(a)
#         row_b, col_b = self.get_2d_idx(b)
#         row_diff = abs(row_a - row_b)
#         col_diff = abs(col_a - col_b)
#         if (row_diff == 1 and col_diff == 0) or (row_diff == 0 and col_diff == 1):
#             # Neighbors!
#             return True
#         # Not neighbors :(
#         return False

#     def flip(self, i):
#         """
#         Flips spin of Node at given index. 
#         """
#         print(f"FLIPPING AT INDEX {i}")
#         row, col = self.get_2d_idx(i)
#         temp = self.get_node(i)
#         self.lattice[row][col] = (temp * -1)

#     def get_dim(self):
#         """
#         Gets the total number of elements in the lattice.
#         """
#         return self.N

#     def calc_spin_sum(self):
#         # TODO doc
#         return sum(self.get_node(i) for i in range(self.N))
            
#     def print_test(self):
#         """
#         Prints lattice
#         """
#         i = 0
#         for row in range(self.height):
#             row_list = []
#             for col in range(self.width):
#                 node = self.lattice[row][col]
#                 row_list.append(node)
#                 i += 1
#             print(row_list)
    
#     def get_spin_matrix(self):
#         """
#         Returns a 2D NumPy array of the lattice spins with shape (height, width).
#         """
#         return self.lattice

