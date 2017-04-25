# -*- coding: utf-8 -*-
"""
Created on Tue Apr 04 18:07:14 2017

@author: uo250973
"""

import numpy as np
from numpy import linalg as LA

def exact(A, b):
    return A ** -1 * b

def jacobi(A, b, x0 = False, tol = 1.e-6, maxiter = 1000):                                                                                                                                                          
    if x0 is False:
        x0 = np.zeros_like(b, dtype=np.float)
                                                                                                                                                                   
    D = np.diag(A)
    R = A - np.diagflat(D)
    
    iter = 0
    i = 0
    error = 1
    x1 = x0
    # Iterate for maxiter times                                                                                                                                                                          
    while (i < maxiter and error > tol):
        x0 = (b - np.dot(R,x0)) / D
        iter = iter + 1
        i+=1
        error = LA.norm(x1 - x0, np.inf)
        x1 = x0
    return x0, iter
    
A = np.array([[4, 3, -1], [4, 5, -3], [-2, 3, -6]])
b = [5, 3, 1]

x1, numiter1 = jacobi(A, b)
x2, numiter2 = jacobi(A, b, x0 = False, tol = 1.e-4)
x3, numiter3 = jacobi(A, b, x0 = 100*np.ones_like(b), tol = 1.e-9)

np.savez('exercise_1', x1=x1, x2=x2, x3=x3,numiter1=numiter1, numiter2=numiter2, numiter3=numiter3)

