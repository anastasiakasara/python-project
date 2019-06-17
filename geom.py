#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 20:02:39 2018

@author: natasa
"""


import numpy as np
import matplotlib.pyplot as plt
sd=0.3
mu=5
nsim=50
nt=100
dt=1.0/nt

S0=100
S = np.ndarray((nsim,nt))   
#  np.random.seed(1)
msd = (mu-sd**2/2.)*dt

for j in range(0,nsim):
    S[j,0] = S0   
    for n in range(1,nt):
            eR = np.exp(msd + sd*np.sqrt(dt)*np.random.normal(0,1,1))
            S[j,n] = S[j,n-1] * eR 
            
##########################################            
S[0,99]
S[0,100]
S[0,0]
plt.plot(S[1,0:110])
plt.show()
#plt.style.use(['bmh'])
#fig, ax = plt.subplots(1)
##fig.suptitle(title, fontsize=16)
#ax.set_xlabel('Time, t')
#ax.set_ylabel('Simulated Asset Price')
#x_axis = np.arange(0, nt, 1)
#for i in range(0,nsim):
#     plt.plot(S[i,0:nt])
#plt.show()
           
print(S[0,0:900])
###################################################
#plt.gcf().clear()


# Geometric brownian motion simulations
for j in range(0,nsim):  
    plt.plot(S[j,:])
    
plt.xlabel('t')
plt.ylabel('S')
plt.title('Realizations of BM')

###############################################################
    # monte carlo for the share prices in time n-1
    
mn = (np.mean(S[0:nsim,n-1]))
print(mn)
mol=(np.log(mn)-np.log(S0))/((n-1)*dt)
print(mol)

###########################################

st = (np.std(S[0:nsim,n-1]))
d=np.log(1+((st**2)/(mn**2)))
sigma=np.sqrt(1/((n-1)*dt))*(np.sqrt(d))
print(sigma)
#plt.clf()
#plt.cla()
#plt.close()