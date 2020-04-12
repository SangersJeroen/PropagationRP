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
alpha = -7.77e-7
theta = 30
c = np.sin(np.pi/180*theta)
x = np.linspace(-600,1500,10000)
k = 0

def z(x,k,c,alpha):
    return c**2 *(-np.exp(alpha*x/c + alpha*k) -np.exp(-alpha*x/c -alpha*k) + 2*n0)/(2*alpha)

def dzdx(array):
    dzdx = np.asarray([])
    for j in range(1,len(array)-1):
        dzdx = np.append(dzdx, (array[j+1]-array[j])/(x[j+1]-x[j]))
    return np.arcsin(dzdx)*180/np.pi

""" for i in np.linspace(alpha,10*alpha,5):
    zx = z(x,k,c,i)
    angle = dzdx(zx)
    plt.plot(x, zx, label=r"$\alpha = {:.2E}$".format(-i))
    #plt.plot(x[1:-1], angle, label="Angle") """

""" plt.subplot(121) """
plt.plot(x,z(x,k,c,alpha), label="Optical path")
plt.xlabel(r"distance $x$ [$m$]")
plt.ylabel(r"height $z$ [$m$]")

""" plt.subplot(122)
plt.plot(x[1:-1],dzdx(z(x,k,c,alpha)), label="Angle with horizontal")
plt.xlabel(r"distance $x$ [$m$]")
plt.ylabel(r"angle $\theta$ [$\degree$]") """

plt.show()
