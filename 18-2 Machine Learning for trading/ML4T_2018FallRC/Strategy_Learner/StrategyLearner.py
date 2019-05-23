"""  		   	  			    		  		  		    	 		 		   		 		  
Template for implementing StrategyLearner  (c) 2016 Tucker Balch  		   	  			    		  		  		    	 		 		   		 		  
  		   	  			    		  		  		    	 		 		   		 		  
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
  		   	  			    		  		  		    	 		 		   		 		  
import datetime as dt  		   	  			    		  		  		    	 		 		   		 		  
import pandas as pd
import numpy as np
import util as ut
import QLearner as ql
import RTLearner as rt
import random
from indicators import *
from marketsimcode import *
import BagLearner as bl
  		   	  			    		  		  		    	 		 		   		 		  
class StrategyLearner(object):  		   	  			    		  		  		    	 		 		   		 		  
  		   	  			    		  		  		    	 		 		   		 		  
    # constructor  		   	  			    		  		  		    	 		 		   		 		  
    def __init__(self, verbose = False, impact=0.0):  		   	  			    		  		  		    	 		 		   		 		  
        self.verbose = verbose  		   	  			    		  		  		    	 		 		   		 		  
        self.impact = impact
        self.ybuy  = 0.008
        self.ysell = -0.008
  		   	  			    		  		  		    	 		 		   		 		  
    # this method should create a QLearner, and train it for trading  		   	  			    		  		  		    	 		 		   		 		  
    def addEvidence(self, symbol = "JPM", sd=dt.datetime(2008,1,1), ed=dt.datetime(2010,1,1),   sv = 10000):
  		   	  			    		  		  		    	 		 		   		 		  
        # add your code to do learning here
        syms=[symbol]
        dates = pd.date_range(sd, ed)
        prices_all = ut.get_data(syms, dates)  # automatically adds SPY
        prices = prices_all[syms]  # only portfolio symbols
        prices_SPY = prices_all['SPY']  # only SPY, for comparison later
        if self.verbose: print prices

        # ndayrets = prices.copy()
        # ndayrets = (ndayrets / ndayrets.shift(1)) - 1
        # ndayrets.ix[0, :] = 0
        # ndayrets.plot(title="ndayrets")

        normed = prices / prices.iloc[0]
        # normed.plot(title="normed")

        # self.rtl = rt.RTLearner(leaf_size=5)
        self.baglearner = bl.BagLearner(learner=rt.RTLearner, kwargs={"leaf_size":5}, bags=50)

        ret = prices.copy()

        ret_10 = (ret.shift(-10)/ret)-1

        ret_10.dropna()
        impactret_10 = (ret.shift(-10) * (1 - (float(self.impact) / 10000)))/ret -1
        impactret_10.dropna()
        ret = prices.copy()
        ret_20 = (ret.shift(-20)/ret)-1
        ret_20.dropna()
        ret_30 = ( ret.shift(-30)/ret) - 1
        ret_30.dropna()
        ret_5 = (ret.shift(-5)/ret) - 1
        ret_5.dropna()

        threshold = prices.copy()
        threshold.ix[:] = 0
        # bool1 = ret_20.values>0.05
        # impactret_10 = ret_10.values*(1-(float(self.impact)/10000))
        bool1 = impactret_10.values > self.ybuy
        bool2 = impactret_10.values < self.ysell
        # bool1 = ret_10.values[:]*self.mulimpact > self.ybuy
        # bool2 = ret_10.values[:]*self.mulimpact < self.ysell
        npthres=threshold.values
        npthres[bool1] = 1
        npthres[bool2] = -1
        threshold.ix[:]=npthres[:]





        # threshold.loc[ret_20.values<-0.05,[symbol]]=-1

        bbIndi = bollingerbands(normed, symbol=symbol)
        smadIndi = smadiff(normed, symbol=symbol)
        smaIndi = sma(normed, symbol=symbol)
        Xdata = bbIndi.join([smaIndi,smadIndi, normed], how='inner')
        Xdata = Xdata[19:]
        threshold = threshold[19:]
        ndXdata = Xdata.values
        ndthreshold=threshold.values


        self.baglearner.addEvidence(dataX=ndXdata, dataY=ndthreshold)






        # example use with new colname
        volume_all = ut.get_data(syms, dates, colname = "Volume")  # automatically adds SPY  		   	  			    		  		  		    	 		 		   		 		  
        volume = volume_all[syms]  # only portfolio symbols  		   	  			    		  		  		    	 		 		   		 		  
        volume_SPY = volume_all['SPY']  # only SPY, for comparison later  		   	  			    		  		  		    	 		 		   		 		  
        if self.verbose: print volume  		   	  			    		  		  		    	 		 		   		 		  
  		   	  			    		  		  		    	 		 		   		 		  
    # this method should use the existing policy and test it against new data  		   	  			    		  		  		    	 		 		   		 		  
    def testPolicy(self, symbol = "JPM", \
        sd=dt.datetime(2010,1,1), \
        ed=dt.datetime(2012,1,1), \
        sv = 10000):  		   	  			    		  		  		    	 		 		   		 		  
  		   	  			    		  		  		    	 		 		   		 		  
        # here we build a fake set of trades  		   	  			    		  		  		    	 		 		   		 		  
        # your code should return the same sort of data  		   	  			    		  		  		    	 		 		   		 		  
        dates = pd.date_range(sd, ed)  		   	  			    		  		  		    	 		 		   		 		  
        prices_all = ut.get_data([symbol], dates)  # automatically adds SPY  		   	  			    		  		  		    	 		 		   		 		  
        prices = prices_all[[symbol]]  # only portfolio symbols
        trades_SPY = prices_all['SPY']  # only SPY, for comparison later
        normed = prices/prices.ix[0]

        bbIndi = bollingerbands(prices, symbol=symbol)
        smadIndi = smadiff(prices, symbol=symbol)
        smaIndi = sma(prices, symbol=symbol)
        Xdata = bbIndi.join([smaIndi, smadIndi, normed], how='inner')
        Xdata = Xdata[19:]

        order = self.baglearner.query(Xdata.values)
        haveStock = False
        iffirst = True

        ndayrets = prices.copy()
        ndayrets = (ndayrets / ndayrets.shift(-10)) - 1
        ndayrets.ix[-10:, :] = 0
        ndayrets.plot(title="ndayrets")
        ndayrets.ix[:,:] = ndayrets.ix[:,:]


        

        trades = prices.copy()
        trades[:]=0
        if self.verbose:
            ret = prices.copy()

            ret_10 = (ret.shift(-10) / ret) - 1
            ret_10.dropna()
            ret_20 = (ret.shift(-20) / ret) - 1
            ret_20.dropna()
            ret_30 = (ret.shift(-30) / ret) - 1
            ret_30.dropna()
            ret_5 = (ret.shift(-5) / ret) - 1
            ret_5.dropna()

            threshold = prices.copy()
            threshold.ix[:] = 0
            # bool1 = ret_20.values>0.05
            impactret_10 = ret_10.values * (1 - (float(self.impact) / 10000))
            impactret_10 = (ret.shift(-10) * (1 - (float(self.impact) / 10000))) / ret - 1
            impactret_10.dropna()
            bool1 = impactret_10.values> self.ybuy
            bool2 = impactret_10.values < self.ysell
            normed = prices/prices.ix[0]-1
            npthres = threshold.values
            npthres[bool1] = 1
            npthres[bool2] = -1
            threshold.ix[:] = npthres[:]
            orderpd = pd.DataFrame(data = order.transpose(), index=threshold.index[19:])
            # threshold.join(orderpd, how='inner')
            df_temp = pd.concat([threshold, orderpd, ndayrets*10, normed], keys=['threshold', 'order', '10day_return*10', 'normalized'],
                                axis=1)
            ax = df_temp.plot(title="JPM-in sample strategy learner", grid=True, fontsize=10)
            ax.set_xlabel("date")
            ax.set_ylabel("order")
            # plt.plot(threshold.index, orderpd, threshold.index, threshold)
            plt.show()

        for i in range(len(order[0])):
            if order[0,i]>0.5 and iffirst:
                trades.ix[i+19, symbol] = 1000
                iffirst = False
                haveStock = True
            elif order[0,i]<-0.5 and iffirst:
                trades.ix[i+19, symbol] = -1000
                iffirst = False
                haveStock = False
            elif order[0,i]>0.5 and not haveStock:
                trades.ix[i+19,symbol] = 2000
                haveStock = True
            elif order[0,i]<-0.5 and haveStock:
                trades.ix[i+19, symbol] =-2000
                haveStock = False
            else :
                trades.ix[i+19, symbol] = 0




        if self.verbose: print type(trades) # it better be a DataFrame!  		   	  			    		  		  		    	 		 		   		 		  
        if self.verbose: print trades  		   	  			    		  		  		    	 		 		   		 		  
        if self.verbose: print prices_all  		   	  			    		  		  		    	 		 		   		 		  
        return trades

    def author(self):
        return 'hku35'  # replace tb34 with your Georgia Tech username
  		   	  			    		  		  		    	 		 		   		 		  
if __name__=="__main__":  		   	  			    		  		  		    	 		 		   		 		  
    print "One does not simply think up a strategy"  		   	  			    		  		  		    	 		 		   		 		  
    sl = StrategyLearner(verbose=True)
    sl.addEvidence(symbol='AAPL')
    trades = sl.testPolicy(symbol='AAPL')
    print trades
    rv = compute_portvals(trades, symbol='AAPL')
    print rv