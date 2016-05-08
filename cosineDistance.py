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
def cosineDistance(x,y):
    for index, value in enumerate(y):
        print cosine_similarity(x, value);       

def square_rooted(x): 
   return round(sqrt(sum([a*a for a in x])),3)
 
def cosine_similarity(x,y):
 
 numerator = sum(a*b for a,b in zip(x,y))
 denominator = square_rooted(x)*square_rooted(y)
 return round(numerator/float(denominator),3)
  
cosineDistance(trainingAverage, trainingMatrix)  
cosineDistance(trainingAverage, manInTheMiddleMatrix)