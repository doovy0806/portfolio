'''
gt id : 903456821
account : hku35
name : Ku, Han Mo
'''


import numpy as np



class BagLearner(object):


    def __init__(self, learner = None, kwargs = {}, bags = 1, boost = False, verbose=False):
        self.kwagrs = kwargs
        self.bags = bags
        self.boost = boost
        self.learners=[]
        self.verbose = verbose
        for i in range(0,bags):
            self.learners.append(learner(**kwargs))




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



        bagsize = int(dataX.shape[0]*(10/6.0))
        for i in range(0,self.bags):
            indexes = np.random.choice(dataX.shape[0], size = bagsize, replace= True)
            # newX = dataX[:,indexes]
            # newY = dataY[indexes]
            self.learners[i].addEvidence(dataX[indexes,:], dataY[indexes])




    def query(self, points):
        """
        @summary: Estimate a set of test points given the model we built.
        @param points: should be a numpy array with each row corresponding to a specific query.
        @returns the estimated values according to the saved model.
        """
        predicted_y = np.zeros((1,points.shape[0]))

        for i in range(0,self.bags):
            predicted_y = predicted_y + self.learners[i].query(points)
        predicted_y = predicted_y/self.bags
        return predicted_y

        # return (self.model_coefs[:-1] * points).sum(axis=1) + self.model_coefs[-1]





if __name__ == "__main__":
    print "the secret clue is 'zzyzx'"





