"""  		   	  			    		  		  		    	 		 		   		 		  
template for generating data to fool learners (c) 2016 Tucker Balch  		   	  			    		  		  		    	 		 		   		 		  
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
  		   	  			    		  		  		    	 		 		   		 		  
Student Name: Han Mo Ku(replace with your name)
GT User ID: hku35 (replace with your User ID)
GT ID: 903456821 (replace with your GT ID)
"""  		   	  			    		  		  		    	 		 		   		 		  
  		   	  			    		  		  		    	 		 		   		 		  
import numpy as np  		   	  			    		  		  		    	 		 		   		 		  
import math  		   	  			    		  		  		    	 		 		   		 		  
  		   	  			    		  		  		    	 		 		   		 		  
# this function should return a dataset (X and Y) that will work  		   	  			    		  		  		    	 		 		   		 		  
# better for linear regression than decision trees  		   	  			    		  		  		    	 		 		   		 		  
def best4LinReg(seed=1489683273):
    np.random.seed(seed)  		   	  			    		  		  		    	 		 		   		 		  
    X = np.random.random(size = (100,3))
    Y = X[:,0]**2 + X[:,1]**3 + X[:,2]
    # Here's is an example of creating a Y from randomly generated  		   	  			    		  		  		    	 		 		   		 		  
    # X with multiple columns  		   	  			    		  		  		    	 		 		   		 		  
    # Y = X[:,0] + np.sin(X[:,1]) + X[:,2]**2 + X[:,3]**3  		   	  			    		  		  		    	 		 		   		 		  
    return X, Y  		   	  			    		  		  		    	 		 		   		 		  
  		   	  			    		  		  		    	 		 		   		 		  
def best4DT(seed=1489683273):  		   	  			    		  		  		    	 		 		   		 		  
    np.random.seed(seed)  		   	  			    		  		  		    	 		 		   		 		  
    X = np.random.random((500,3))
    xmed = np.median(X, axis=0)
    temp1 = X[:,0] <= xmed[0]
    temp2 = X[:,1]<= xmed[1]
    temp3 = X[:,2]<= xmed[2]
    first = temp1 & temp2 & temp3

    temp1 = X[:, 0] > xmed[0]
    temp2 = X[:, 1] <= xmed[1]
    temp3 = X[:, 2] <= xmed[2]
    second = temp1 & temp2 & temp3

    temp1 = X[:, 0] <= xmed[0]
    temp2 = X[:, 1] > xmed[1]
    temp3 = X[:, 2] <= xmed[2]
    third = temp1 & temp2& temp3

    temp1 = X[:, 0] <= xmed[0]
    temp2 = X[:, 1] <= xmed[1]
    temp3 = X[:, 2] > xmed[2]
    fourth = temp1 & temp2& temp3

    temp1 = X[:, 0] > xmed[0]
    temp2 = X[:, 1] > xmed[1]
    temp3 = X[:, 2] <= xmed[2]
    fifth = temp1 & temp2& temp3

    temp1 = X[:, 0] > xmed[0]
    temp2 = X[:, 1] <= xmed[1]
    temp3 = X[:, 2] > xmed[2]
    sixth = temp1 & temp2& temp3

    temp1 = X[:, 0] <= xmed[0]
    temp2 = X[:, 1] > xmed[1]
    temp3 = X[:, 2] > xmed[2]
    seventh = temp1 & temp2& temp3

    temp1 = X[:, 0] > xmed[0]
    temp2 = X[:, 1] > xmed[1]
    temp3 = X[:, 2] > xmed[2]
    eightth = temp1 & temp2 & temp3

    ones = first | third | fifth | sixth
    Y = np.zeros((500,))
    Y[ones] = 1

    return X, Y
  		   	  			    		  		  		    	 		 		   		 		  
def author():  		   	  			    		  		  		    	 		 		   		 		  
    return 'hku35' #Change this to your user ID
  		   	  			    		  		  		    	 		 		   		 		  
if __name__=="__main__":  		   	  			    		  		  		    	 		 		   		 		  
    print "they call me Tim."  		   	  			    		  		  		    	 		 		   		 		  
