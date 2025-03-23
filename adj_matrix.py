from lattice import Lattice

class AdjacencyMatrix():
    """
    Adjacency matrix of a Ising model lattice containing information about 
    the neighbors of each node.

    Format: 
        {
            i: [indices of neighbors]
        }
        - Dictionary of lattice indices mapping to all other lattice indices 
        they are next to in the lattice.
    """
    def __init__(self, lattice: Lattice) -> None:
        """
        Initializes an AdjacencyMatrix.

        Arguments:
            - Lattice: Lattice from which to construct the adjacency matrix.
        """
        self.lattice = lattice
        self.N = self.lattice.get_dim()
        self.adjacency_matrix = self.generate_matrix()

    def generate_matrix(self):
        """
        Generates the adjacency matrix for a given lattice. Returns a dictionary 
        mapping indices to a list of their neighbors.
        """
        adjacency_matrix = {}
        for i in range(self.N):
            adjacency_matrix[i] = []
            for j in range(self.N):
                if self.lattice.is_neighbor(i, j):
                    adjacency_matrix[i].append(j)
        return adjacency_matrix

    def get_neighbors(self, idx):
        """
        Get a list of neighbors of a node at the given index.
        """
        return self.adjacency_matrix[idx]

    def get_matrix(self):
        """
        Returns the adjacency matrix.
        """
        return self.adjacency_matrix

    def get_element(self, i, j):
        """
        Returns 1 if the nodes at indices i, j are neighbors in the lattice; 0 otherwise.
        """
        if j in self.adjacency_matrix[i]: return 1
        else: return 0

    def print_test(self):
        """
        Prints dictionary of adjacency matrix.
        """
        print(self.adjacency_matrix)