# -*- coding: utf-8 -*-
"""
Created on Tue Apr 04 19:14:00 2017

@author: uo250973
"""
import numpy as np
from numpy import linalg as LA

    
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
    
def gauss_seidel(A, b, x = False, tol = 1.e-6, maxiter = 1000):
    if x is False:
        x = np.zeros_like(b, dtype=np.float)
        
    L = np.tril(A)
    U = A - L
    i = 0
    error = 1
    x1 = x
    iter = 0
    while (i < maxiter and error > tol):
        x = np.dot(np.linalg.inv(L), b - np.dot(U, x))
        i += 1
        error = LA.norm(x1 - x, np.inf)
        x1 = x
        iter += 1
    return x, iter
    
A = np.array([[4, 3, -1], [4, 5, -3], [-2, 3, -6]])
b = [5, 3, 1]

x1, numiter1 = gauss_seidel(A, b)
x2, numiter2 = jacobi(A, b)

np.savez('exercise_2', x1=x1, x2=x2, numiter1=numiter1,numiter2=numiter2)