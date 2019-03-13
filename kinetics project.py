import numpy as np
import array
import scipy.integrate as integrate
import scipy.special as special
import time
import matplotlib.pyplot as plt

k=1
A0=1            #A0 is the concentration of A at 0
a=1             # a is the reaction order
B0=1            #B0 is the concentration of B at 0
timestep=0.1
timelen=100

dAdt = k*A0
tspan = np.arange(0, timestep*timelen,timestep)

A=np.array ([A0])
t=0
for i in range(len(tspan)-1):
    
    A_at_time_t= k*(A[i-1])*timestep+(A[i-1])   #i'm trying to add the change in concentration to the previous concentration  
    i=i+1
    A=np.append(A,A_at_time_t)
                                                             #keep getting index error index 2 is out of bounds for axis 0 with size 2
    
plt.figure(1)
plt.clf()
plt.plot(tspan, A)                           #once i get the code working, this is how i would plot it
