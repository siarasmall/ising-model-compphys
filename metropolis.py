import numpy as np
from ising import Ising
from random import randrange, uniform
from math import e
import scipy.constants

class Metropolis(Ising):
    def __init__(self, width: int, height: int) -> None:
        super().__init__(width, height)

    def metropolis(self, time_steps: int, temp):
        flips = 0
        for t in range(time_steps):
            i = randrange(0, self.N)
            old_E = self.hamiltonian(i)
            self.lattice.flip(i)
            new_E = self.hamiltonian(i)
            delta_E = old_E - new_E
            if delta_E >= 0 or uniform(0, 1) >= pow(e, (-delta_E/ (scipy.constants.k*temp))):
            # if delta_E >= 0:
                self.lattice.flip(i)
                # print(f"keeping flip. detla e = {delta_E}. old E = {old_E} and new E = {new_E}")
            else:
                flips = flips + 1
        return flips
