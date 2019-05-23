import pandas as pd
import numpy as np
import datetime as dt
import os
import matplotlib.pyplot as plt
from util import get_data, plot_data


def compute_portvals(orders_df, start_val=1000000, commission=9.95, impact=0.005 ):
    # this is the function the autograder will call to test your code
    # NOTE: orders_file may be a string, or it may be a file object. Your
    # code should work correctly with either input
    # TODO: Your code here

    # In the template, instead of computing the value of the portfolio, we just
    # read in the value of IBM over 6 months


    #start_date = dt.datetime(2011, 1, 1)
    #end_date = dt.datetime(2011, 12, 31)
    start_date = orders_df.index[0]
    end_date = orders_df.index[-1]
    stockvals = get_data(['JPM'], pd.date_range(start_date, end_date))
    stockvals = stockvals[['JPM']]  # remove SPY
    spxvals = get_data(['JPM'], pd.date_range(start_date, end_date))
    spxvals = stockvals[['JPM']]  # remove SPY
    porvals = get_data(['JPM'], pd.date_range(start_date, end_date))
    porvals = stockvals[['JPM']]  # remove SPY

    rv = stockvals.copy()
    rv.ix[:] = 0

    cash_amount = start_val
    stock_index = {'JPM': 1}
    symbols = ['JPM']
    portfolio = [cash_amount, 0]

    value = cash_amount

    order_num = 0
    order_date = orders_df.index[order_num]
    for day in rv.index:
        order = orders_df.ix[day,'JPM']

        if order > 0:
            price = stockvals.ix[day]*(1+ impact)
            portfolio[1] += order
            portfolio[0] -= order*price + commission
        elif order<0 :
            price = stockvals.ix[day] * (1 - impact)
            portfolio[1] += order
            portfolio[0] -= order * price + commission
        rv.ix[day] = portfolio[0] + portfolio[1]*stockvals.ix[day]

        if day == orders_df.index[-1]:
            daily_rets = (rv/rv.shift(1))-1
            daily_rets.ix[0] = 0
            sr= 252**(1/2.0) * (daily_rets.mean()/  daily_rets.std())

            # print "Data Rage:"+ str(start_date) + "to"+ str(end_date)
            # print "Sharpe Ratio of Fund:", float(sr)
            # print "Cumulative Return of Fund:", float(rv.ix[-1]/rv.ix[0]-1)
            # print "Standard Deviation of Fund:", float(rv.std())
            # print "Average Daily Return of Fund:", float(daily_rets.mean())
            # print "Final Portfolio Value :", float(rv.ix[-1])
    return rv




# compute_portvals()

