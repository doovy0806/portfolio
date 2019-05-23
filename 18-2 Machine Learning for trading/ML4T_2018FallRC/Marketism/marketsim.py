"""MC2-P1: Market simulator.  		   	  			    		  		  		    	 		 		   		 		  
  		   	  			    		  		  		    	 		 		   		 		  
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
  		   	  			    		  		  		    	 		 		   		 		  
Student Name: Tucker Balch (replace with your name)  		   	  			    		  		  		    	 		 		   		 		  
GT User ID: hku35 (replace with your User ID)
GT ID: 903456821 (replace with your GT ID)
"""  		   	  			    		  		  		    	 		 		   		 		  
import pandas as pd
import numpy as np
import datetime as dt
import os
from util import get_data, plot_data


def compute_portvals(orders_file="./orders/orders.csv", start_val=1000000, commission=9.95, impact=0.005):
    # this is the function the autograder will call to test your code
    # NOTE: orders_file may be a string, or it may be a file object. Your
    # code should work correctly with either input
    # TODO: Your code here

    # In the template, instead of computing the value of the portfolio, we just
    # read in the value of IBM over 6 months
    orders_df = pd.read_csv(orders_file, index_col='Date', parse_dates=True, na_values=['nan'])
    orders_df = orders_df.sort_index(level='Date')

    #start_date = dt.datetime(2011, 1, 1)
    #end_date = dt.datetime(2011, 12, 31)
    start_date = orders_df.index[0]
    end_date = orders_df.index[-1]
    stockvals = get_data(['$SPX'], pd.date_range(start_date, end_date))
    stockvals = stockvals[['$SPX']]  # remove SPY
    spxvals = get_data(['$SPX'], pd.date_range(start_date, end_date))
    spxvals = stockvals[['$SPX']]  # remove SPY
    porvals = get_data(['$SPX'], pd.date_range(start_date, end_date))
    porvals = stockvals[['$SPX']]  # remove SPY

    rv = pd.DataFrame(index=porvals.index, data=porvals.as_matrix())

    cash_amount = start_val
    stock_index = {'$SPX': 1}
    symbols = ['$SPX']
    portfolio = [cash_amount, 0]
    value = cash_amount

    order_num = 0
    order_date = orders_df.index[order_num]
    for day in rv.index:  # stockvals should be modified
        while order_date == day:
            symbol = orders_df.ix[order_num, 'Symbol']
            order = orders_df.ix[order_num, 'Order']
            shares = orders_df.ix[order_num, 'Shares']
            if not (symbol in stock_index):
                symbols.append(symbol)
                stock = get_data([symbol], pd.date_range(start_date, end_date))
                stock = stock[[symbol]]
                stockvals = stockvals.join(stock)
                stock_index[symbol] = len(portfolio)
                portfolio.append(0)


            price = stockvals.ix[day, symbol]

            if order == 'BUY':
                total_cost = (price*(1+impact)) * shares
                # substract from cash
                portfolio[0] -= total_cost
                # add to portfolio
                portfolio[stock_index[symbol]] += shares
                portfolio[0] -= commission

            elif order == 'SELL':
                total_amount = price*(1-impact) * shares
                # substract from portfolio
                portfolio[stock_index[symbol]] -= shares
                portfolio[0] += total_amount
                portfolio[0] -= commission
            order_num+=1
            if not order_date == orders_df.index[-1]:
                order_date = orders_df.index[order_num]
            else:
                break


        date_amount = portfolio[0]
        for i in symbols:
            symbolprice = stockvals.ix[day, i]
            date_amount += symbolprice * portfolio[stock_index[i]]
        rv.ix[day] = date_amount

        # if day == orders_df.index[-1]:
        #     daily_rets = (rv/rv.shift(1))-1
        #     daily_rets.ix[0] = 0
        #     sr= 252**(1/2.0) * (daily_rets.mean()/  daily_rets.std())
        #
        #     daily_rets_spx = (spxvals/spxvals.shift(1))-1
        #     daily_rets_spx.ix[0] = 0
        #     sr_spx = 252**(1/2.0) * (daily_rets_spx.mean()/  daily_rets_spx.std())



    return rv
    rv.to_csv("portvals.csv")

