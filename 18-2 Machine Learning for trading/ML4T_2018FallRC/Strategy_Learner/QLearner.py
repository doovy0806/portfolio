"""  		   	  			    		  		  		    	 		 		   		 		  
Template for implementing QLearner  (c) 2015 Tucker Balch  		   	  			    		  		  		    	 		 		   		 		  
  		   	  			    		  		  		    	 		 		   		 		  
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
  		   	  			    		  		  		    	 		 		   		 		  
Student Name: Han Mo Ku (replace with your name)
GT User ID: hku35 (replace with your User ID)
GT ID: 903456821 (replace with your GT ID)
"""  		   	  			    		  		  		    	 		 		   		 		  
  		   	  			    		  		  		    	 		 		   		 		  
import numpy as np  		   	  			    		  		  		    	 		 		   		 		  
import random as rand  		   	  			    		  		  		    	 		 		   		 		  
  		   	  			    		  		  		    	 		 		   		 		  
class QLearner(object):  		   	  			    		  		  		    	 		 		   		 		  
  		   	  			    		  		  		    	 		 		   		 		  
    def __init__(self, \
        num_states=100, \
        num_actions = 4, \
        alpha = 0.2, \
        gamma = 0.9, \
        rar = 0.5, \
        radr = 0.99, \
        dyna = 0, \
        verbose = False):  		   	  			    		  		  		    	 		 		   		 		  
  		   	  			    		  		  		    	 		 		   		 		  
        self.verbose = verbose  		   	  			    		  		  		    	 		 		   		 		  
        self.num_actions = num_actions  		   	  			    		  		  		    	 		 		   		 		  
        self.s = 0
        self.a = 0
        self.num_states = num_states
        self.qtable = np.zeros((self.num_states, self.num_actions))
        self.T_c = np.zeros((self.num_states, self.num_actions, self.num_states))
        self.T = np.zeros((self.num_states, self.num_actions, self.num_states))
        self.T_a = np.zeros((self.num_states, self.num_actions, self.num_states))
        self.T_c[:,:,:] = 0.00001
        self.T[:,:,:]=1/self.num_states
        self.R = np.zeros((self.num_states,self.num_actions))

        self.alpha = alpha
        self.gamma = gamma
        self.rar = rar
        self.radr = radr
        self.dyna = dyna

  		   	  			    		  		  		    	 		 		   		 		  
    def querysetstate(self, s):  		   	  			    		  		  		    	 		 		   		 		  
        """  		   	  			    		  		  		    	 		 		   		 		  
        @summary: Update the state without updating the Q-table  		   	  			    		  		  		    	 		 		   		 		  
        @param s: The new state  		   	  			    		  		  		    	 		 		   		 		  
        @returns: The selected action  		   	  			    		  		  		    	 		 		   		 		  
        """
        self.s = s
        argmax = np.argmax(self.qtable[s])
        if rand.random() < self.rar:
            action = rand.randint(0, self.num_actions-1)
        else:
            action = argmax
        self.a = action
        if self.verbose: print "s =", s,"a =",action  		   	  			    		  		  		    	 		 		   		 		  
        return action
  		   	  			    		  		  		    	 		 		   		 		  
    def query(self,s_prime,r):  		   	  			    		  		  		    	 		 		   		 		  
        """  		   	  			    		  		  		    	 		 		   		 		  
        @summary: Update the Q table and return an action  		   	  			    		  		  		    	 		 		   		 		  
        @param s_prime: The new state  		   	  			    		  		  		    	 		 		   		 		  
        @param r: The ne state  		   	  			    		  		  		    	 		 		   		 		  
        @returns: The selected action = next action to take	   	  			    		  		  		    	 		 		   		 		  
        """
        prev_reward = self.qtable[self.s, self.a]
        argmax = np.argmax(self.qtable[s_prime])
        #update qtable of the state s and the action a
        self.qtable[self.s, self.a] = (1-self.alpha)*prev_reward + (self.gamma*self.qtable[s_prime, argmax]+r)*self.alpha

        # if self.dyna>0:
        #     self.T_c[self.s,self.a,s_prime] +=1
        #     sumsa = np.sum(self.T_c[self.s,self.a])
        #     self.T[self.s,self.a,:]= self.T_c[self.s,self.a,:]/sumsa
        #     self.R[self.s, self.a] = (1-self.alpha)*(self.R[self.s, self.a])+self.alpha*r
        #     for i in range(self.dyna):
        #         s_dyna=rand.randint(0,self.num_states-1)
        #         a_dyna=rand.randint(0,self.num_actions-1)
        #         prob = rand.random()
        #         sa_ac = np.add.accumulate(self.T[s_dyna,a_dyna])
        #         cond = prob < self.T[s_dyna, a_dyna] and np.roll(self.T[s_dyna,a_dyna])< prob)
        #         s_prime_dyna=np.argwhere()
        #


        # choose the new action for the state s_prime
        self.s = s_prime
        if rand.random() < self.rar :
            self.a = rand.randint(0, self.num_actions-1)
        else:
            self.a = argmax
        #update radr
        self.rar *= self.radr

        action = self.a
        if self.verbose: print "s =", s_prime,"a =",action,"r =",r,' rar = ',self.rar
        return action


    def author(self):
        return 'hku35'  # replace tb34 with your Georgia Tech username
  		   	  			    		  		  		    	 		 		   		 		  
if __name__=="__main__":  		   	  			    		  		  		    	 		 		   		 		  
    print "Remember Q from Star Trek? Well, this isn't him"  		   	  			    		  		  		    	 		 		   		 		  
