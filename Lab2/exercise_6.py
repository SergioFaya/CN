
# -*- coding: utf-8 -*-
from __future__ import print_function
import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as sp

def f(x):
    return np.cosh(x)* np.cos(x) - 1;

f1 = lambda x: np.cosh(x)* np.cos(x) - 1;
results = open('./exercise_6.txt', 'w')
print('{:.10e}'.format(sp.newton(f1,5)), file=results)
results.close()
#x = np.linspace(-1,20)
#y = f1(x);
#plt.plot(x,y,'red')
#plt.axhline(0, color='green')