import numpy as np 

class Algorithm():
    def __init__(self) -> None:
        pass

class Ising():
    def __init__(self, algorithm, dim: int) -> None:
        # TODO: will dimensions be same or should have height and width?
        self.dim = dim
        self.magnetization = 0
        self.avg_energy = 0
        self.init_lattice()

    def sum_spins():
        pass

    def calc_hamiltonian(self, j):
        pass

    def calc_magnetization(self):
        pass

    def get_energy(self):
        return self.avg_energy

    def init_lattice(self):
        self.lattice = np.zeros([self.dim, self.dim], dtype= float)
        for row in range(self.dim):
            for col in range(self.dim):
                self.lattice[row][col] = np.random.choice([-1, 1])

    def flip(self, row: int, col: int):
        self.lattice[row][col] *= -1

    def print_test(self):
        for row in range(self.dim):
            for col in range(self.dim):
                print(f"Elem at row {row}, col {col} = {self.lattice[row][col]}")