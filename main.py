# from metropolis import Metropolis
# from ising import Ising
from lattice import SquareLattice
from adj_matrix import Adjacency_matrix

def main():
    # testObj = SquareLattice(9, 3, 3)
    # testObj.print_test()
    testMatrix = Adjacency_matrix(6, 2, 3)
    testMatrix.print_test()

if __name__ == "__main__":
    main()