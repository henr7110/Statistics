#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 19:28:09 2017

@author: Henrik
"""
import math as m
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import numpy as np

def mean(x1,x2):
    return (((1/x1**2)/((1/x1**2)+(1/x2**2))*x1+((1/x2**2)/((1/x1**2)+(1/x2**2))*x2)))

def variance(v1,v2):
    return 1/((1/v1**2)+(1/v2**2))

means = [3.4,3.6,3.1]
variances = [0.3,0.1,0.2,]

meanf = 3.2
variancef = 0.2

for i in range(len(means)):
    meanf = mean(meanf,means[i])
    variancef = variance(variancef,variances[i])
    x = np.linspace(2.5,4,400)
    plt.plot(x,mlab.normpdf(x,meanf,m.sqrt(variancef)),label= "sample "+ str(i),)
        
print meanf, variancef, m.sqrt(variancef) 
plt.legend()
plt.show()
               
