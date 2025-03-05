from ising import Ising
from lattice import Lattice
from adj_matrix import AdjacencyMatrix

def main():
    testMatrix = Ising(10)
    testMatrix.print_test()

if __name__ == "__main__":
    main()