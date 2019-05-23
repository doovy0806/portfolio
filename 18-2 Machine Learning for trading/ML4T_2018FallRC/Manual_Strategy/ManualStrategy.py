import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt
import os
from util import get_data, plot_data
import marketsimcode as msc
import indicators as indi

def testPolicy(symbol="JPM", sd=dt.datetime(2008, 1,1), ed=dt.datetime(2009, 12, 31), sv=100000):
    stockvals = get_data([symbol], pd.date_range(sd, ed))
    sma = indi.sma(stockvals)
    bb = indi.bollingerbands(stockvals)

    order_sma = sma.copy()
    order_sma[:] = 0
    order_bb = bb.copy()
    order_bb[:] = 0
    order = bb.copy()



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
        #
        # for day in stockvals.index:
        #     if pd.isnull(bb.ix[day, symbol]) or pd.isnull(smad.ix[day, symbol]) or pd.isnull(sma.ix[day, symbol]):
        #         order.ix[day] = 0
        #     elif iffirst and smad[day] >= 0:
        #         increasing = True
        #         iffirst = False
        #     elif iffirst and smad[day] < 0:
        #         increasing = False
        #         iffirst = False
        #     elif smad[day] < 0 and increasing:
        #         increasing = False
        #         # order_smad[day] = -1000- port_smad
        #         # port_smad = -1000
        #         order_smad[day] = 1000 - port_smad
        #         port_smad = 1000
        #     elif smad[day] >= 0 and not increasing:
        #         increasing = True
        #         # order_smad[day] = 1000 - port_smad
        #         # port_smad = 1000
        #         order_smad[day] = -1000 - port_smad
        #         port_smad = -1000
        #     else:
        #         order_smad[day] = 0
    smad_portfolio = msc.compute_portvals(order_smad, start_val = sv)


    return order_smad


trade = testPolicy()


