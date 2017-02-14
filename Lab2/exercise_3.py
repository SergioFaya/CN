from __future__ import print_function
from __future__ import division 

def f(x):
    return x ** 3 - 2 * x ** 2 + 1

def secant(x0, x1, tol, maxiter):
    error = 1
    i = 1
    x = x0
    while (error > tol or i < maxiter):
        if (f(x1) - f(x0) == 0):
            return x0
        else:
            op = (x1-x0) / (f(x1)-f(x0))
            x = x1 - f(x1) * op
            error = abs(x-x1)
            x0 = x1
            x1 = x
            i = i+1
    return x

tol = 1*10**-9
results = open('./exercise_3.txt', 'w')
print('{:10e}'.format(secant(-1,0, tol, 200)), file = results)
print('{:10e}'.format(secant(0, 1, tol, 200)), file = results)
print('{:10e}'.format(secant(2,3 , tol, 200)), file = results)

results.close()