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
import LinRegLearner as lrl  		   	  			    		  		  		    	 		 		   		 		  
import sys
import matplotlib.pyplot as plt
import DTLearner as dtl
import RTLearner as rtl
import BagLearner as bl

import pandas as pd
  		   	  			    		  		  		    	 		 		   		 		  
if __name__=="__main__":  		   	  			    		  		  		    	 		 		   		 		  
    if len(sys.argv) != 2:  		   	  			    		  		  		    	 		 		   		 		  
        print "Usage: python testlearner.py <filename>"  		   	  			    		  		  		    	 		 		   		 		  
        sys.exit(1)  		   	  			    		  		  		    	 		 		   		 		  
    inf = open(sys.argv[1])
    if sys.argv[1]=="Istanbul.csv":
        alldata = np.genfromtxt(inf, delimiter=',')
        data = alldata[1:,1:]

    else:
        data = np.array([map(float,s.strip().split(',')) for s in inf.readlines()])
  		   	  			    		  		  		    	 		 		   		 		  
    # compute how much of the data is training and testing  		   	  			    		  		  		    	 		 		   		 		  
    train_rows = int(0.6* data.shape[0])
    test_rows = data.shape[0] - train_rows  		   	  			    		  		  		    	 		 		   		 		  
  		   	  			    		  		  		    	 		 		   		 		  
    # separate out training and testing data  		   	  			    		  		  		    	 		 		   		 		  
    trainX = data[:train_rows,0:-1]  		   	  			    		  		  		    	 		 		   		 		  
    trainY = data[:train_rows,-1]  		   	  			    		  		  		    	 		 		   		 		  
    testX = data[train_rows:,0:-1]  		   	  			    		  		  		    	 		 		   		 		  
    testY = data[train_rows:,-1]  		   	  			    		  		  		    	 		 		   		 		  
  		   	  			    		  		  		    	 		 		   		 		  
    print testX.shape  		   	  			    		  		  		    	 		 		   		 		  
    print testY.shape  		   	  			    		  		  		    	 		 		   		 		  
  		   	  			    		  		  		    	 		 		   		 		  
    # create a learner and train it  		   	  			    		  		  		    	 		 		   		 		  
    learner = lrl.LinRegLearner(verbose = True) # create a LinRegLearner  		   	  			    		  		  		    	 		 		   		 		  
    learner.addEvidence(trainX, trainY) # train it  		   	  			    		  		  		    	 		 		   		 		  
    print learner.author()  		   	  			    		  		  		    	 		 		   		 		  
  		   	  			    		  		  		    	 		 		   		 		  
    # evaluate in sample  		   	  			    		  		  		    	 		 		   		 		  
    predY = learner.query(trainX) # get the predictions  		   	  			    		  		  		    	 		 		   		 		  
    rmse = math.sqrt(((trainY - predY) ** 2).sum()/trainY.shape[0])  		   	  			    		  		  		    	 		 		   		 		  
    print  		   	  			    		  		  		    	 		 		   		 		  
    print "In sample results"  		   	  			    		  		  		    	 		 		   		 		  
    print "RMSE: ", rmse  		   	  			    		  		  		    	 		 		   		 		  
    c = np.corrcoef(predY, y=trainY)  		   	  			    		  		  		    	 		 		   		 		  
    print "corr: ", c[0,1]  		   	  			    		  		  		    	 		 		   		 		  
  		   	  			    		  		  		    	 		 		   		 		  
    # evaluate out of sample  		   	  			    		  		  		    	 		 		   		 		  
    predY = learner.query(testX) # get the predictions  		   	  			    		  		  		    	 		 		   		 		  
    rmse = math.sqrt(((testY - predY) ** 2).sum()/testY.shape[0])  		   	  			    		  		  		    	 		 		   		 		  
    print  		   	  			    		  		  		    	 		 		   		 		  
    print "Out of sample results"  		   	  			    		  		  		    	 		 		   		 		  
    print "RMSE: ", rmse  		   	  			    		  		  		    	 		 		   		 		  
    c = np.corrcoef(predY, y=testY)  		   	  			    		  		  		    	 		 		   		 		  
    print "corr: ", c[0,1]

    leaf_total =100
    outofCorr = np.ones(leaf_total, dtype = 'float64')
    inCorr = np.ones(leaf_total,dtype = 'float64')
    outofR = np.ones(leaf_total, dtype='float64')
    inR = np.ones(leaf_total, dtype='float64')

    for i in range(1, leaf_total):
        learner = dtl.DTLearner(verbose=True, leaf_size=i)  # create a DTLearner
        learner.addEvidence(trainX, trainY)  # train it
        # print learner.author()

    # evaluate in sample
        predY = learner.query(trainX)  # get the predictions
        rmse = math.sqrt(((trainY - predY) ** 2).sum() / trainY.shape[0])
        # print
        # print "In sample results"
        # print "RMSE: ", rmse
        inR[i] = rmse
        c = np.corrcoef(predY, y=trainY)
        inCorr[i] = c[0,1]
        # print "corr: ", c[0, 1]

    # evaluate out of sample
        predY = learner.query(testX)  # get the predictions
        rmse = math.sqrt(((testY - predY) ** 2).sum() / testY.shape[0])
        # print
        # print "Out of sample results"
        # print "RMSE: ", rmse
        outofR[i] = rmse
        c = np.corrcoef(predY, y=testY)
        outofCorr[i] = c[0,1]
        # print "corr: ", c[0, 1]

    plt.figure(1)
    outofCorr = outofCorr[1:]
    print "DT - Out of sample Correlation maximum when leafsize = ", np.argmax(outofCorr) + 1
    outofCorr = pd.DataFrame(outofCorr, index = range(1,leaf_total))
    inCorr = inCorr[1:]
    inCorr = pd.DataFrame(inCorr, index=range(1,leaf_total))




    df_temp = pd.concat([outofCorr, inCorr], keys=['out of sample Correlation', 'in sample Correlation'], axis=1)
    ax = df_temp.plot(title="DT - Correlation difference", grid=True, fontsize=10)
    ax.set_xlabel("size of leaf")
    ax.set_ylabel("correlation")
    plt.savefig("corr_DTLearner.png")

    plt.figure(3)

    outofR = outofR[1:]
    print "DT - Out of sample rmse minimum when leafsize = ", np.argmin(outofR) + 1
    outofR = pd.DataFrame(outofR, index=range(1, leaf_total))
    inR = inR[1:]
    inR = pd.DataFrame(inR, index=range(1, leaf_total))
    df_temp = pd.concat([outofR, inR], keys=['out of sample RMSE', 'in sample RMSE'], axis=1)
    ax = df_temp.plot(title="DT - RMSE difference", grid=True, fontsize=10)
    ax.set_xlabel("size of leaf")
    ax.set_ylabel("RMSE")
    plt.savefig("rmse_DTLearner.png")


    # plt.savefig("chart.png")
    # plt.plot(outofCorr)
    # plt.plot(inCorr)
    pass

    outofCorr = np.ones(leaf_total, dtype = 'float64')
    inCorr = np.ones(leaf_total,dtype = 'float64')
    outofR = np.ones(leaf_total, dtype = 'float64')
    inR = np.ones(leaf_total, dtype = 'float64')

    for i in range(1, leaf_total):
        learner = rtl.RTLearner(verbose=True, leaf_size=i)  # create a DTLearner
        learner.addEvidence(trainX, trainY)  # train it
        # print learner.author()

    # evaluate in sample
        predY = learner.query(trainX)  # get the predictions
        rmse = math.sqrt(((trainY - predY) ** 2).sum() / trainY.shape[0])
        # print
        # print "In sample results"
        # print "RMSE: ", rmse
        inR[i] = rmse
        c = np.corrcoef(predY, y=trainY)
        inCorr[i] = c[0,1]
        # print "corr: ", c[0, 1]

    # evaluate out of sample
        predY = learner.query(testX)  # get the predictions
        rmse = math.sqrt(((testY - predY) ** 2).sum() / testY.shape[0])
        # print
        # print "Out of sample results"
        # print "RMSE: ", rmse
        outofR[i] =rmse
        c = np.corrcoef(predY, y=testY)
        outofCorr[i] = c[0,1]
        # print "corr: ", c[0, 1]

    plt.figure(2)
    outofCorr = outofCorr[1:]
    print "RT - Out of sample Correlation maximum when leafsize = ", np.argmax(outofCorr) + 1
    outofCorr = pd.DataFrame(outofCorr, index=range(1, leaf_total))
    inCorr = inCorr[1:]
    inCorr = pd.DataFrame(inCorr, index=range(1, leaf_total))

    df_temp = pd.concat([outofCorr, inCorr], keys=['out of sample Correlation', 'in sample Correlation'], axis=1)
    ax = df_temp.plot(title="RT - Correlation difference", grid=True, fontsize=10)
    ax.set_xlabel("size of leaf")
    ax.set_ylabel("correlation")
    plt.savefig("corr_RTLearner.png")

    plt.figure(4)

    outofR = outofR[1:]
    print "RT - Out of sample rmse minimum when leafsize = ", np.argmin(outofR) + 1
    outofR = pd.DataFrame(outofR, index=range(1, leaf_total))
    inR = inR[1:]
    inR = pd.DataFrame(inR, index=range(1, leaf_total))
    df_temp = pd.concat([outofR, inR], keys=['out of sample RMSE', 'in sample RMSE'], axis=1)
    ax = df_temp.plot(title="RT - RMSE difference", grid=True, fontsize=10)
    ax.set_xlabel("size of leaf")
    ax.set_ylabel("RMSE")
    plt.savefig("rmse_RTLearner.png")



    bag_total = 100

    #now bagging vs simple decision Tree
    outofCorr = np.ones(leaf_total, dtype='float64')
    inCorr = np.ones(leaf_total, dtype='float64')
    outofR = np.ones(leaf_total, dtype='float64')
    inR = np.ones(leaf_total, dtype='float64')



    for i in range(leaf_total):
        learner = bl.BagLearner(learner=dtl.DTLearner, kwargs={"leaf_size" : i}, bags=10, verbose=False)
        learner.addEvidence(trainX, trainY)  # train it

        predY = learner.query(trainX)  # get the predictions
        rmse = math.sqrt(((trainY - predY) ** 2).sum() / trainY.shape[0])

        inR[i] = rmse
        c = np.corrcoef(predY, y=trainY)
        inCorr[i] = c[0, 1]

        predY = learner.query(testX)  # get the predictions
        rmse = math.sqrt(((testY - predY) ** 2).sum() / testY.shape[0])

        outofR[i] = rmse
        c = np.corrcoef(predY, y=testY)
        outofCorr[i] = c[0, 1]

    plt.figure(1)
    outofCorr = outofCorr[1:]
    print "BL - Out of sample Correlation maximum when leafsize = ", np.argmax(outofCorr) + 1
    outofCorr = pd.DataFrame(outofCorr, index=range(1, leaf_total))
    inCorr = inCorr[1:]
    print "BL - in sample Correlation maximum when leafsize = ", np.argmax(inCorr) + 1

    inCorr = pd.DataFrame(inCorr, index=range(1, leaf_total))

    df_temp = pd.concat([outofCorr, inCorr], keys=['out of sample Correlation', 'in sample Correlation'], axis=1)
    ax = df_temp.plot(title="Bag - Correlation difference", grid=True, fontsize=10)
    ax.set_xlabel("size of leaf")
    ax.set_ylabel("correlation")
    plt.savefig("corr_BagLearner.png")

    plt.figure(3)

    outofR = outofR[1:]
    print "BL - Out of sample rmse minimum when leafsize = ", np.argmin(outofR) + 1
    outofR = pd.DataFrame(outofR, index=range(1, leaf_total))
    inR = inR[1:]
    print "BL - in sample rmse minimum when leafsize = ", np.argmin(inR) + 1

    inR = pd.DataFrame(inR, index=range(1, leaf_total))
    df_temp = pd.concat([outofR, inR], keys=['out of sample RMSE', 'in sample RMSE'], axis=1)
    ax = df_temp.plot(title="Bag - RMSE difference", grid=True, fontsize=10)
    ax.set_xlabel("size of leaf")
    ax.set_ylabel("RMSE")
    plt.savefig("rmse_BagLearner.png")




    outofCorr = np.ones(leaf_total, dtype='float64')
    inCorr = np.ones(leaf_total, dtype='float64')
    outofR = np.ones(leaf_total, dtype='float64')
    inR = np.ones(leaf_total, dtype='float64')

    for i in range(bag_total):
        learner = bl.BagLearner(learner=dtl.DTLearner, kwargs={"leaf_size" : 10}, bags=i, verbose=False)
        learner.addEvidence(trainX, trainY)  # train it

        predY = learner.query(trainX)  # get the predictions
        rmse = math.sqrt(((trainY - predY) ** 2).sum() / trainY.shape[0])

        inR[i] = rmse
        c = np.corrcoef(predY, y=trainY)
        inCorr[i] = c[0, 1]

        predY = learner.query(testX)  # get the predictions
        rmse = math.sqrt(((testY - predY) ** 2).sum() / testY.shape[0])

        outofR[i] = rmse
        c = np.corrcoef(predY, y=testY)
        outofCorr[i] = c[0, 1]

    plt.figure(1)
    outofCorr = outofCorr[1:]
    print "BL - Out of sample Correlation maximum when bagsize = ", np.argmax(outofCorr) + 1
    outofCorr = pd.DataFrame(outofCorr, index=range(1, bag_total))
    inCorr = inCorr[1:]
    print "BL - in sample Correlation maximum when bagsize = ", np.argmax(inCorr) + 1
    inCorr = pd.DataFrame(inCorr, index=range(1, bag_total))

    df_temp = pd.concat([outofCorr, inCorr], keys=['out of sample Correlation', 'in sample Correlation'], axis=1)
    ax = df_temp.plot(title="Bag - Correlation difference on bagsize", grid=True, fontsize=10)
    ax.set_xlabel("size of leaf")
    ax.set_ylabel("correlation")
    plt.savefig("corr_BagLearner_on_bagsize.png")

    plt.figure(3)

    outofR = outofR[1:]
    print "BL - Out of sample rmse minimum when bagsize = ", np.argmin(outofR) + 1
    outofR = pd.DataFrame(outofR, index=range(1, bag_total))
    inR = inR[1:]
    print "BL - in sample rmse minimum when bagsize = ", np.argmin(inR) + 1
    inR = pd.DataFrame(inR, index=range(1, bag_total))
    df_temp = pd.concat([outofR, inR], keys=['out of sample RMSE', 'in sample RMSE'], axis=1)
    ax = df_temp.plot(title="Bag - RMSE difference on bagsize", grid=True, fontsize=10)
    ax.set_xlabel("size of leaf")
    ax.set_ylabel("RMSE")
    plt.savefig("rmse_BagLearner_on_bagsize.png")




    pass

