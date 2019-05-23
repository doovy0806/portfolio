"""MC1-P2: Optimize a portfolio.  		   	  			    		  		  		    	 		 		   		 		  
  		   	  			    		  		  		    	 		 		   		 		  
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
  		   	  			    		  		  		    	 		 		   		 		  
  		   	  			    		  		  		    	 		 		   		 		  
import pandas as pd
import matplotlib as plt
import numpy as np
import datetime as dt  		   	  			    		  		  		    	 		 		   		 		  
from util import get_data
import scipy.optimize as spo
  		   	  			    		  		  		    	 		 		   		 		  
# This is the function that will be tested by the autograder  		   	  			    		  		  		    	 		 		   		 		  
# The student must update this code to properly implement the functionality  		   	  			    		  		  		    	 		 		   		 		  
def optimize_portfolio(sd=dt.datetime(2008, 1, 1), ed=dt.datetime(2009, 1, 1), \
                       syms=['GOOG', 'AAPL', 'GLD', 'XOM'], gen_plot=False):
    # Read in adjusted closing prices for given symbols, date range
    pd.set_option('chained_assignment', None)
    dates = pd.date_range(sd, ed)
    prices_all = get_data(syms, dates)  # automatically adds SPY
    prices = prices_all[syms]  # only portfolio symbols
    prices_SPY = prices_all['SPY']  # only SPY, for comparison later

    # here starts my code
    prices_all.fillna(method="ffill", inplace=True)
    prices_all.fillna(method="bfill", inplace=True)
    prices.fillna(method="ffill", inplace=True)
    prices.fillna(method="bfill", inplace=True)

    # find the allocations for the optimal portfolio
    # note that the values here ARE NOT meant to be correct for a test case
    syms_length = len(syms)

    allocs = np.ones(syms_length)
    allocs = allocs / float(syms_length)  # add code here to find the allocations
    allocsGuess = allocs.copy()

    cons = {'type': 'eq', 'fun': con}

    '''calculate the total Sharpe Ratio'''
    bounds = get_bounds(syms_length)
    result = spo.minimize(error_function, allocsGuess, args=(prices,), method='SLSQP', \
                          bounds=bounds, constraints=cons, options={'disp': True})

    allocs = result.x

    dr = get_dailyrets(allocs, prices)
    port_val = get_portval(allocs, prices)
    cr = (port_val[-1] / port_val[0]) - 1
    adr = dr.mean()
    sddr = dr.std()
    sr = get_sharperatio(allocs, prices)

    ''' now generate plots'''

    # Compare daily portfolio value with SPY using a normalized plot
    if gen_plot:
        # add code to plot here
        normSPY = (prices_SPY / prices_SPY.iloc[0])
        df_temp = pd.concat([port_val, normSPY], keys=['Portfolio', 'SPY'], axis=1)
        ax = df_temp.plot(title="Daily Portfolio Value and SPY", grid=True, fontsize=10)
        ax.set_xlabel("Date")
        ax.set_ylabel("Normalized Price")
        plt.savefig("chart.png")
        pass

    return allocs, cr, adr, sddr, sr


''' my code - functions'''


def get_dailyrets(allocs, prices):
    port_val = get_portval(allocs, prices)
    daily_rets = (port_val / port_val.shift(1)) - 1
    daily_rets.ix[0] = 0
    '''be careful - port_vals has only one column.'''
    return daily_rets


# mycode -function that returns cumulative returns
def get_portval(allocs, prices):
    start_val = 1
    normed = prices / prices.iloc[0]
    alloced = normed * allocs
    pos_vals = alloced * start_val
    port_val = pos_vals.sum(axis=1)
    return port_val


def get_sharperatio(allocs, prices):
    daily_rets = get_dailyrets(allocs, prices)
    sr = 252 ** (1 / 2.0) * daily_rets.mean() / daily_rets.std()
    return sr


def error_function(allocs, prices):
    sr = get_sharperatio(allocs, prices)
    return sr * (-1)


def con(allocs):
    return allocs.sum() - 1


def get_bounds(syms_length):
    bounds = []
    for i in range(syms_length):
        bounds.append((0, 1))
    return bounds


'''my code ends here'''


def test_code():
    # This function WILL NOT be called by the auto grader  		   	  			    		  		  		    	 		 		   		 		  
    # Do not assume that any variables defined here are available to your function/code  		   	  			    		  		  		    	 		 		   		 		  
    # It is only here to help you set up and test your code  		   	  			    		  		  		    	 		 		   		 		  
  		   	  			    		  		  		    	 		 		   		 		  
    # Define input parameters  		   	  			    		  		  		    	 		 		   		 		  
    # Note that ALL of these values will be set to different values by  		   	  			    		  		  		    	 		 		   		 		  
    # the autograder!  		   	  			    		  		  		    	 		 		   		 		  
  		   	  			    		  		  		    	 		 		   		 		  
    start_date = dt.datetime(2009,1,1)  		   	  			    		  		  		    	 		 		   		 		  
    end_date = dt.datetime(2010,1,1)  		   	  			    		  		  		    	 		 		   		 		  
    symbols = ['GOOG', 'AAPL', 'GLD', 'XOM', 'IBM']  		   	  			    		  		  		    	 		 		   		 		  
  		   	  			    		  		  		    	 		 		   		 		  
    # Assess the portfolio  		   	  			    		  		  		    	 		 		   		 		  
    allocations, cr, adr, sddr, sr = optimize_portfolio(sd = start_date, ed = end_date,\
        syms = symbols, \
        gen_plot = False)  		   	  			    		  		  		    	 		 		   		 		  
  		   	  			    		  		  		    	 		 		   		 		  
    # Print statistics  		   	  			    		  		  		    	 		 		   		 		  
    print "Start Date:", start_date  		   	  			    		  		  		    	 		 		   		 		  
    print "End Date:", end_date  		   	  			    		  		  		    	 		 		   		 		  
    print "Symbols:", symbols  		   	  			    		  		  		    	 		 		   		 		  
    print "Allocations:", allocations  		   	  			    		  		  		    	 		 		   		 		  
    print "Sharpe Ratio:", sr  		   	  			    		  		  		    	 		 		   		 		  
    print "Volatility (stdev of daily returns):", sddr  		   	  			    		  		  		    	 		 		   		 		  
    print "Average Daily Return:", adr  		   	  			    		  		  		    	 		 		   		 		  
    print "Cumulative Return:", cr  		   	  			    		  		  		    	 		 		   		 		  
  		   	  			    		  		  		    	 		 		   		 		  
if __name__ == "__main__":  		   	  			    		  		  		    	 		 		   		 		  
    # This code WILL NOT be called by the auto grader  		   	  			    		  		  		    	 		 		   		 		  
    # Do not assume that it will be called  		   	  			    		  		  		    	 		 		   		 		  
    test_code()  		   	  			    		  		  		    	 		 		   		 		  
