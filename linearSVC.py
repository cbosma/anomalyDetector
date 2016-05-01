#!/usr/bin/env python

from sklearn import svm
trainingMatrix = '/home/cb/Desktop/trainingMatrix.txt'
manInTheMiddleMatrix = '/home/cb/Desktop/manInTheMiddleMatrix.txt'



def linearSVN(trainingMatrix, testMatrix):
    lin_clf = svm.LinearSVC()
    lin_clf.fit(trainingMatrix, testMatrix) 
    dec = lin_clf.decision_function([[1]])
    dec.shape[1]
    
linearSVN(trainingMatrix, manInTheMiddleMatrix)