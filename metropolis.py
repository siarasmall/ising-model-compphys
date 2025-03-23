from ising import Ising
from math import exp
from copy import deepcopy
import random as rnd

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

    def metropolis(self, T, timesteps: int, k = 0.5):
        """
        Performs the Metropolis algorithm for a given number of timesteps. 

        Arguments:
            - time_steps: int = Number of time steps to run the algorithm.
            - temp: int = Temperature in K.
            - k: Placeholder for Boltzmann comstant.

        Returns:
            Tuple containing:
                - mags: List[Float] = Magnetizations of the lattice at each time step.
                - lattices: List[List[Int]] = Preservation of lattice configuration at each time step.
        """
        # Init accumulation variables for preservation.
        mags = []
        lattices = []

        # Iterate through timesteps
        for timestep in range(timesteps):
            for idx in range(self.N):
                # Randomly select row, column
                selected_row = rnd.randrange(self.height - 1)
                selected_col = rnd.randrange(self.width - 1)

                # Calculate change in energy upon flipping spin at random site.
                old = self.lattice.hamiltonian(selected_row, selected_col);
                self.lattice.flip(selected_row, selected_col)
                new = self.lattice.hamiltonian(selected_row, selected_col);

                # Determine if flip should be kept.
                if (new >= old):
                    if (exp((old - new)/T) < rnd.random()):
                        self.lattice.flip(selected_row, selected_col)

            # Preserve data at timestep
            mags.append(self.lattice.magnetization())
            lattices.append(deepcopy(self.lattice))
        return mags, lattices

