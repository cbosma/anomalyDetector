#!/usr/bin/env python

from sklearn import svm
trainingMatrix = open('/home/cb/Desktop/trainingMatrix.txt')
manInTheMiddleMatrix = open('/home/cb/Desktop/manInTheMiddleMatrix.txt')


def linearSVN(trainingMatrix, testMatrix):
    trainingMatrix = [ map(int,line.split()) for line in trainingMatrix ]
    testMatrix = [ map(int,line.split()) for line in testMatrix ]
    print trainingMatrix
    print testMatrix
    lin_clf = svm.LinearSVC()
    lin_clf.fit(trainingMatrix, testMatrix) 
    dec = lin_clf.decision_function([[1]])
    dec.shape[1]
    

    
linearSVN(trainingMatrix, manInTheMiddleMatrix)