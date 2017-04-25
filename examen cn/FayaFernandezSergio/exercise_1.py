# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 18:40:26 2017

@author: UO251005 , Faya Fernández Sergio
"""
from __future__ import print_function
from __future__ import division
import matplotlib.pyplot as plt
import math as m
import numpy as np
def f(x):
    return m.e**(-x) - x;

def df(x):
    return (-(m.e)**(-x)) -1;

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

#Plots of the function
mesh = np.linspace(-1 ,1,100);
plt.plot((f(mesh)), color = 'r');
#Print of the zeros and variable saving
tol = 1*10**-9
#Variable that holds the value of newton's xk
x = newton(-1, tol, 200);
results = open('./exercise_1.txt', 'w')
print('{:.10e}'.format(x), file = results)
print(x);
np.savez('exercise_1',x);
results.close()