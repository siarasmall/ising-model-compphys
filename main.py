from ising import Ising

def main():
    testMatrix = Ising(10)
    # testMatrix.print_test()
    testMatrix.get_lattice().print_test()

if __name__ == "__main__":
    main()