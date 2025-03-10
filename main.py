from metropolis import Metropolis

def main():
    algo = Metropolis(10, 10)
    for timestep in range(0, 40, 1):
        flips = algo.metropolis(timestep, 400)
        print(f"RUNNING METROPOLIS ALGO WITH {timestep} TIMESTEPS. FLIPS = {flips}")

if __name__ == "__main__":
    main()