from matplotlib.finance import quotes_historical_yahoo
from datetime import date
import pandas as pd
today = date.today()
start = (today.year-2, today.month, today.day)
quotes = quotes_historical_yahoo('MSFT', start, today)
# quotes = quotes_historical_yahoo('http://finance.yahoo.com/q/cp?s=^DJI', start, today)
attributes = ['date','open','close','high','low','volume']
quotesdf = pd.DataFrame(quotes, columns = attributes)

list1 = []
for i in range(0, len(quotes)):
    x = date.fromordinal(int(quotes[i][0]))
    y = date.strftime(x, '%Y/%m/%d')
    list1.append(y)
quotesdf.index = list1
quotesdf = quotesdf.drop(['date'], axis = 1)
#quotesdf['15/06/01':'15/12/31'][quotesdf.close> 49]
quotesdf.ix['15/01/30':'15/02/10',['open', 'close']]

p=quotesdf['15/01/01':'15/12/31'].sort_values(by='close', ascending=False)[:5]
#quotesdf['15/01/01':'15/12/31'].sort('close', ascending=True)[:5]
print p
quotesdf['15/1/1':'15/5/31'].sort_values(by='volume')

list1 = []
tmpdf = quotesdf['15/01/01':'15/12/31']
for i in range(0, len(tmpdf)):
    list1.append(int(tmpdf.index[i][3:5]))
tmpdf['month'] = list1
print tmpdf[ tmpdf.close > tmpdf.open]['month'].value_counts()

sorted = tmpdf.sort_values(by='close')
pd.concat([sorted[:5], sorted[len(tmpdf)-5:]])