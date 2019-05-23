"""
Test a learner.  (c) 2015 Tucker Balch

Copyright 2018, Georgia Institute of Technology (Georgia Tech)
Atlanta, Georgia 30332
All Rights Reserved

Template code for CS 4646/7646

Georgia Tech asserts copyright ownership of this template and all derivative
works, including solutions to the projects assigned in this course. Students
and other users of this template code are advised not to share it with others
or to make it available on publicly viewable websites including repositories
such as github and gitlab.  This copyright statement should not be removed
or edited.

We do grant permission to share solutions privately with non-students such
as potential employers. However, sharing with other current or future
students of CS 7646 is prohibited and subject to being investigated as a
GT honor code violation.

-----do not edit anything above this line---
"""

import numpy as np
import math
import DTLearner as dtl
import sys
import matplotlib.pyplot as plt
import pandas as pd

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print "Usage: python testlearner.py <filename>"
        sys.exit(1)
    inf = open(sys.argv[1])
    if sys.argv[1] == "Istanbul.csv":
        alldata = np.genfromtxt(inf, delimiter=',')
        data = alldata[1:, 1:]

    else:
        data = np.array([map(float, s.strip().split(',')) for s in inf.readlines()])

    # compute how much of the data is training and testing
    sys.setrecursionlimit(10000)
    train_rows = int(0.6 * data.shape[0])
    test_rows = data.shape[0] - train_rows

    # separate out training and testing data
    trainX = data[:train_rows, 0:-1]
    trainY = data[:train_rows, -1]
    testX = data[train_rows:, 0:-1]
    testY = data[train_rows:, -1]

    print testX.shape
    print testY.shape

    # create a learner and train it
    leaf_total =100
    outofCorr = np.ones(leaf_total, dtype = 'float64')
    inCorr = np.ones(leaf_total,dtype = 'float64')

    for i in range(1, leaf_total):
        learner = dtl.DTLearner(verbose=True, leafsize=i)  # create a DTLearner
        learner.addEvidence(trainX, trainY)  # train it
        print learner.author()

    # evaluate in sample
        predY = learner.query(trainX)  # get the predictions
        rmse = math.sqrt(((trainY - predY) ** 2).sum() / trainY.shape[0])
        print
        print "In sample results"
        print "RMSE: ", rmse
        c = np.corrcoef(predY, y=trainY)
        inCorr[i] = c[0,1]
        print "corr: ", c[0, 1]

    # evaluate out of sample
        predY = learner.query(testX)  # get the predictions
        rmse = math.sqrt(((testY - predY) ** 2).sum() / testY.shape[0])
        print
        print "Out of sample results"
        print "RMSE: ", rmse
        c = np.corrcoef(predY, y=testY)
        outofCorr[i] = c[0,1]
        print "corr: ", c[0, 1]


    plt.plot(outofCorr)
    plt.plot(inCorr)
    plt.savefig("chart.png")
    pass
