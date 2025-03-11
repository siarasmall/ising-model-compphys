from ising import Ising
from random import randrange, uniform
from math import e
import scipy.constants

class Metropolis(Ising):
    # TODO: re-document algo functions and probs make it more modular
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

    def metropolis_with_convergence(self, temp) -> int:
        """
        Performs the Metropolis algorithm until convergence. 

        Arguments:
            - time_steps: int = Number of time steps to run the algorithm.
            - temp: int = Temperature in K.

        Returns:
            Integer representing the number of successful flips during 
            the running of the algorithm.
        """
        # Accumulate sum of successful flips
        flips = []
        equilibrium = False
        idx = 0
        while not equilibrium:
            curr_flips = 0
            # Get random site in lattice
            i = randrange(0, self.N)
            # Calculate original energy
            old_E = self.hamiltonian(i)
            # Perform random flip
            self.lattice.flip(i)
            # Calculate new energy
            new_E = self.hamiltonian(i)
            # Calculate change in energy
            delta_E = old_E - new_E
            # Analyze if flip should be kept; if not, flip back
            if delta_E >= 0 or uniform(0, 1) >= pow(e, (-delta_E/ (scipy.constants.k*temp))):
                self.lattice.flip(i)
            else:
                # If flip is kept, increment flip sum
                curr_flips = 1
            if idx >= 5:
                if curr_flips == 0 and flips[idx - 1] == 0 and flips[idx - 2] == 0 and flips[idx - 3] == 0 and flips[idx - 4] == 0:
                    equilibrium = True

            idx += 1
            flips.append(curr_flips)
        return idx # index at which it converges


    def metropolis_with_timesteps(self, temp, timesteps: int) -> tuple:
        """
        Performs the Metropolis algorithm for a set number of timesteps while recording 
        magnetization at each timestep.

        Arguments:
            temp: int = Temperature (K).
            timesteps: int = Number of timesteps to run the algorithm for.

        Returns:
            A tuple containing:
            - flips: int
                The number of successful flips.
            - mag_time_series: list
                A list of magnetization values recorded at each timestep.
        """
        flips = 0
        mag_time_series = []
        
        for _ in range(timesteps):
            # Get random site in lattice
            site_index = randrange(0, self.N)
            # Calculate original energy
            old_E = self.hamiltonian(site_index)
            # Perform a random flip
            self.lattice.flip(site_index)
            # Calculate new energy
            new_E = self.hamiltonian(site_index)
            # Calculate change in energy
            delta_E = old_E - new_E
            # Analyze if flip should be kept; if not, flip back
            if delta_E >= 0 or uniform(0, 1) >= pow(e, (-delta_E / (scipy.constants.k * temp))):
                self.lattice.flip(site_index)  # flip back if not accepted
            else:
                # If flip is kept, increment flip sum
                flips += 1
            # Save magnetization at current timestep
            mag_time_series.append(self.magnetization())

        return flips, mag_time_series
