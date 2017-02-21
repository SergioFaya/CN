# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 19:04:57 2017

@author: UO251005
"""
from __future__ import print_function
import scipy.optimize as sp
import numpy as np
import matplotlib.pyplot as plt

f0 = lambda x: x
f1 = lambda x: np.exp(-x)
f2 = lambda x: (x + np.exp(-x))/2
f3 = lambda x: -np.log(x)

x = np.linspace(0,1)
y1 = f0(x);
y2 = f1(x);
y3 = f2(x);
y4 = f3(x);
plt.plot(x,y1,'red')
plt.plot(x,y2,'black')
plt.plot(x,y3,'green')
plt.plot(x,y4)

def g1(x):
    return  np.exp(-x)

def g2(x):
    return (x + np.exp(-x))/2

def g3(x):
    return -np.log(x)


def fixedpoints1(x0, tol, maxiter):
    error = 1;
    i = 0;
    x = x0
    while ( error > tol and i < maxiter):
        xk = g1(x)
        error = abs(xk - x)
        x = xk
        i+=1
    return i
    
def fixedpoints2(x0, tol, maxiter):
    error = 1;
    i = 0;
    x = x0
    while ( error > tol and i < maxiter):
        xk = g2(x)
        error = abs(xk - x)
        x = xk
        i+=1
    return i
    
def fixedpoints3(x0, tol, maxiter):
    error = 1;
    i = 0;
    x = x0
    while ( error > tol and i < maxiter):
        xk = g3(x)
        error = abs(xk - x)
        x = xk
        if(np.isnan(x)):
            return -1;
        i+=1
    return i
tol = 1*10**-16
results = open('./exercise_8.txt', 'w')
print('{:d}'.format(fixedpoints1(0.5,tol,200)), file=results)
print('{:d}'.format(fixedpoints2(0.5,tol,200)), file=results)
print('{:d}'.format(fixedpoints3(0.5,tol,200)), file=results)
results.close()
