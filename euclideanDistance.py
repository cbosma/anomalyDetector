#!/usr/bin/env python
 
from math import sqrt, pow
 
#Compute the distance 
def euclidean_distance(x,y): 
    return sqrt(sum(pow(a-b,2) for a, b in zip(x, y)))