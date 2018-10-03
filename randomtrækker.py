#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 09:59:00 2017

@author: Henrik
"""

import numpy as np
import random as r
import matplotlib.pyplot as plt

#generate bag

class bag:
    def __init__(self,black,white):
        self.black = black
        self.white = white
        
    def pull(self):
        draw = r.randint(0,self.white+self.black)
        if draw <= self.white:
            self.white -= 1
            return 1.0
        else:
            self.black -= 1
            return 0.0

def run(black,white,rep):

    runs = np.zeros(black+white)
    for i in range(rep):
        if i % 1000 == 0:
            print i
        b = bag(black,white)
        r = []
        for i in range(black+white):
            r.append(b.pull())
        runs += np.array(r)
        
    print np.mean(runs/rep)
    print np.var(runs/rep)
    plt.plot(np.zeros(len(runs))+np.mean(runs/rep))
    plt.plot(runs/rep)
    plt.title("%d experiments with draws from a bag of %d white and %d black" %(rep, white, black))
    plt.legend(["mean number of whites", "whites pr. run"])
    plt.xlabel("N")
    plt.ylabel("P")
    plt.show()

         
        