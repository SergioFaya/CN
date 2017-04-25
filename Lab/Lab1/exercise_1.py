# -*- coding: utf-8 -*-

from __future__ import print_function
import numpy as np

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
    return np.flipud(b)                # flip upside-down to get correct form

        
# MAIN
        
results = open('./exercise_1.txt', 'w')
        
print(de2bi_a(105.8125), file = results)

results.close() 
