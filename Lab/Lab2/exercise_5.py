# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 19:29:39 2017

@author: uo250973
"""

from __future__ import print_function
from __future__ import division
import math
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return math.sin(x) - 0.1 * x

def df(x):
    return math.cos(x) - 0.1

def newton(x0, tol, maxiter):
    error = 1
    it = 1
    x = x0
    while (error > tol or it < maxiter):
        if(df(x) == 0):
            return x
        else:
            xk = x - (f(x) / df(x))
            error = abs(xk-x)
            x = xk
            it += 1
    return xk


tol = 1*10**-9
results = open('./exercise_5.txt', 'w')
print('{:.10e}'.format(newton(0, tol, 100)), file = results)
print('{:.10e}'.format(newton(2, tol, 100)), file = results)
print('{:.10e}'.format(newton(6, tol, 100)), file = results)
print('{:.10e}'.format(newton(8, tol, 100)), file = results)
results.close()

f1 = lambda x : np.sin(x) - 0.1 * x
g1 = lambda x : np.cos(x) - 0.1

x = np.linspace(-1, 20)
y = f1(x)
plt.plot(x,y)
plt.axhline(0, color = 'red')