# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 18:31:00 2017

@author: uo250973
"""
from __future__ import print_function
from __future__ import division

def f(x):
    return x**3 - 2*(x**2) + 1

def df(x):
    return 3*(x**2) - 4*x

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
results = open('./exercise_2.txt', 'w')
print('{:.10e}'.format(newton(-1, tol, 200)), file = results)
print('{:.10e}'.format(newton(1, tol, 200)), file = results)
print('{:.10e}'.format(newton(2, tol, 200)), file = results)
results.close()