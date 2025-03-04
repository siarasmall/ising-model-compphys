import numpy as np
from ising import Ising
from random import randrange

class Metropolis(Ising):
    def __init__(self, dim: int) -> None:
        super().__init__(dim)

    def step(self):
        randRow = randrange(self.dim)
        randCol = randrange(self.dim)
        super().flip(randRow, randCol)

    def evolve(self):
        deltaEnergy = super().get_energy() - super().calc_hamiltonian()
