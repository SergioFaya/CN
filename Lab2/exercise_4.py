# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 19:04:57 2017

@author: UO251005
"""
from __future__ import print_function
from __future__ import division 
import math
import numpy as np
import matplotlib.pyplot as plt


    
    
def f(x):
    return math.exp(-x) - x;

def g(x):
    return math.exp(-x);

def fixedpoints(x0, tol, maxiter):
    error = 1;
    i = 1;
    x = x0
    while ( error > tol or i < maxiter):
        xk = g(x)
        error = abs(xk - x)
        x = xk
        i+=1
    return xk
tol = 1*10**-9  
results = open('./exercise_4.txt', 'w')
print('{:.10e}'.format(fixedpoints(0,tol,200)), file=results)

f1 = lambda x: np.exp(-x) -x;
x = np.linspace(-1,1)
y = f1(x);
plt.plot(x,y)