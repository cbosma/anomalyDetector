#!/usr/bin/env python

from sklearn import svm
trainingMatrix = open('/home/cb/Desktop/trainingMatrix.txt').readlines()
manInTheMiddleMatrix = open('/home/cb/Desktop/manInTheMiddleMatrix.txt').readlines()



def linearSVN(trainingMatrix, testMatrix):
    lin_clf = svm.LinearSVC()
    lin_clf.fit(trainingMatrix, testMatrix) 
    dec = lin_clf.decision_function([[1]])
    dec.shape[1]
    
print trainingMatrix
print manInTheMiddleMatrix
    
linearSVN(trainingMatrix, manInTheMiddleMatrix)