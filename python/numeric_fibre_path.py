# -*- coding: utf-8 -*-
"""
Created on Wed May  6 17:53:40 2020

@author: vanlo
"""

import numpy as np
import matplotlib.pyplot as plt

plt.close()   # Close previous plots 

   # Define function to plot the analytical solution to the problem using only the x
def  analytical(x):
    return  np.sqrt(n0**2 -a**2)/( n0*alpha)*np.sin((n0*alpha*x)/a)

   # Define function to find the slope of the function at every steo in x-step. Input: previous value of r
def drdx(r):
       # We need to add inclnine variable in order to let the function change direction
       # If incline = 1, the function is going up until it reaches it's peak, else, the function needs to down until it's peak
    if incline == 1:
        drdx_1 = abs(np.sqrt((n0**2 - n0**2*alpha**2*r**2-a**2)*a**(-2)))
    else:
        drdx_1 = -abs(np.sqrt((n0**2 - n0**2*alpha**2*r**2-a**2)*a**(-2)))
       # If the slope has a value close to 0, we know the function has reached a peak (or is near a peak)
       # --> We change value of peak to 1 if value for slope is near 0. If not, peak = 0 --> not at a peak
    if abs(drdx_1)<0.01:
        peak = 1
    else: 
        peak = 0
    return [drdx_1,peak] 


   # Define constants also using complex part in order to perfom complex roots:
n0 = 1.7 +0*1j   # Refractive index at r = 0
R = 1    # Outer radius of fiber
alpha = 1/R +0*1j   # inverse of R
a = 1 +0*1j   # Arbitrary constant
N = int(2*1e3)   # Number of steps for numeric calculation

incline = 1   # Variable to define if function is going down or going up

x = np.linspace(0,10*R,N)  # Array for which to find r values
dx = x[1]-x[0] + 0*1j   # Step size in x-direction
drdx_array = np.array([])   # Empty array to fill up with correct slopes for every x-step

r = np.zeros(N) + np.zeros(N)*1j  #Emty array to fill up with correct r-values. Also complex part for computation 
r[1] = dx   # We let the beam come in at an angle of 1/2*Pi.

peak_array = np.empty(N)   # Array for peak values to keep track of past peak values

   # Numeric calculation of r:
for i in range(1,N):
       # Calculate slope and add to array
    drdx_i = drdx(r[i-1])[0]
    r[i] = r[i-1] + drdx_i*dx  
       # See if function is at a peak or near a peak, and add to array
    peak_i = drdx(r[i-1])[1]
    peak_array[i-1] = peak_i
       # If functions is at a peak and hasn't just passed a peak, change incline so it changes direction
       # --> in order to let function oscillate
    if peak_i == 1 and (1 not in peak_array[i-6:i-1]):
        incline = -1* incline
    
    
   # plots of numeric and analytical solution 
plt.plot(x,r, label='Numeric', linewidth=3.)
plt.plot(x,analytical(x), linestyle='--', label='analytical', linewidth=2.)
plt.legend()
plt.xlabel('x [R]')
plt.ylabel('y [R]')
plt.show()

    
    