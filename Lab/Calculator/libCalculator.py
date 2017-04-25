# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 18:30:30 2017

@author: UO250973
"""

import math


def newton(f, df, x0, tol):
    error = 1
    iterations = 1
    x = x0
    while (error > tol):
        Xk = x - (f(x)/df(x))
        error = math.fabs(Xk-x)
        x = Xk
        iterations = iterations+1
    return Xk, iterations-1

def getExp(e):
    e = float(e)
    exp = 0
    #We have an integer number, or a x.yz number
    if (e>=1):
        while (e>=1):
            e=e/10
            exp=exp+1
    #We have a decimal 0.xyz number        
    else:
        while (e<1):
            e = e*10
            exp=exp-1
            
    return exp

def inverse(n):
    if (n[0] == '-' or n[0] == '+'):
        sign = n[0]
    else:
        sign = '+'
    num=float(n)
    num=abs(num)
    exp = getExp(num)
    if(exp>0):
        x0=10**-exp
    else:
        x0=10**exp
    x1=0.0
    f = lambda x: x*(2-num*x)
    count = 0
    while(abs(x1-x0)>10**-16):
        count = count + 1
        x1 = x0
        x0=f(x0)
    result = f(x0)
    if(sign == '-'):
        resultToReturn = [result*(-1), count]
        return resultToReturn
    else:
        resultToReturn = [result, count]
        return resultToReturn
    
def sqrt(n):
    num = float(n)
    f = lambda x: num**inverse("2")[0] - x
    df = lambda x: -1   
    return newton(f, df, num, 10**-10)


def cbrt(n):
    num = float(n)
    f = lambda x: num**inverse("3")[0] - x
    df = lambda x: -1   
    return newton(f, df, num, 10**-10)    


