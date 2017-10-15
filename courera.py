#from matplotlib.finance import quotes_historical_yahoo_ochl
from matplotlib.finance import quotes_historical_yahoo, candlestick

from datetime import date
today = date.today()
start = (today.year-2, today.month, today.day)
#quotes = quotes_historical_yahoo_ochl('http://finance.yahoo.com/q/cp?s=^DJI', start, today)
quotes = quotes_historical_yahoo('http://finance.yahoo.com/q/cp?s=^DJI', start, today)

