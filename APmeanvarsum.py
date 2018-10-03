
#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 29 19:00:55 2017

@author: Henrik
"""
import math as m
import matplotlib.pyplot as plt
import numpy as np
from iminuit import Minuit
from scipy import stats
from probfit import Chi2Regression # , BinnedChi2 # , BinnedLH#, , UnbinnedLH, , , Extended
plt.close('all')

def malinger(values,variances):
    """script that takes indepentent values, variances and spits out mean and
    variance...
    INCLUDE chi2, Ndf, p-value"""
    #Add values, get mean and variances based on multiple independent measure-
    #ments of same thing
    #make chi-square fit based on real mean (fit straight line)

    Nvar = 1
    Ndof_calc = len(values) - Nvar

    def fit_function(x, alpha0):
        return alpha0

    chi2_object = Chi2Regression(fit_function, np.array(range(len(values))), np.array(values), np.array(variances))

    minuit = Minuit(chi2_object, pedantic=False, alpha0=np.mean(values), print_level=0)
    minuit.migrad();  # perform the actual fit
    minuit_output = [minuit.get_fmin(), minuit.get_param_states()] # save the output parameters in case needed

    alpha0_fit = minuit.values['alpha0']
    sigma_alpha0_fit = minuit.errors['alpha0']
    Chi2_fit = minuit.fval # the chi2 value
    Prob_fit =  stats.chi2.sf(Chi2_fit, Ndof_calc) # The chi2 probability given N degrees of freedom (Ndof)


    print ("alpha0 = " + str(alpha0_fit) + ", sigma_alpha0_fit= " + str(sigma_alpha0_fit) + ", Chi2 = "
           + str(Chi2_fit) + ", P-val = " + str(Prob_fit))

    table1 = []
    table1.append(["mean","variance"])
    for i in range(len(values)):
        table1.append([round(values[i],3),round(variances[i],3)])

    table(table1)

    return alpha0_fit, sigma_alpha0_fit, Chi2_fit, Prob_fit


def table(table1):
    for i in range(len(table1)):
        if i == 0:
            b = [str(a) for a in table1[i]]
            print (", ".join(b))
        else:
            b = [str(a) for a in table1[i]]
            print (",    ".join(b))

def linje(x1,y1):
    x,y = np.array(x1),np.array(y1)
    mxy = np.mean(x*y)
    mx = np.mean(x)
    my = np.mean(y)
    dx2 = np.mean(x**2)-(mx**2)
    a_0 = ((mxy)-(mx*my))/(dx2)
    b_0 = ((np.mean(x**2)*(my))-(mx*mxy))/dx2

    out = []
    print ("x       y ")
    for i in range(len(x)):
        out.append([x[i],y[i]])

    table(out)
    print ("\n")
    table([["<xy>","         <x>","       <y>","       dx^2"],[round(mxy,3),round(mx,3),round(my,3),round(dx2,3)]])
    print ("\n")
    print ("A = " + str(round(a_0,10)) + " B = " + str(round(b_0,10)))

np.random.seed(42)
malinger(range(8),np.random.normal(loc=3,scale=1,size=8))
