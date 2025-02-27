import numpy as np

class Metropolis():
    def __init__(self, w, h) -> None:
        # TODO: consider making number of dimensions parameterized
        # TODO: all have same dimension?
        self.width = w
        self.height = h
        self.magnetization = 0
        self.avg_energy = 0
        self.lattice = self.initial_lattice()
        # will also need adj matrix?

    def calc_hamiltonian(self, j):
        # this should probs go in ising class
        pass

    def sum_spins():
        pass

    def calc_magnetization(self):
        pass

    def initial_lattice(self):
        lattice = np.zeros([self.height, self.width], dtype= float)
        for row in range(self.height):
            for col in range(self.width):
                lattice[row][col] = np.random.choice([-1, 1])
        return lattice

    def print_test(self):
        for row in range(self.height):
            for col in range(self.width):
                print(f"elem at row {row}, col {col} = {self.lattice[row][col]}")
