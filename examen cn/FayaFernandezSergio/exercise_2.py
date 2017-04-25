# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 18:40:26 2017

@author: UO251005
"""

import numpy as np
import matplotlib.pyplot as plt
def euler_explicit_system(F,f10,f20,T,timeStep):
    i = 0;
    f1 = np.zeros((20001,));
    f2 = np.zeros((20001,));
    mesh = np.zeros((20001,));    
    f1[0] = f10;
    f2[0] = f20;
    while i<20000:
        f1[i+1] = f1[i]+timeStep*f2[i]
        f2[i+1] = f2[i]+timeStep*F(f1[i],f2[i])
        mesh[i]=i
        i+=1;
    return f1,f2,mesh;
    
def F(x,y):
    return -x -0.25*y;

f1,f2,mesh = euler_explicit_system(F,0,1,20,0.001)
plt.plot(mesh,f1)
np.savez('exercise_2',f1)


