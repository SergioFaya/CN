# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 18:05:14 2017

@author: uo250973
"""

import numpy as np
import matplotlib.pyplot as plt


def lagrange_fundamental(index, x, nodes):
    numerador = 1;
    denominador = 1;
    for i in range(0, len(nodes)):
        if (i != index):
            numerador = numerador * (x - nodes[i])
            denominador = denominador * (nodes[index] - nodes[i])
            
    result = numerador / denominador;
    return result;
    
def lagrange_polynomial(x, nodes, values):
    result = 0;
    for i in range(0, len(nodes)):
        result = result + values[i] * lagrange_fundamental(i, x, nodes)
    return result;
    
nodes = [2,3,4,5,6]
values = [2,6,5,5,6]
mesh = np.linspace(2,6,100)

v = lagrange_polynomial(mesh, nodes, values)
y = lagrange_fundamental(2, mesh, nodes)
np.savez('exercise_1', v)
print(v)

#plt.plot(v, color='red')
plt.plot(y, color='blue')
