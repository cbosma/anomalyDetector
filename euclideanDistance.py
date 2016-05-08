#!/usr/bin/env python
 
from math import*

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


#Function to compare each packet in the unknown capture to the average of the 
#training packets.      
def findEuclideanDistance(x,y):
    for index, value in enumerate(y):
        print euclidean_distance(x, value);      
    
 
def euclidean_distance(x,y): 
  return sqrt(sum(pow(a-b,2) for a, b in zip(x, y)))
  
findEuclideanDistance(trainingAverage, trainingMatrix)  
findEuclideanDistance(trainingAverage, manInTheMiddleMatrix)