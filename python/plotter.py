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
n0 = 1.00022929
n1 = 1.000271621
alpha = -(n1-n0)/3
theta = 179
c = 100
d = 10
x = np.linspace(-d,100,100)
x_ = np.linspace(-d,100,100)+d
k = 0

print(alpha)

def z(x,k,c,alpha):
    out =  c**2 *(-np.exp((alpha*(x-d) + alpha*k)/c) -np.exp((-alpha*(x-d) -alpha*k)/c) + 2*n0)/(2*alpha)
    out = out - out[0]+1.80
    return out

def dzdx(array):
    dzdx = np.asarray([])
    for j in range(1,len(array)-1):
        dzdx = np.append(dzdx, (array[j+1]-array[j])/(x[j+1]-x[j]))
    return np.arcsin(dzdx)*180/np.pi

for i in np.linspace(alpha,5*alpha,5):
    zx = z(x,k,c,i)
    angle = dzdx(zx)
    plt.plot(x_, zx, label=r"$\alpha = {:.2E}$".format(-i))
    #plt.plot(x[1:-1], angle, label="Angle") """

plt.ylim([1,3])
""" plt.subplot(121) """
#plt.plot(x_,z(x,k,c,alpha), label="Optical path")
plt.xlabel(r"distance $x$ [$m$]")
plt.ylabel(r"height $z$ [$m$]")
plt.legend()

""" plt.subplot(122)
plt.plot(x[1:-1],dzdx(z(x,k,c,alpha)), label="Angle with horizontal")
plt.xlabel(r"distance $x$ [$m$]")
plt.ylabel(r"angle $\theta$ [$\degree$]") """

plt.show()
