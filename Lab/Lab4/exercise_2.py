# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 19:02:35 2017

@author: uo250973
"""

import numpy as np
import matplotlib.pyplot as plt



def divided_differences(nodes, values):
    '''x : array of data points
       y : array of f(x)  '''
    nodes.astype(float)
    values.astype(float)
    n = len(nodes)
    a = []
    for i in range(n):
        a.append(values[i])

    for j in range(1, n):
        for i in range(n-1, j-1, -1):
            a[i] = float(a[i]-a[i-1])/float(nodes[i]-nodes[i-j])

    return a 

def newton_polynomial(x, nodes, values):    
    v = divided_differences(nodes, values)
    result = v[0];
    counter = len(nodes) - 1
    for i in range(1, len(nodes)):
        for j in range(1,p = 1):
            result = result + v[i] * (x - nodes[p])
            if p = 4
    return result;
    
    
nodes = np.array([2,3,4,5,6])
values = np.array([2,6,8,7,6])
mesh = np.linspace(2,6,100)
v = newton polynomial(mesh, nodes, values) 
np.savez('exercise_2', v)
#print(divided_differences(nodes, values))
plt.plot(v)