import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt
import os
from util import get_data, plot_data
import marketsimcode as msc


#benchmark and the JPM result


def testPolicy(symbol = "JPM", sd=dt.datetime(2008,1,1), ed=dt.datetime(2009,12,31), sv=100000):
    stockvals = get_data([symbol], pd.date_range(sd, ed))
    stockvals = stockvals[[symbol]]
    start_date = sd
    end_date = ed

    # orders = pd.DataFrame(index=stockvals.index, data=stockvals.as_matrix())
    # portvals = pd.DataFrame(index=stockvals.index, data=stockvals.as_matrix())
    # sharesdf = pd.DataFrame(index=stockvals.index, data=stockvals.as_matrix())
    orders = get_data([symbol], pd.date_range(sd, ed))
    orders = stockvals[[symbol]]
    portvals = get_data([symbol], pd.date_range(sd, ed))
    portvals = stockvals[[symbol]]
    sharesdf = get_data([symbol], pd.date_range(sd, ed))
    sharesdf = stockvals[[symbol]]

    ordernum = 0
    rising = False
    cash = sv
    shares = 0


    for day in stockvals.index[:-1]:
        todayprice = stockvals.ix[ordernum, symbol]
        tomorrowprice = stockvals.ix[ordernum+1, symbol]

        if ordernum==0:
            if todayprice < tomorrowprice:
                stockprice = stockvals.ix[ordernum, symbol]
                buymoney = stockprice * shares
                order = 1000
                orders.ix[day] = order
                shares = 1000
                sharesdf[day]=shares
                cash = cash - buymoney
                portvals.ix[day] = cash + shares * (stockprice)
                rising = True
            else:
                stockprice = stockvals.ix[ordernum, symbol]
                orders.ix[day] = - 1000
                shares = -1000
                sharesdf[day] = shares
                sellmoney = stockprice * shares
                cash -=sellmoney
                portvals.ix[day] = cash + shares * (stockprice)
                rising=False

        elif todayprice < tomorrowprice: #if the price goes up tomorrow
            if rising:
                orders.ix[day] = 0
                sharesdf[day] = shares
                portvals.ix[day] = cash + shares*stockvals.ix[ordernum]
            else:
                stockprice = stockvals.ix[ordernum, symbol]

                orders.ix[day] = -shares + 1000
                shares = 1000
                sharesdf[day] = shares
                cash = cash - orders.ix[day] * stockprice
                portvals.ix[day] = cash + (shares*(stockprice))
            rising = True
        else :
            if rising:
                stockprice = stockvals.ix[ordernum, symbol]
                sellmoney = stockprice * shares
                orders.ix[day] = -(shares) - 1000
                order = -(shares) - 1000
                shares = -1000
                sharesdf[day] = shares
                cash -= order * stockprice
                portvals.ix[day] = cash + (shares * stockprice)
            else:
                orders.ix[day] = 0
                portvals.ix[day] = cash + (shares * stockvals.ix[ordernum])
                sharesdf[day] = shares
            rising = False
        ordernum += 1

    orders.ix[ordernum] = 0
    portvals.ix[ordernum] = cash+abs(shares*stockvals.ix[ordernum])
    sharesdf[ordernum] = shares
    # print sharesdf
    # print portvals
    # print orders
    return orders


# order = bestPolicy()
# benchmark = order.copy()
# benchmark.ix[0] = 1000
# benchmark.ix[1:] = 0
# port = msc.compute_portvals(order, commission=0, impact=0)
# benchport = msc.compute_portvals(benchmark, commission=0, impact=0)
# port = port/port.ix[0]
# benchport = benchport/benchport.ix[0]
# port_daily = port/port.shift(1) -1
# benchport_daily = benchport/benchport.shift(1) -1
#
# print "cumulative returns, optimal :", float(port.ix[-1]-1), " benchmark: ", float(benchport.ix[-1])
# print "standard dev, optimal : ", float(port_daily.std()) , "  benchmark : " , float( benchport_daily.std())
# print "mean dev, optimal : " ,  float(port_daily.mean()) , "  benchmark : " ,float( benchport_daily.mean())
#
# df_temp = pd.concat([port, benchport], keys=['Optimal', 'Benchmark'], axis=1)
# # ax = df_temp.plot(title="normalized portfolio values of optimal strategy and benchmark", grid=True, color='c')
# # ax.plot()
# plt.plot(port.index, port, color='black')
# plt.plot(port.index, benchport, color='blue')
# plt.show()
# plt.savefig('benchmark_vs_optimal.png')