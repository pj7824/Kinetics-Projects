import numpy as np
import array
import scipy.integrate as integrate
import scipy.special as special
import time
import matplotlib.pyplot as plt

k=1
A0=1            #A0 is the concentration of A at 0
a=1             # a is the reaction order
B0=100            #B0 is the concentration of B at 0
#B=10
timestep=0.1
timelen=100

dAdt = k*A0
tspan = np.arange(0, timestep*timelen,timestep)

A=np.array ([A0])
B=np.array ([B0])
t=0
for i in range(len(tspan)-1):
    # new [A] = change in A +        previous A
    A_at_time_t= k*(B[i-1])*timestep+(A[i-1])   #i'm trying to add the change in concentration to the previous concentration  
        #this line should update B_at_time_t        
    A=np.append(A,A_at_time_t)
        #this like should add B_at_time_t onto B
    B_at_time_t= -k*(B[i-1])*timestep+(B[i-1])
    B=np.append(B,B_at_time_t)    
    i=i+1
print (B)
#A_r=100           # A_r the concentration of A reverse reaction 
#dBdt=-k*B0     
#tspan= np.arange(0, timestep*timelen,timestep) 
#
#R=np.array([B0])
#for i in range(len(tspan)-1):
#    
#    R_at_time_t= -k*(A[i+1])*timestep-(A[i-1])
#    i=-i+1
#    A_r=np.append (A_r,R_at_time_t)                                  


    

    
plt.figure(1)
plt.clf()
plt.plot(tspan, A)
plt.plot(tspan, B)  
#plt.plot(tspan,R)                         #once i get the code working, this is how i would plot it
