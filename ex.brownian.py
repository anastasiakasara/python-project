#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 10 19:47:18 2018

@author: natasa
"""



import os
print(os.getcwd())
os.chdir("/home/natasa/pythonwork")
print(os.getcwd())
################################################################test-3
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from math import sqrt
N=101
dt=1/N
t=np.arange(0,1,dt)
t.shape


plt.figure(2)
def brownian_path(N):
    Δt_sqrt = math.sqrt(1 / N)
    Z = np.random.randn(N)
    Z[0] = 0
    B = np.cumsum(Δt_sqrt * Z)
    return B

T1 = [x for x in range(N)]
B = brownian_path(N)
plt.plot(T1,B,c="green")
plt.xlabel('time')
plt.ylabel("Brownian")


#W_t=np.zeros(N)
#W_t.shape
#W_t.ndim
#W_t[0] = 0.0
#for i in range(1,N):
#    W_t[i]=W_t[i-1]+np.random.normal(0,1,1)*sqrt(dt)
    
print(W_t)
plt.figure(1)
#plt.subplot(211)
plt.plot(t,W_t,c='red')

#t_p=0.4
#
#for i in range(1,N-1):  
#   if np.logical_and(t[i]<t_p, t[i+1]>t_p) == True:
#    break
#
#print(i)


print(N)
t_p=0.4
while i in range(1,N-1):
 #   print(i,t[i]) 
    if t[i]<t_p and t[i+1]>t_p:
      break
  

  

print(i)
#    
     

print(W_t[40])

    
####################################################
#N2=5001
#dt = 1/(N2)
#t2=np.arange(0,1,dt)
#t2.shape
#W_t2=np.zeros(N2)
#W_t2.shape
#W_t2.ndim
#W_t2[0] = 0.0
#for i in range(1,N2):
#    W_t2[i]=W_t2[i-1]+np.random.normal(0,1,1)*sqrt(dt)
#    
#print(W_t)
#plt.subplot(212)
#plt.plot(t2,W_t2,c='blue')
#
#plt.show()





