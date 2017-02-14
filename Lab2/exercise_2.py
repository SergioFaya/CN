from __future__ import print_function
from __future__ import division 
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**3 - 2*x**2 + 1

def f_prime(x):
    return 3*x**2 - 4*x

def newton(x0, tol, maxiter):
    error = 1
    it = 1
    x = x0
    while (error>tol or it<maxiter):
        if(f_prime(x) == 0):
            return x
        else:
            xk = x - (f(x) / f_prime(x))
            error = abs(xk-x)
            x = xk
            it += 1
    return xk
tol = 1*10**-9


results = open('./exercise_2.txt', 'w')
print('{:10e}'.format(newton(-1, tol,  200)), file = results)
print('{:10e}'.format(newton(1, tol, 200)), file = results)
print('{:10e}'.format(newton(2, tol, 200)), file = results)
results.close()