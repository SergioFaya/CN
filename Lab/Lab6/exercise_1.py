# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 18:07:39 2017

@author: uo250973
"""

import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return np.sin(x)*np.cos(2*np.pi*x)

def df(x):
    return np.cos(x) * np.cos(2 * np.pi * x) - np.sin(x) * np.sin(2 * np.pi * x) * 2 * np.pi


def frontward(x):
    if(x[0] == 0):
        return derAt0(x)
    elif(x[len(x) - 1] == 2*np.pi):
        return derAtN(x)
    else:
        return (f(x+h)-f(x))/h

def backward(x):
    if (x[0] == 0):
        return derAt0(x)
    elif (x[len(x) - 1] == 2*np.pi):
        return derAtN(x)
    else:
        return (f(x) - f(x-h))/h
    
def centered(x):
    if(x[0] == 0):
        return derAt0(x)
    elif(x[len(x)-1] == 2*np.pi):
        return derAtN(x)
    else:
        return (f(x+h) - f(x-h))/2*h

def derAtN(x):
    return (1/(2*h))*(3*f(x) - 4*f(x-h) + f(x-2*h))

def derAt0(x):
    return (1/(2*h))*(-3*f(x) + 4*f(x+h) - f(x+2*h));

h = np.pi /100

mesh = np.linspace(0 ,2*np.pi,100)

plt.plot((df(mesh)), color = 'y')
plt.plot(frontward(mesh),color = 'g')
plt.plot(backward(mesh),color = 'b')
plt.plot(centered(mesh),color = 'r')

errb = (df(mesh) - backward(mesh))/df(mesh)
errf = (df(mesh) - frontward(mesh))/df(mesh)
errc = (df(mesh) - centered(mesh))/df(mesh)
errg = (df(mesh) - np.gradient(mesh))/df(mesh)
err = np.array([errb, errf, errc, errg])
np.savez('exercise_1', err)















