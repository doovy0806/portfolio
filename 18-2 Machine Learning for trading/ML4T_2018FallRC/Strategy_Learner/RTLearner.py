'''
gt id : 903456821
account : hku35
name : Ku, Han Mo
'''

import numpy as np
import random



class RTLearner(object):
    def __init__(self,leaf_size = 1, verbose=False):
        self.leaf_size = leaf_size
        pass  # move along, these aren't the drones you're looking for

    def author(self):
        return 'hku35'  # replace tb34 with your Georgia Tech username


    def addEvidence(self, dataX, dataY):
        """
        @summary: Add training data to learner
        @param dataX: X values of data to add
        @param dataY: the Y training values
        """

        # slap on 1s column so linear regression finds a constant term - only for linear regression
        # newdataX = np.ones([dataX.shape[0], dataX.shape[1] + 1])
        # newdataX[:, 0:dataX.shape[1]] = dataX

        # build and save the model
        # self.model_coefs, residuals, rank, s = np.linalg.lstsq(newdataX, dataY)

        self.rt = TreeNode(dataX, dataY, np.ones(dataX.shape[0], dtype='bool'), leaf_size = self.leaf_size)

        self.rt.build()


    def query(self, points):
        """
        @summary: Estimate a set of test points given the model we built.
        @param points: should be a numpy array with each row corresponding to a specific query.
        @returns the estimated values according to the saved model.
        """
        predicted_y = np.empty((1,points.shape[0]))
        return self.rt.predict(points,predicted_y, np.ones(predicted_y.shape, dtype='bool'))

        # return (self.model_coefs[:-1] * points).sum(axis=1) + self.model_coefs[-1]





if __name__ == "__main__":
    print "the secret clue is 'zzyzx'"


class TreeNode(object):
    def __init__(self, dataX, dataY, indexes, leaf_size=1):
        self.dataX = dataX
        self.dataY = dataY
        self.indexes = indexes
        self.right = None
        self.left = None
        self.split_val = None
        self.feature = None
        self.ifleaf = -1
        self.leaf_size = leaf_size
        self.leafvalue = None



    def build(self):
        n = np.count_nonzero(self.indexes)
        if np.count_nonzero(self.indexes) > self.leaf_size:
            # corr =np.array([np.corrcoef(self.dataX[self.indexes, i], self.dataY[self.indexes])[0][1] for i in range(self.dataX.shape[1])])
            # #needs to be revised. 1. absoulte correlation, second argmax should consider nan by using nanargmax            self.feature= np.argmax(corr)
            # corr= np.abs(corr)
            # self.feature = np.nanargmax(corr)
            self.feature = random.randrange(0,self.dataX.shape[1])
            self.split_val = np.median(self.dataX[self.indexes, self.feature])
            left_indexes = self.indexes & (self.dataX[:, self.feature] <= self.split_val)
            right_indexes = self.indexes & (self.dataX[:, self.feature] > self.split_val)

            if np.count_nonzero(left_indexes) == 0:
                self.ifleaf = 1
                self.leafvalue = self.dataY[self.indexes].mean(axis=0)
            elif np.count_nonzero(right_indexes) == 0:
                self.ifleaf = 1
                self.leafvalue = self.dataY[self.indexes].mean(axis=0)
            else :
                self.left = TreeNode(self.dataX, self.dataY, left_indexes, leaf_size=self.leaf_size)
                self.right = TreeNode(self.dataX, self.dataY, right_indexes, leaf_size=self.leaf_size)
                self.left.build()
                self.right.build()
        else:
            self.ifleaf = 1
            self.leafvalue = self.dataY[self.indexes].mean(axis=0)
            # please check if the axis should be 0 -- which means dataY is aligned in one row

    def predict(self, testX, testY, testindexes):
        if self.ifleaf>0:
            testY[testindexes] = self.leafvalue
        else :
            left_indexes = testindexes & ( testX[:, self.feature] <= self.split_val)
            right_indexes = testindexes & ( testX[:, self.feature] > self.split_val)
            self.left.predict(testX, testY, left_indexes)
            self.right.predict(testX, testY, right_indexes)
        return testY







