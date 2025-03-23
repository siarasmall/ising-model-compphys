import numpy as np 
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

    def get_matrix(self):
        """
        Returns the adjacency matrix.
        """
        return self.adj_matrix

    def get_lattice(self):
        """
        Returns the lattice.
        """
        return self.lattice

    # Calculate the energy of lattice site (i,j)
    # def energy(a,i,j):
    #     il=i-1 if i>0 else N-1
    #     ir=i+1 if i<N else 0
    #     jl=j-1 if j>0 else N-1
    #     jr=j+1 if j<N else 0
    #     return -a[i,j]*(a[il,j]+a[ir,j]+a[i,jl]+a[i,jr])

    def hamiltonian(self, i: int, J = 1):
        """
        Calculates the Hamiltonian.

        Arguments:
            - i: int = Index of the lattice site for which to calculate the Hamiltonian.
            - J: int = Exchange parameter. Defaults to 1.
        """
        # Calculate Sigma
        sigma = sum((self.adj_matrix.get_element(i, j) * self.lattice.get_node(i).spin * self.lattice.get_node(j).spin) for j in range(self.N) if i != j)
        # Calculate Hamiltonian
        return -J * sigma

    def magnetization(self):
        return self.lattice.calc_spin_sum() / self.N

    def print_test(self):
        self.lattice.print_test()