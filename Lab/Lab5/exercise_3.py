# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 18:44:52 2017

@author: uo250973
"""

import numpy as np
import matplotlib.pyplot as plt


def spline_natural(x, nodes, values):
    h0 = nodes[1] - nodes[0]    
    h1 = nodes[2] - nodes[1]    
    h2 = nodes[3] - nodes[2]    
    h3 = nodes[4] - nodes[3]    
    H = np.matrix([[2*(h0 + h1), h1, 0], [h1, 2*(h1 + h2), h2], [0, h2, 2*(h2 + h3)]])
    delta0 = (values[1] - values[0]) / h0
    delta1 = (values[2] - values[1]) / h1
    delta2 = (values[3] - values[2]) / h2
    delta3 = (values[4] - values[3]) / h3
    d0 = delta1 - delta0
    d1 = delta2 - delta1
    d2 = delta3 - delta2
    d = np.matrix([[d0], [d1], [d2]])
    W = H ** (-1) * d
    W = 6 * W
    Wfinal = np.matrix([[0], [W[0]], [W[1]], [W[2]], [0]])
    a0 = (values[0] / h0) - (Wfinal[0] * h0 / 6) 
    a1 = (values[1] / h1) - (Wfinal[1] * h1 / 6) 
    a2 = (values[2] / h2) - (Wfinal[2] * h2 / 6) 
    #a = np.matrix([[a0], [a1], [a2]])
    b0 = (values[1] / h0) - (Wfinal[1] * h0 / 6) 
    b1 = (values[2] / h1) - (Wfinal[2] * h1 / 6) 
    b2 = (values[3] / h2) - (Wfinal[3] * h2 / 6) 
    #b = np.matrix([[b0], [b1], [b2]])
    f1 = (Wfinal[1] * ((nodes[2] - x)**3) / (6 * h1)) + (Wfinal[2] * ((x - nodes[1])**3) / (6 * h1)) + a1[0] * (nodes[2] - x) + b1[0] * (x - nodes[1]) 
    return f1;
        
    
nodes = [2,3,4,5,6]
values = [3,6,2,1,3]
mesh = np.linspace(2,6,100)

v = spline_natural(mesh, nodes, values)
np.savez('exercise_3', v)
print(v)

plt.plot(v)
#plt.plot(y, color='blue')