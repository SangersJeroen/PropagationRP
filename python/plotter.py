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
alpha = 0.01
theta = 30
sin = np.sin(np.pi/180*theta)
c = 0.5*(-np.sqrt(16*alpha**2 +16*alpha*n0+sin**2+4*n0**2)-sin)
k = np.log((np.sqrt(16*alpha**2 +16*alpha*n0+sin**2+4*n0**2)+4*alpha+sin+2*n0)/(np.sqrt(16*alpha**2 +16*alpha*n0+sin**2+4*n0**2) -4*alpha +sin-2*n0))/2*alpha

x = np.linspace(0,100,10000)
print(c)

""" def z(x,c):
    upper = -n0*np.exp(2*alpha*(x-c)) + c*(-np.exp(2*alpha*(x-c))) + c - n0
    lower = alpha*(np.exp(2*alpha*(x-c))+1)
    return upper/lower
 """
"""
def dzdx(x,z):
    zprime = np.sqrt((n0+alpha*z)**2 -c**2)/c
    return zprime
 """"""

def y(x):
    return (np.exp(-(alpha**2 * x)/c)*(-2*b*np.exp((alpha**2 * x)/c) -4*alpha**2 * const + np.exp(2*alpha*x/c) +b**2 ))/(4*alpha**2)
"""

def z(c,x,alpha):
    return -n0+1.7 - (c*np.cosh(alpha*(x+k)))

for i in [alpha,alpha*0.9,alpha*0.8,alpha*0.7,alpha*0.6,alpha*0.5,alpha*0.4,alpha*0.3]:
    plt.plot(x,z(c,x,i), label='alpha = {:.3f}'.format(i))
    plt.xlabel("Distance $m$")
    plt.ylabel("Height $m$")
#plt.plot(x,z1(c,x), label='Light z1')
#plt.ylim([0,z1(c,x)[-1]])
plt.legend()
plt.show()