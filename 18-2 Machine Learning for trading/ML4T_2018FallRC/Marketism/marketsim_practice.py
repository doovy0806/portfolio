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

        if day == orders_df.index[-1]:
            daily_rets = (rv/rv.shift(1))-1
            daily_rets.ix[0] = 0
            sr= 252**(1/2.0) * (daily_rets.mean()/  daily_rets.std())

            daily_rets_spx = (spxvals/spxvals.shift(1))-1
            daily_rets_spx.ix[0] = 0
            sr_spx = 252**(1/2.0) * (daily_rets_spx.mean()/  daily_rets_spx.std())


            print "Data Rage:", str(start_date) , "to", str(end_date)
            print "Sharpe Ratio of Fund:", sr
            print "Sharpe Ratio of $SPX:", sr_spx
            print "Cumulative Return of Fund:", rv.ix[-1]/rv.ix[0]-1
            print "Cumulative Return of $SPX:", spxvals.ix[-1] / spxvals.ix[0] - 1
            print "Standard Deviation of Fund:", rv.std()
            print "Standard Deviation of $SPX:", spxvals.std()
            print "Average Daily Return of Fund:", daily_rets.mean()
            print "Average Daily Return of $SPX:", daily_rets_spx.mean()
            print "Final Portfolio Value :", rv.ix[-1]





    rv.to_csv("portvals.csv")

compute_portvals(orders_file="./orders/orders2.csv",)
# compute_portvals()

