import numpy as np
import BagLearner as bl
import LinRegLearner as lrl
class InsaneLearner(object):
    def __init__(self, verbose=False):
        pass  # move along, these aren't the drones you're looking for
    def author(self):
        return 'hku35'  # replace tb34 with your Georgia Tech username
    def addEvidence(self, dataX, dataY):
        self.learners = []
        for i in range(20):
            self.learners.append(bl.BagLearner(learner=lrl.LinRegLearner, bags=20))
            self.learners[i].addEvidence(dataX, dataY)
    def query(self, points):
        predicted_y = np.zeros((points.shape[0]))
        for i in range(20):
            predicted_y = predicted_y+self.learners[i].query(points)
        return predicted_y/20
if __name__ == "__main__":
    print "the secret clue is 'zzyzx'"
