#!/usr/bin/env python

#Create an average of the known matrix. 

def averageKnownMatrix(filename):
    #Start by averaging the training matrix.
    x = open(filename)
    x = [ map(int,line.split()) for line in x ]
    summation = [0] * 12
    trainingAverage = [0] * 12
    for i in x:
        for index, value in enumerate(i):
            summation[index] = summation[index] + value
    for index, value in enumerate(summation):
        trainingAverage[index] = summation[index]/len(x)
    return trainingAverage;