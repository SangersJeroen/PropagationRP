#Importin the used libraries
import numpy as np
from numpy.lib import scimath
import math
import matplotlib.pyplot as plt

#Defining a few constants
n0 = 1.7
R = 1
alpha =1/(R)
a = 1
N = 50 #steps

x = np.linspace(0,2*R,N)
dx = x[1]-x[0]

def index(r):
    return n0**2 * (1-(alpha*r)**2)

def dr_squared(r):
    return (n0**2 * (1-(alpha*r)**2) -a**2)/a**2

def analytical(x):
    return np.sqrt(n0**2 -a**2)/(n0*alpha)*np.sin((n0*alpha*x)/a)

r = np.empty(N) +0j
increments = np.empty(N) +0j
r[0] = 0
for i in range(1,N):
    increment = dr_squared(r[i-1])
    print(np.sqrt(increment))
    increments[i] = increment
    r[i] = r[i-1] + np.real(np.sqrt(increment))*dx - np.imag(np.sqrt(increment))*dx

plt.plot(x, r, marker=".", label="positive solution")
plt.xlabel(r"distance along center [$R$]")
plt.ylabel(r"distance from center [$R$]")
plt.plot(x, analytical(x), label="analytical solution")
plt.legend()
plt.show()