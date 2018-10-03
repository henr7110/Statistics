#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 19:00:55 2017

@author: Henrik
"""
import math as m
import matplotlib.pyplot as plt
import numpy as np


def malinger(values,variances):
    
    inversevar = 0
    inversevart = []
    
    for i in variances:
        inversevar += 1/(i**2)
        inversevart.append(1/(i**2))
    
    mean = 0
    weight = []
    meanweight = []
    for i in range(len(variances)):
        weight.append(((1/(variances[i]**2))/inversevar))
        meanweight.append(((1/(variances[i]**2))/inversevar)*values[i])
        mean += ((1/(variances[i]**2))/inversevar)*values[i]
    
    variance = m.sqrt((1/(inversevar)))
    
    table1 = []
    table1.append(["mean","variance","1/variance","weight","weightedmean"])
    for i in range(len(values)):
        table1.append([round(values[i],3),round(variances[i],3),round(inversevart[i],3),round(weight[i],3),round(meanweight[i],3)])
    
    print "\n"
    for i in range(len(table1)):
        if i == 0:
            b = [str(a) for a in table1[i]]
            print ", ".join(b)
        else:
            b = [str(a) for a in table1[i]]
            print ",    ".join(b)
    print "\n"
    print "mean = " + str(round(mean,3)) + "      variance = " + str(round(variance,3)) + "        sum 1/variance^2 = " + str(round(inversevar,3))

def table(table1):
    for i in range(len(table1)):
        if i == 0:
            b = [str(a) for a in table1[i]]
            print ", ".join(b)
        else:
            b = [str(a) for a in table1[i]]
            print ",    ".join(b)

def linje(x1,y1):
    x,y = np.array(x1),np.array(y1)
    mxy = np.mean(x*y)
    mx = np.mean(x)
    my = np.mean(y)
    dx2 = np.mean(x**2)-(mx**2)
    a_0 = ((mxy)-(mx*my))/(dx2)
    b_0 = ((np.mean(x**2)*(my))-(mx*mxy))/dx2
    
    out = []
    print "x       y "
    for i in range(len(x)):
        out.append([x[i],y[i]])
        
    table(out)
    print "\n"
    table([["<xy>","         <x>","       <y>","       dx^2"],[round(mxy,3),round(mx,3),round(my,3),round(dx2,3)]])
    print "\n"
    print "A = " + str(round(a_0,10)) + " B = " + str(round(b_0,10))
    
    
        