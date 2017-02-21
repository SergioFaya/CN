# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 19:04:57 2017

@author: UO251005
"""
from __future__ import print_function
import scipy.optimize as sp
import numpy as np
import matplotlib.pyplot as plt

def g1(x,y):
    return  (x-2)**2 + y**2 -4

def g2(x,y):
    return x**2+(y-3)**2 - 4

x = np.linspace(-2,4)
y = x
y1 = g1(x,y);
y2 = g2(x,y);

plt.plot(x,y1,'red')
plt.plot(x,y2,'black')




tol = 1*10**-16
results = open('./exercise_9.txt', 'w')
print('{:d}'.format(fixedpoints1(0.5,tol,200)), file=results)
print('{:d}'.format(fixedpoints2(0.5,tol,200)), file=results)
print('{:d}'.format(fixedpoints3(0.5,tol,200)), file=results)
results.close()