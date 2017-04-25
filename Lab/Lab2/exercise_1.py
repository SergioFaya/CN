# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 18:07:00 2017

@author: uo250973
"""
from __future__ import print_function
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**3 - 2*x**2 + 1

def bisection(a, b, tol, maxiter):
    c = (a + b) / 2.0
    i = 1
    while (b-a)/2.0 > tol or i<maxiter: 
        if (f(c) == 0):
            return c
        elif f(a)*f(c) < 0:
            b = c
        else:
            a = c
        c = (a + b) / 2.0
        i+=1
    return c

tol = 1*10**-9
results = open('./exercise_1.txt', 'w')

print('{:.10e}'.format(bisection(-1,0,tol,200)), file = results)
print('{:.10e}'.format(bisection(0,1,tol,200)), file = results)
print('{:.10e}'.format(bisection(1,2,tol,200)), file = results)
results.close()

x = np.arange(-1, 2, 0.1)
y = f(x)
plt.plot(x,y)