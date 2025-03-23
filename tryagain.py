import numpy as np
import random as rnd
import time
from math import exp
from main import plot_mag_v_time, plot_mag_v_temp

N=20
Niter=1000
T=2

# Initialize the board
def init():
    if (rnd.random()<0.5):
        return 1
    return -1

def run_algo(T):
    a = np.zeros((N, N))
    for i in range(N):
        for j in range(N):
            a[i,j]=init()
    mags = []
    for n in range(Niter):
        for k in range(N*N):
            i=rnd.randrange(N-1)
            j=rnd.randrange(N-1)
            old = energy(a, i, j);
            a[i,j]=-a[i,j]
            new = energy(a, i, j);
            if (new>=old):
                if (exp((old-new)/T)<rnd.random()):
                    a[i,j]=-a[i,j]
        mags.append(magnetization(a))
    return mags



# Calculate the energy of lattice site (i,j)
def energy(a,i,j):
    il=i-1 if i>0 else N-1
    ir=i+1 if i<N else 0
    jl=j-1 if j>0 else N-1
    jr=j+1 if j<N else 0
    return -a[i,j]*(a[il,j]+a[ir,j]+a[i,jl]+a[i,jr])

# Calculate the total energy of the system
def total(a):
    en=0
    for i in range(N):
        for j in range(N):
            en+=a[i,j]
    return en

# Magnetization
def magnetization(a):
    m=0
    for i in range(N):
        for j in range(N):
            m+=a[i,j]
    return m/(N*N)

# Visualization
def vis(a):
    for i in range(N):
        str=""
        for j in range(N):
            if (a[i,j]<0):
                str+="-"
            else:
                str+="X"
        print(str);
    return

# multiple lines
mags_for_temp = []
for temp in list(range(0, 10, 1)):
    mags_temp = run_algo(temp)
    mags_for_temp.append((mags_temp, temp))

plot_mag_v_time(list(range(Niter)), mags_for_temp, "Metropolis", f"Square {N} by {N}")


# single line
# mags_for_temp = []
# for temp in list(range(0, 10, 1)):
#     mags_temp = run_algo(temp)
#     mags_for_temp.append(np.mean(mags_temp))

# plot_mag_v_temp(list(range(0, 10, 1)), mags_for_temp, "Metropolis", f"Square {N} by {N}")
