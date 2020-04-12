import numpy as np
import matplotlib.pyplot as plt

import matplotlib as mpb

plt.rcParams['figure.dpi'] = 150
mpb.rcParams.update({
    #"pgf.texsystem": "pdflatex",
    'font.family': 'serif',
    'text.usetex': True,
    #'pgf.rcfonts': False,
})

#Defining our constants
Rsp = 8.3144598
Rair = 287.05
Kair = 0.00023
Ts = 292.15
beta = 6.5/1000
T0 = 323.15
P0 = 101325
g = 9.81

def temperature(c,z):
    return T0 - c*z

def rho_isa(c,z):
    return P0/Rair * (temperature(c,z))**(-g/(beta*Rsp) -1) * Ts**(-g/(beta*Rsp))

def pressure(c,z):
    return P0*np.exp(-(g/(Rair*temperature(c,z))*(z)))

def rho(c,z):
    return pressure(c,z)/(Rair*temperature(c,z))

def index(c,z):
    return 1 + Kair*rho(c,z)

z = np.linspace(0,100,1001)

c = 100

#rho = rho(c,z)
n = index(c,z)

print(n[0],(n[1]-n[0])/(z[1]-z[0]))


plt.subplot(131)
plt.plot(rho(c,z),z)
plt.xlabel('Air density $$\rho [kg/m^3]$$')
plt.subplot(132)
plt.plot(n,z, marker=","),
plt.subplot(133)
plt.plot(temperature(c,z) ,z, color="red")
plt.show()