def author():
        return 'hku35' # replace tb34 with your Georgia Tech username.


def test_code():  		   	  			    		  		  		    	 		 		   		 		  
    # this is a helper function you can use to test your code  		   	  			    		  		  		    	 		 		   		 		  
    # note that during autograding his function will not be called.  		   	  			    		  		  		    	 		 		   		 		  
    # Define input parameters  		   	  			    		  		  		    	 		 		   		 		  
  		   	  			    		  		  		    	 		 		   		 		  
    of = "./orders/orders2.csv"  		   	  			    		  		  		    	 		 		   		 		  
    sv = 1000000  		   	  			    		  		  		    	 		 		   		 		  
  		   	  			    		  		  		    	 		 		   		 		  
    # Process orders  		   	  			    		  		  		    	 		 		   		 		  
    portvals = compute_portvals(orders_file = of, start_val = sv)  		   	  			    		  		  		    	 		 		   		 		  
    if isinstance(portvals, pd.DataFrame):  		   	  			    		  		  		    	 		 		   		 		  
        portvals = portvals[portvals.columns[0]] # just get the first column  		   	  			    		  		  		    	 		 		   		 		  
    else:  		   	  			    		  		  		    	 		 		   		 		  
        "warning, code did not return a DataFrame"  		   	  			    		  		  		    	 		 		   		 		  
  		   	  			    		  		  		    	 		 		   		 		  
    # Get portfolio stats  		   	  			    		  		  		    	 		 		   		 		  
    # Here we just fake the data. you should use your code from previous assignments.  		   	  			    		  		  		    	 		 		   		 		  
    start_date = dt.datetime(2008,1,1)  		   	  			    		  		  		    	 		 		   		 		  
    end_date = dt.datetime(2008,6,1)  		   	  			    		  		  		    	 		 		   		 		  
    cum_ret, avg_daily_ret, std_daily_ret, sharpe_ratio = [0.2,0.01,0.02,1.5]  		   	  			    		  		  		    	 		 		   		 		  
    cum_ret_SPY, avg_daily_ret_SPY, std_daily_ret_SPY, sharpe_ratio_SPY = [0.2,0.01,0.02,1.5]  		   	  			    		  		  		    	 		 		   		 		  
  		   	  			    		  		  		    	 		 		   		 		  
    # Compare portfolio against $SPX  		   	  			    		  		  		    	 		 		   		 		  
    print "Date Range: {} to {}".format(start_date, end_date)  		   	  			    		  		  		    	 		 		   		 		  
    print  		   	  			    		  		  		    	 		 		   		 		  
    print "Sharpe Ratio of Fund: {}".format(sharpe_ratio)  		   	  			    		  		  		    	 		 		   		 		  
    print "Sharpe Ratio of SPY : {}".format(sharpe_ratio_SPY)  		   	  			    		  		  		    	 		 		   		 		  
    print  		   	  			    		  		  		    	 		 		   		 		  
    print "Cumulative Return of Fund: {}".format(cum_ret)  		   	  			    		  		  		    	 		 		   		 		  
    print "Cumulative Return of SPY : {}".format(cum_ret_SPY)  		   	  			    		  		  		    	 		 		   		 		  
    print  		   	  			    		  		  		    	 		 		   		 		  
    print "Standard Deviation of Fund: {}".format(std_daily_ret)  		   	  			    		  		  		    	 		 		   		 		  
    print "Standard Deviation of SPY : {}".format(std_daily_ret_SPY)  		   	  			    		  		  		    	 		 		   		 		  
    print  		   	  			    		  		  		    	 		 		   		 		  
    print "Average Daily Return of Fund: {}".format(avg_daily_ret)  		   	  			    		  		  		    	 		 		   		 		  
    print "Average Daily Return of SPY : {}".format(avg_daily_ret_SPY)  		   	  			    		  		  		    	 		 		   		 		  
    print  		   	  			    		  		  		    	 		 		   		 		  
    print "Final Portfolio Value: {}".format(portvals[-1])  		   	  			    		  		  		    	 		 		   		 		  
  		   	  			    		  		  		    	 		 		   		 		  
if __name__ == "__main__":  		   	  			    		  		  		    	 		 		   		 		  
    test_code()  		   	  			    		  		  		    	 		 		   		 		  
