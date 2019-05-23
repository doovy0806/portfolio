#should generate charts that illustrate the indicators in the report.
'''
gt id : 903456821
account : hku35
name : Ku, Han Mo
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt
import os
from util import get_data, plot_data


def bollingerbands(pricedf, symbol='JPM'):
    # jpm_r : dataframe to calculate of JPM's rolling means
    # jpm_r = get_data(['JPM'], pd.date_range(sample_start, end_date))
    # jpm_r = jpm_r / jpm_r.ix[10]
    # jpm_rm = pd.rolling_mean(jpm_r['JPM'], window=10)
    # jpm_r = jpm_r.ix[10:, ['JPM']]
    # jpm_rm = jpm_rm.ix[10:]
    # jpm_rstd = pd.rolling_std(jpm_r['JPM'], window=10)
    # jpm_bbup = jpm_rm + (2 * jpm_rstd)
    # jpm_bbdown = jpm_rm - (2 * jpm_rstd)
    # bb_jpm = (jpmvals['JPM'] - jpm_rm) / (2 * jpm_rstd)
    normalizedprice = pricedf/pricedf.ix[0]
    jpm_rm = pd.rolling_mean(normalizedprice[symbol], window=10)
    jpm_rstd = pd.rolling_std(normalizedprice[symbol], window=10)
    jpm_bbup = jpm_rm+(2*jpm_rstd)
    jpm_bbdown = jpm_rm - (2*jpm_rstd)
    bb_jpm = (normalizedprice[symbol] - jpm_rm) / (2*jpm_rstd)
    bb_jpm=bb_jpm.to_frame(name='bb')
    return bb_jpm
    # plt.figure(1)
    # plt.plot(jpmvals.index, jpmvals, jpmvals.index, jpm_bbup, jpmvals.index, jpm_bbdown, jpmvals.index, bb_jpm)
    # plt.savefig("bollingerbands_jpm.png")
    # plt.figure(2)
    # plt.plot(bb_jpm.index, bb_jpm)
    # plt.show()
    # plt.savefig("bollingerbands.png")
    # print jpm_rm
def smadiff(pricedf, symbol='JPM'):
    normalizedprice = pricedf / pricedf.ix[0]
    jpm_rm = pd.rolling_mean(normalizedprice[symbol], window=10)
    jpm_rm20 = pd.rolling_mean(normalizedprice[symbol], window=20)
    jpmsma = normalizedprice[symbol]-jpm_rm
    jpmsma_diff = jpm_rm-jpm_rm20
    jpmsma_diff = jpmsma_diff.to_frame(name='smadiff')
    return jpmsma_diff

def sma(pricedf, symbol='JPM'):
    normalizedprice = pricedf / pricedf.ix[0]
    jpm_rm = pd.rolling_mean(normalizedprice[symbol], window=10)
    jpmsma = normalizedprice[symbol] - jpm_rm
    jpmsma= jpmsma.to_frame(name='sma')
    return jpmsma

# def macd(pricedf):
#     normalizedprice = pricedf / pricedf.ix[0]
#     jpm_rm = pd.rolling_mean(normalizedprice['JPM'], window=20)
#     jpmema = (normalizedprice['JPM'] - jpm_rm.shift(1))*2/float(20+1) + jpm_rm.shift(1)
#
#     iffirst = True
#     indexint = 0
#     for day in jpm_rm.index:
#         if not pd.isnull(jpm_rm[day]):
#             if iffirst:
#                 iffirst = False
#             else:
#                 jpmema[day] = (normalizedprice['JPM'] - jpmema[indexint-1])*2/float(20+1) + jpmema[indexint-1]
#         indexint+=1
#
#     jpmmacd = jpmema - jpm_rm
#     return jpmmacd




#
# start_date = dt.datetime(2011, 1, 1)
# end_date = dt.datetime(2011, 12, 31)
# start_date = dt.datetime(2008, 1, 1)
# sample_start = dt.datetime(2007, 12, 15)
# end_date = dt.datetime(2009, 12, 31)
# jpmvals = get_data(['JPM'], pd.date_range(start_date, end_date))
# jpmvals = jpmvals[['JPM']]  # remove SPY
# jpm_norm = jpmvals/jpmvals.ix[0]
# bb_jpm = bollingerbands(jpmvals)
# ax = bb_jpm.plot(title="bollinger bands of JPM", grid=True)
# ax.set_xlabel("Date")
# ax.set_ylabel("boolinger bands of JPM")
#
# plt.figure(0)
# plt.plot(jpmvals.index, jpm_norm )
# plt.savefig("jpm_norm.png")
# plt.show()
#
#
# plt.figure(1)
# plt.plot(jpmvals.index, bb_jpm )
# # plt.figure(1)
# # plt.show()
# plt.savefig("bollingerbands_jpm.png")
# plt.show()
#
# # plt.figure()
# sma_jpm = sma(jpmvals)
# # ax2 = sma_jpm.plot(title='price minus sma of JPM', grid=True)
# # ax2.set_xlabel("Date")
# # ax2.set_ylabel("price-sma of JPM")
# # # plt.figure(2)
# # # plt.show()
# # plt.savefig("sma_jpm.png")
# plt.figure(2)
# plt.plot(jpmvals.index, sma_jpm )
# plt.savefig("sma_jpm.png")
# plt.show()
#
#
#
# sma_jpm = pd.rolling_mean(jpm_norm, window=10)
# plt.figure(4)
# plt.plot(jpmvals.index, jpm_norm, jpmvals.index, sma_jpm )
# plt.savefig("sma_jpm.png")
# plt.show()
#
# plt.figure(5)
# plt.plot(jpmvals.index, jpm_norm, jpmvals.index, pd.rolling_mean(jpm_norm, window=10), jpmvals.index, pd.rolling_mean(jpm_norm, window=20)  )
# plt.savefig("smad2_jpm.png")
# plt.show()
#
