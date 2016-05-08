#!/usr/bin/env python

import numpy as np
from sklearn import svm
trainingMatrix = open('/home/cb/Desktop/trainingMatrix.txt')
manInTheMiddleMatrix = open('/home/cb/Desktop/manInTheMiddleMatrix.txt')


def linearSVN(trainingMatrix, testMatrix):
    trainingMatrix = [ map(int,line.split()) for line in trainingMatrix ]
    testMatrix = [ map(int,line.split()) for line in testMatrix ]
    trainingMatrix = np.reshape(trainingMatrix, (len(trainingMatrix), 7))
    print trainingMatrix
    clf = svm.SVC()
    for i in testMatrix:
        print i
        clf.fit(trainingMatrix, i) 
        #dec = lin_clf.decision_function([[1]])
        #dec.shape[1]
    

    
linearSVN(trainingMatrix, manInTheMiddleMatrix)