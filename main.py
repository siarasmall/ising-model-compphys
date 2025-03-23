from metropolis import Metropolis
from vis import plot_mag_v_temp, plot_mag_v_time, visualize_lattice
import numpy as np
from copy import copy, deepcopy


def main():
    # TODO: make this more modular and probably put in ising module
    width = 20
    height = 20
    # MAGNETIZATION VS TIME FOR EACH TEMP
    temps = list(range(0, 10, 1))
    # # algo = Metropolis(width, height) #figuring out where this goes
    timesteps = 2000
    mags_for_temp = []
    
    for temp in temps:
    # temp = 5
        algo = Metropolis(width, height)
        flips, current_mags, lattices = algo.metropolis(temp, timesteps)
        mags_for_temp.append((deepcopy(current_mags), temp))
    plot_mag_v_time(list(range(timesteps)), mags_for_temp, "Metropolis", f"Square {width} by {height}")
    

    # MAGNETIZATION VS TEMPERATURE - this is working
    # mags = []
    # for temp in temps:
    #     algo = Metropolis(width, height)
    #     flips, all_mags, lattices = algo.metropolis(temp, timesteps)
    #     mags.append(np.mean(all_mags))
    
    # plot_mag_v_temp(temps, mags, "Metropolis", f"Square {width} by {height}")
    # visualize_lattice(lattices)
    # pick J st J/kT ~= 1


if __name__ == "__main__":
    main()