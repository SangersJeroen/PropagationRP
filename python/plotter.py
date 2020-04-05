import matplotlib.pyplot as plt
import matplotlib as mpb
from scipy.integrate import solve_ivp
import numpy as np

plt.rcParams['figure.dpi'] = 150
mpb.rcParams.update({
    #"pgf.texsystem": "pdflatex",
    'font.family': 'serif',
    #'text.usetex': True,
    #'pgf.rcfonts': False,
})


#Defining a few constants
n0 = 1.0002512365013845
alpha = -7.77e-5
theta = 30
c = np.sin(np.pi/180*theta)
x = np.linspace(0,1000,10000)
k = 0

def z(x,k,c):
    return c**2 *(-np.exp(alpha*x/c + alpha*k) -np.exp(-alpha*x/c -alpha*k) + 2*n0)/(2*alpha)

zx = z(x,k,c)
dzdx = np.asarray([])
for i in range(1,len(zx)-1):
    dzdx = np.append(dzdx, (zx[i+1]-zx[i])/(x[i+1]-x[i]))
    angle = np.arcsin(dzdx)*180/np.pi

print(zx[0],zx[-1])
plt.plot(x,zx, label="optical path")
plt.plot(x[1:-1],angle, label="path angle with horizontal")
plt.legend()
plt.show()
