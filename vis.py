import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from mpl_toolkits.mplot3d import axes3d


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


def visualize_lattice(lattice_series):
    frames = [lat.get_spin_matrix() for lat in lattice_series]

    print(frames)
    
    fig, ax = plt.subplots(figsize=(6, 6))

    im = ax.imshow(frames[0], cmap='coolwarm', vmin=-1, vmax=1, interpolation='none')
    ax.set_title("Time step: 0")
    plt.colorbar(im, ax=ax)

    def update(frame_index):
        im.set_data(frames[frame_index])
        ax.set_title(f"Time step: {frame_index}")
        return [im]

    ani = animation.FuncAnimation(fig, update, frames=len(frames), interval=100, blit=False)
    plt.show()