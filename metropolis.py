from ising import Ising
from random import randrange, uniform
from math import e
import scipy.constants

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

    def metropolis(self, time_steps: int, temp) -> int:
        """
        Performs the Metropolis algorithm.

        Arguments:
            - time_steps: int = Number of time steps to run the algorithm.
            - temp: int = Temperature in K.

        Returns:
            Integer representing the number of successful flips during 
            the running of the algorithm.
        """
        # Accumulate sum of successful flips
        flips = 0
        for t in range(time_steps):
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
                # TODO: can also explore exchanging adjacent sites rather than flipping
                self.lattice.flip(i)
            else:
                # If flip is kept, increment flip sum
                flips = flips + 1
        return flips
