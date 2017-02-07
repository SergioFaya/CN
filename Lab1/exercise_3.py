# -*- coding: utf-8 -*-
"""
Created on Tue Feb 07 18:39:35 2017

@author: UO251005
"""

from __future__ import print_function
import numpy as np

def de2bi_b(d):
    aux =  np.fix(d);
    x = d - aux;
    b = [] 
    while x*2 <> 0 :
        solution = x*2;
        bit =  np.fix(solution);
        b.append(bit);
        x = solution - bit;
          # compute quotient
        
    b = np.array(b, dtype=np.int8)     
    return b;
    
def de2bi_a(d):
    """
    b = de2bi_a(d):
    Transforms integer part of a decimal number d into binary b
    d must be positive
    """

    x = np.fix(d)                      # truncate fractional part
    b = []                             # initialize output as list (to append)
    
    while x/2 > 0 :
        b.append(x%2)                  # compute remainder
        x = x//2                       # compute quotient
        
    b = np.array(b, dtype=np.int8)     
    return np.flipud(b)
    
def ieee754(d):
    
    b= np.array([])
    mantissa = np.array([])
    entera = de2bi_a(d)
    decimal = de2bi_b(d)
    print(int(d)>=0)
    
    if(int(d)>=0):
        zero = np.array([0])
        print(zero)
        b = np.append(b,zero)
    else:
        one = np.array([1])
        b= np.append(b,one)
    exponent = entera.size;
    exp2 = exponent +126;
    binexp= de2bi_a(exp2);
    np.append(b,binexp)
    mantissa = np.concatenate((entera,decimal))
    mantissa = np.delete(mantissa,0);
    b = np.array(b, dtype=np.int8)  
    b = np.concatenate((b,mantissa))    
    while(b.size < 32):
        print(b.size)
        b= np.append(b,0)
    
 #   b = np.array(b, dtype=np.int8)     
    return b;
    
results = open('./exercise_3.txt', 'w')
        
print(ieee754(120.875), file = results)

results.close() 
    
    
    