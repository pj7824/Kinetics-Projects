import numpy as np

def myode(C, t):
    # ra = -k1*Ca the forward rate law
    # rb = -k_1*Cb  the backward rate law
    # rate of A:  ra - rb
    # rate of B: -ra + rb

    k1 = 1   # 1/min; 
    k_1 = 0.5   # 1/min;

    Ca = C[0]   #the intial concentrations of A and B
    Cb = C[1]

    ra = -k1 * Ca
    rb = -k_1 * Cb

    dCadt =  ra - rb
    dCbdt = -ra + rb

    dCdt = [dCadt, dCbdt]   #trying to integrate this function but cannot
tspan = np.linspace(0, 1000)    #

init = [1, 0]       


Ca = Ca[12:,0]          #A(previouse time) + (a thing that reflects the change in A for one timke)
Cb = Cb[19:,1]

import matplotlib.pyplot as plt
plt.plot(tspan, Ca, tspan, Cb)
plt.xlabel('Time (min)')
plt.ylabel('C (mol/L)')     #units of the concentration when it is able to plot

