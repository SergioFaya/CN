# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 19:04:57 2017

@author: UO251005
"""
from __future__ import print_function
import scipy.optimize as sp
import numpy as np
import matplotlib.pyplot as plt

xtol = 1*10**-9
maxiter = 100

f1 = lambda x: x**3 - 75

results = open('./exercise_7.txt', 'w')
print(sp.bisect(f1,3,5,xtol = 1*10**-9,args = () ,maxiter =100, full_output = True), file=results);
results.close(  )

x = np.linspace(-1,20)
y = f1(x);
plt.plot(x,y,'red')
plt.axhline(0, color='green')