# -*- coding: utf-8 -*-
"""
Created on Tue Feb 07 18:21:58 2017

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
    return b;                # flip upside-down to get correct form

        
# MAIN
        
results = open('./exercise_2.txt', 'w')
        
print(de2bi_b(105.8125), file = results)

results.close() 
        