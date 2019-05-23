import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt
import os
from util import get_data, plot_data
import marketsimcode as msc
import indicators as indi

def bestPolicy(symbol="JPM", sd=dt.datetime(2008, 1,1), ed=dt.datetime(2009, 12, 31), sv=100000):
    stockvals = get_data([symbol], pd.date_range(sd, ed))
    sma = indi.sma(stockvals)
    bb = indi.bollingerbands(stockvals)

    order_sma = sma.copy()
    order_sma[:] = 0
    order_bb = bb.copy()
    order_bb[:] = 0



    cash_sma = sv
    port_sma = 0

    abovesma=False
    iffirst=True
    for day in stockvals.index:
        if pd.isnull(sma.ix[day, symbol]):
            order_sma.ix[day] = 0
        else:
            if iffirst:
                if sma.ix[day, symbol] > 0:
                    abovesma=True
                else :
                    abovesma = False
                iffirst=False
            else:
                if abovesma and sma.ix[day, symbol] < 0:
                    order_sma.ix[day] = 1000 - port_sma
                    port_sma = 1000
                    # order_sma.ix[day] = -1000 - port_sma
                    # port_sma = -1000
                    abovesma = False
                elif not abovesma and sma.ix[day, symbol] >0:
                    order_sma.ix[day] = -1000 - port_sma
                    port_sma = -1000
                    # order_sma.ix[day] = 1000 - port_sma
                    # port_sma= 1000
                    abovesma = True
                else:
                    order_sma.ix[day] = 0
    sma_portfolio = msc.compute_portvals(order_sma, start_val=sv)
    print sma_portfolio
    sma.plot()
    plt.show()
    # print order_sma
    cash_bb = sv
    port_bb = 0
    iffirst = True
    for day in stockvals.index:
        if pd.isnull(bb.ix[day, symbol]):
            order_bb.ix[day] = 0
        elif bb.ix[day, symbol] >= 1:
            order_bb.ix[day] = -1000 - port_bb
            port_bb = -1000
        elif bb.ix[day, symbol] <= -1:
            order_bb.ix[day] = 1000 - port_bb
            port_bb = 1000
        else:
            order_bb.ix[day] = 0
    bb_portfolio = msc.compute_portvals(order_bb, start_val=sv)

    cash_smad = sv
    port_smad = 0
    iffirst = True

    smad = indi.smadiff(stockvals)
    order_smad = smad.copy()
    order_smad[:] = 0
    increasing = False


    for day in stockvals.index:
        if pd.isnull(bb.ix[day,symbol]):
            order_bb.ix[day] =0
        elif iffirst and smad[day]>=0:
            increasing=True
            iffirst = False
        elif iffirst and smad[day]<0:
            increasing=False
            iffirst = False
        elif smad[day] < 0 and increasing:
            increasing=False
            # order_smad[day] = -1000- port_smad
            # port_smad = -1000
            order_smad[day] = 1000 - port_smad
            port_smad = 1000
        elif smad[day] >=0 and not increasing:
            increasing = True
            # order_smad[day] = 1000 - port_smad
            # port_smad = 1000
            order_smad[day] = -1000 - port_smad
            port_smad = -1000
        else:
            order_smad[day] = 0
    smad_portfolio = msc.compute_portvals(order_smad, start_val = sv)

    # macd = indi.macd(stockvals)
    # order_macd = macd.copy()
    # order_macd[:] = 0
    # increasing = False
    # port_macd=0
    # iffirst = True
    #
    # for day in stockvals.index:
    #     if pd.isnull(macd.ix[day, symbol]):
    #         order_macd.ix[day] = 0
    #     elif iffirst and macd[day] >= 0:
    #         increasing = True
    #         iffirst = False
    #     elif iffirst and macd[day] < 0:
    #         increasing = False
    #         iffirst = False
    #     elif macd[day] < 0 and increasing:
    #         increasing = False
    #         # order_macd[day] = -1000 - port_macd
    #         # port_macd = -1000
    #         order_macd[day] = 1000 - port_macd
    #         port_macd = 1000
    #     elif macd[day] >= 0 and not increasing:
    #         increasing = True
    #         # order_macd[day] = 1000 - port_macd
    #         # port_macd = 1000
    #         order_macd[day] = -1000 - port_macd
    #         port_macd = -1000
    #     else:
    #         order_macd[day] = 0
    # macd_portfolio = msc.compute_portvals(order_macd, start_val=sv)


    # print bb_portfolio
    # # print smad_portfolio
    # # smad.plot()
    # # plt.show()
    # print macd_portfolio
    print sma_portfolio
    return order_smad


order = bestPolicy(sd= dt.datetime(2010,1,1), ed=dt.datetime(2011,12,31))
benchmark = order.copy()
benchmark.ix[0] = 1000
benchmark.ix[1:] = 0
port = msc.compute_portvals(order, commission=0, impact=0)
benchport = msc.compute_portvals(benchmark, commission=0, impact=0)
port = port/port.ix[0]
benchport = benchport/benchport.ix[0]
port_daily = port/port.shift(1) -1
benchport_daily = benchport/benchport.shift(1) -1
long = order>0
short = order<0

print "cumulative returns, optimal :", float(port.ix[-1]-1), " benchmark: ", float(benchport.ix[-1])
print "standard dev of daily ret, optimal : ", float(port_daily.std()) , "  benchmark : " , float( benchport_daily.std())
print "mean of daily ret, optimal : " ,  float(port_daily.mean()) , "  benchmark : " ,float( benchport_daily.mean())

df_temp = pd.concat([port, benchport], keys=['Optimal', 'Benchmark'], axis=1)
# ax = df_temp.plot(title="normalized portfolio values of optimal strategy and benchmark", grid=True, color='c')
# ax.plot()
plt.plot(port.index, port, color='black')
plt.plot(port.index, benchport, color='blue')
plt.plot(port.index, long, color='green')
plt.plot(port.index, short, color = 'red')
plt.show()
plt.savefig('benchmark_vs_optimal.png')