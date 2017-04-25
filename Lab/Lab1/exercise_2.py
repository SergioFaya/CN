# -*- coding: utf-8 -*-

from __future__ import print_function
import numpy as np

def de2bi_b(d):
    """
    b = de2bi_a(d):
    Transforms fractional part of a decimal number d into binary b
    d must be positive
    """

    aux = np.fix(d)                      # truncate fractional part
    x = d - aux                         #fractional part
    b = []                             # initialize output as list (to append)
    
    while x*2 != 0 :
        s = x*2
        n = np.fix(s)
        b.append(n)                
        x = s - n                       
        
    b = np.array(b, dtype=np.int8)     
    return b                

        
# MAIN
        
results = open('./exercise_2.txt', 'w')
        
print(de2bi_b(105.8125), file = results)

results.close() 