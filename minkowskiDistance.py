#!/usr/bin/env python
 
from math import pow
from decimal import Decimal
 
def nth_root(value, n_root):
    root_value = 1/float(n_root)
    return round (Decimal(value) ** Decimal(root_value),3)

#Compute Minkowski distance 
def minkowski_distance(x,y,p_value): 
    return nth_root(sum(pow(abs(a-b),p_value) for a,b in zip(x, y)),p_value)