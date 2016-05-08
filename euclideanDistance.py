#!/usr/bin/env python
 
from math import*
import numpy as np
from numpy import dot, array
from pcapparser.config import out



trainingMatrix = open('/home/cb/Desktop/trainingMatrix.txt')
manInTheMiddleMatrix = open('/home/cb/Desktop/manInTheMiddleMatrix.txt')
trainingMatrix = [ map(int,line.split()) for line in trainingMatrix ]
manInTheMiddleMatrix = [ map(int,line.split()) for line in manInTheMiddleMatrix ]
#Start by averaging the training matrix.
summation = [0] * 10
trainingAverage = [0] * 10
for i in trainingMatrix:
    for index, value in enumerate(i):
        summation[index] = summation[index] + value
for index, value in enumerate(summation):
    trainingAverage[index] = summation[index]/len(trainingMatrix)
       
def test_each_packet(x,y):
    for index, value in enumerate(y):
        print x
        print value
        #weights = [.1,.1,1,1,1,1,1]
        #weightedX = (array(x).transpose() * weights)
        #weightedY = (array(value).transpose() * weights)
        
        #print weightedX
       # print weightedY
        print euclidean_distance(x, value);      
    
 
def euclidean_distance(x,y):
 
  return sqrt(sum(pow(a-b,2) for a, b in zip(x, y)))
  
test_each_packet(trainingAverage, trainingMatrix)  
#test_each_packet(trainingAverage, manInTheMiddleMatrix)


