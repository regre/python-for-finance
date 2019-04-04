import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web


style.use('ggplot')
#
# start = dt.datetime(2014,1,1)
# end = dt.datetime(2018,12,31)
#
# df = web.DataReader('TSLA', 'iex', start, end)
# df.to_csv('tsla.csv')
df = pd.read_csv('tsla.csv', parse_dates=True, index_col=0)

# print(df.head())

print(df[['open','high']].tail())

df['close'].plot()
plt.show()
