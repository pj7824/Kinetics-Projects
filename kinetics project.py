import numpy as np
import array
import scipy.integrate as integrate
import scipy.special as special
import matplotlib.pyplot as plt

k=1
A0=1            #A0 is the concentration of A at 0
a=1             # a is the reaction order
B0=1            #B0 is the concentration of B at 0
timestep=1
import time 

dAdt = k*A0
tspan = np.linspace(0, 5)
i=1
A=np.array ([A0,np.linspace(0,len(tspan),timestep)])

for i in range(len(tspan)):

    A[i+1]=A[i]-((A[i]-(a*np.log(A[i])-np.log(k*timestep)))/timestep)  #i'm trying to add the change in concentration to the previous concentration  
    i=i+1
    print (A)                                                          #keep getting index error index 2 is out of bounds for axis 0 with size 2
    


plt.plot(tspan, A[i])                           #once i get the code working, this is how i would plot it