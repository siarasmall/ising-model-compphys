from metropolis import Metropolis
import matplotlib.pyplot as plt
import numpy as np

def plot_mag_v_temp(temps, mags, algo, lattice):
    # TODO: dont like how the code was organized here. make more OO
    """
    Plots magnetization as a function of temperature for a particular algorithm and lattice.
    """
    # Create plot
    plt.figure(figsize=(10, 7))
    plt.plot(temps, mags, label='Magnetization', linestyle='-', color='b')
    # Create title, subtitle, axis labels, and legend
    plt.suptitle(f'Ising model: Magnetization as a Function of Temperature')
    plt.title(f'Lattice: {lattice}; Algorithm: {algo}')
    plt.ylabel('Magnetization \n (amps/m)')
    plt.xlabel('Temperature (K)')
    plt.legend(loc='upper right', bbox_to_anchor=(1.15, 1))
    # Show plot
    plt.show()

def plot_mag_v_time(times, mags_for_temp, algo, lattice):
    plt.figure(figsize=(12, 7))
    # Generate color range to match temp
    colors = plt.cm.plasma(np.linspace(0, 1, len(mags_for_temp)))
    # Generate lines for each temp
    for (mags, temp), color in zip(mags_for_temp, colors):
        plt.plot(times, mags, label=f'T = {temp} K', linestyle='-', color = color)
    plt.axhline(linewidth=1, color='grey', linestyle='dotted')
    # Create title, subtitle, axis labels, and legend
    plt.suptitle('Ising model: Magnetization as a Function of Time')
    plt.title(f'Lattice: {lattice}; Algorithm: {algo}')
    plt.ylabel('Magnetization \n (amps/m)')
    plt.xlabel('Time step')
    plt.legend(loc='upper right', bbox_to_anchor=(1, 1))
    # Show plot
    plt.show()


def main():
    # TODO: make this more modular and probably put in ising module
    width = 10
    height = 10
    # MAGNETIZATION VS TIME FOR EACH TEMP
    temps = list(range(375, 475, 15))
    # algo = Metropolis(width, height) #figuring out where this goes
    timesteps = 800
    mags_for_temp = []
    
    for temp in temps:
        algo = Metropolis(width, height)
        flips, current_mags = algo.metropolis_with_timesteps(temp, timesteps)
        mags_for_temp.append((current_mags, temp))
    
    plot_mag_v_time(list(range(timesteps)), mags_for_temp, "Metropolis", f"Square {width} by {height}")

    # MAGNETIZATION VS TEMPERATURE - this is working
    # mags = []
    # algo = Metropolis(width, height)
    # for temp in temps:
    #     algo.metropolis_with_convergence(temp)    
    #     mags.append(algo.magnetization())
    # plot_mag_v_temp(temps, mags, "Metropolis", f"Square {width} by {height}")

    # pick J st J/kT ~= 1


if __name__ == "__main__":
    main()