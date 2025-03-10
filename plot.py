# plotting temp vs average magnetization 
# TODO: siara make scaffolding
from typing import List
import matplotlib.pyplot as plt

class Plot():
    def __init__(self, mags: List[float], temps: List[int], lattice: str, algo: str) -> None:
        """
        Initializes a Plot object.

        Args:
            - mags: List[float] = List of magnetization values (TODO: units?)
            - temps: List[int] = List of temperature values (K)
            - lattice: str = Description of lattice to be used in the plot title
            - algo: str = Description of algorithm to be used in the plot title
        """
        self.mags = mags
        self.temps = temps
        self.lattice = lattice
        self.algo = algo

    def plot_magnetization(self):
        """
        Plots magnetization as a function of temperature for a particular algorithm and lattice.
        """
        # Create plot
        plt.figure(figsize=(8, 5))
        plt.plot(self.temps, self.mags, label='Magnetization', linestyle='-.', color='b')
        # Create title, subtitle, axis labels, and legend
        plt.suptitle('Ising model: Magnetization as a function of temperature')
        plt.title(f'Lattice: {self.lattice}; Algortihm: {self.algo}')
        # TODO: units?
        plt.xlabel('Magnetization ()')
        plt.ylabel('Temperature (K)')
        plt.legend(loc='upper right', bbox_to_anchor=(1.15, 1))
        # Show plot
        plt.show()