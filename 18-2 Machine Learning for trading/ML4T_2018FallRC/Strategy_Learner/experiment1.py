import StrategyLearner as stl
import marketsimcode as msc
import indicators as indi
import datetime as dt

sl = stl.StrategyLearner(verbose=True)
symbol = 'JPM'
sl.addEvidence(symbol=symbol)
trades = sl.testPolicy(symbol=symbol,sd=dt.datetime(2008,1,1), ed=dt.datetime(2010,1,1))
slrv = msc.compute_portvals(trades, symbol=symbol)
print(slrv)
# dailyret = slrv/slrv.shift(1) -1
#
# sr= 252**(1/2.0) * (dailyret.mean()/  dailyret.std())
# print "std of daily ret"+dailyret.std()
# print "mean of daily ret"+dailyret.mean()


benchmark=trades.copy()
benchmark.ix[0, :]=1000
benchmark.ix[1:,:]=0

benchrv = msc.compute_portvals(benchmark, symbol=symbol)
print(benchrv)

