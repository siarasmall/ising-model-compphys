from ising import Ising
from random import randrange, uniform
from math import e, exp
from copy import copy, deepcopy
import random as rnd
import numpy as np

class Metropolis(Ising):
    """
    Class for the Metropolis algorithm for the Ising model of ferromagnetism.
    """
    def __init__(self, width: int, height: int) -> None:
        """
        Arguments:
            - width: int = Width of the lattice. 
            - width: int = Height of the lattice. 
        """
        super().__init__(width, height)

    # def metropolis(self, temp, timesteps: int, k = 0.5) -> tuple:
    #     """
    #     Performs the Metropolis algorithm for a set number of timesteps while recording 
    #     magnetization at each timestep.

    #     Arguments:
    #         temp: int = Temperature (K).
    #         timesteps: int = Number of timesteps to run the algorithm for.

    #     Returns:
    #         A tuple containing:
    #         - flips: int
    #             The number of successful flips.
    #         - mag_time_series: list
    #             A list of magnetization values recorded at each timestep.
    #     """
    #     # Init variables to accumulate
    #     mag_time_series = []
    #     flips = 0   
    #     lattices = []

    #     for timestep in range(timesteps):
    #         # Get random site in lattice
    #         site_index = randrange(0, self.N)
    #         # Calculate original energy
    #         old_E = self.hamiltonian(site_index)
    #         # Perform a random flip
    #         self.lattice.flip(site_index)
    #         # Calculate new energy
    #         new_E = self.hamiltonian(site_index)
    #         # Calculate change in energy
    #         delta_E = new_E - old_E

    #         if delta_E <= 0:
    #             if uniform(0, 1) < exp(-delta_E / (k * temp)):
    #                 flips += 1
    #         else:
    #             self.lattice.flip(site_index)
    #         mag_time_series.append(self.magnetization())
    #         lattices.append(deepcopy(self.lattice))

    #     return flips, mag_time_series, lattices

    def metropolis(self, T, timesteps: int, k = 0.5):
        mags = []
        for n in range(timesteps):
            for k in range(self.N):
                i=rnd.randrange(self.height-1)
                j=rnd.randrange(self.width-1)
                old = self.energy(self.lattice, i, j);
                self.lattice[i,j]=-self.lattice[i,j]
                new = self.energy(self.lattice, i, j);
                if (new>=old):
                    if (exp((old-new)/T)<rnd.random()):
                        self.lattice[i,j]=-self.lattice[i,j]
            mags.append(self.magnetization(self.lattice))
        return mags

