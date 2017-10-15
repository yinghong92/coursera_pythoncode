from matplotlib.finance import quotes_historical_yahoo_ochl
from datetime import date
from datetime import datetime
import pandas as pd
import xlwt
start = datetime(2014,10,1)
end = datetime(2014,10,31)
quotesINTC = quotes_historical_yahoo_ochl('INTC', start, end)
quotesGE = quotes_historical_yahoo_ochl('GE', start, end)
fields = ['date','open','close','high','low','volume']
#quotesdf = pd.DataFrame(quotes, columns = fields)
#quotesdf = pd.DataFrame(quotes, index = range(1,len(quotes)+1),columns = fields)
list1 = []
for i in range(0,len(quotesINTC)):
    x = date.fromordinal(int(quotesINTC[i][0]))
    y = datetime.strftime(x,'%Y-%m-%d')
    list1.append(y)
print list1

list2 = []
for i in range(0,len(quotesGE)):
    x = date.fromordinal(int(quotesGE[i][0]))
    y = datetime.strftime(x,'%Y-%m-%d')
    list2.append(y)
print list2

quotesdfINTC = pd.DataFrame(quotesINTC, index = list1, columns = fields)
quotesdfINTC = quotesdfINTC.drop(['date'], axis = 1)
quotesdfGE = pd.DataFrame(quotesGE, index = list1, columns = fields)
quotesdfGE = quotesdfGE.drop(['date'], axis = 1)
#print quotesdf

quotesdf = pd.DataFrame()
quotesdf['closeINTC'] = quotesdfINTC.close
quotesdf['closeGE'] = quotesdfGE.close
#quotesdf.plot(kind='bar')
#quotesdf.plot(kind='barh')
#quotesdf.plot(kind='scatter',x='closeINTC',color='g',y='closeGE')
quotesdf.plot(kind='kde')
plt.show()
#quotesdf.boxplot()
#quotesdfGE.close.plot()
quotesdf.to_excel('kkk.xls')