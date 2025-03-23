from lattice import Lattice
from adj_matrix import AdjacencyMatrix

class Ising():
    """
    Simulation of the Ising model of ferromagnetism.
    """
    def __init__(self, width: int, height: int) -> None:
        """
        Initializes an object for the Ising model.

        Arguments:
            - width: int = Width of the lattice
            - height: int = Height of the lattice
        """
        # Initializes dimensions
        self.width = width
        self.height = height
        self.N = width*height
        # Initializes lattice and adjacency matrix
        self.lattice = Lattice(width, height)
        self.adj_matrix = AdjacencyMatrix(self.lattice)
