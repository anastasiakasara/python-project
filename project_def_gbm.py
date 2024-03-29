#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 13:23:02 2018

@author: natasa
"""
import os
print(os.getcwd())
os.chdir("/users/lamprosnikolopoulos/pythonwork")



import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
#from datetime import date

from scipy import stats
#tickers = ['AAPL', 'MSFT', '^GSPC']
from datetime import datetime
from iexfinance.stocks import Stock
from iexfinance.stocks import get_historical_data


def read_data():
    global df   
    
    # here the input routines should be  entered
##    
#    start = datetime(2017, 1, 1)
#    end   = datetime(2018, 1, 1)
    
    ticker = input('Company ticker:')
    
    day_i = [int(i) for i in input("Insert initial date: day month year:  ").split()]
    day_f = [int(i) for i in input("Insert final date: day month year:  ").split()]
    
    print(day_i)
#    input('Provide start year, month, day')
#    yst    = int(input())
#    mst    = int(input())
#    dst    = int(input())
#    input('Provide end year, month, day')
#    yed    = int(input())
#    med    = int(input())
#    ded    = int(input())  
#   
#    
#    print(yst,mst,dst)
#    print(yed,med,ded)
#    
    start_1 = datetime(day_i[2], day_i[1], day_i[0])
    end_1   = datetime(day_f[2], day_f[1], day_f[0])
#    
    print(start_1)
    print(end_1)
   
    
    df = get_historical_data(ticker, start=start_1, end=end_1, output_format='pandas')
    
    
def check_data():
    global x  
    df.head()
    df.shape
    x=df['close']  # Share price
    #x.drop(x.index[0], inplace=True)
    # x=df.loc[:,['close']] keeps the index
    #x.drop(x.index[:1], inplace=True)
    x.shape
    x.head(20)
    x.tail()
    plt.plot(x)
    plt.show()
    x[28]
    (len(x))
#
#    
def analyze_data():
    from scipy.stats import sem, t
    from scipy import mean
    from scipy import sqrt
    from scipy.stats import chi2  
    import math
    
    x=df['close']    
    t1=len(x)
    dx=x.diff()
    dx.drop(x.index[0], inplace=True)
    dx.head()
    Y =np.zeros(len(dx))
    (len(Y))   
    for i in range(1,len(x)):   
        #    dx[i-1] = x[i]-x[i-1]
     Y[i-1]=dx[i-1]/x[i-1]
     #    print(i)

    print(np.mean(Y))
    
      
    s01= np.std(Y)
    m01= np.mean(Y)
    v01=s01*s01

    print('s01 =', s01)
    print('m01 =' , m01)
    print('v01 =',v01)

    Y[0]    
    n=len(Y)
    print(n)
    
    #confidence interval for the mean 95% 
 
    confidence = 0.95

    std_err = sem(Y) #  sd = s01/sqrt(n)
    h = std_err * t.ppf((1 + confidence) / 2, n - 1)

    start = m01 - h
    end =m01 + h
    print('start' ,start, 'm01', m01 ,'end', end)
    
     #  standard deviation
    crit_u=stats.chi2.ppf((1-confidence)/2,n-1)
    crit_l=stats.chi2.ppf((1+confidence)/2,n-1)
    s_l=sqrt((n-1)*s01**2/crit_l)
    s_u=sqrt((n-1)*s01**2/crit_u)
    ((s_l,s01,s_u)) #confidence interval
    
   
    logx0 = np.log(x[t1-1])
    t=np.arange(0,20)                 # relative future from the end datetime (2018, 12, 31)
    y_t= logx0 + m01 * t       # mean value for ln(S(t))=G(t)
    st=np.exp(y_t)                     # mean of stock price 
    st_l=np.exp(y_t-1.96*s01*sqrt(t))
    st_u=np.exp(y_t+1.96*s01*sqrt(t))
    st[0]
    st_l[0]
    st_u[0]
    tt =t+t1
    t_1= np.arange(0,t1) 
    ###############################################
 ##### plot the future share price 
    
    
   

    
    plt.plot(t_1,x)
    plt.plot(tt,st_l,tt,st,tt,st_u,t_1,x)

   
    plt.show()
    print(t1)
    print(st)
    

#########################################################


    ##########################################
#

 