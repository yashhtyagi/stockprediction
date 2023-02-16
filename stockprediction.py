import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader as data
import yfinance as yf

start = '2010-01-01'
end = '2019-12-31' 
df = yf.download('AAPL', start=start, end=end)
df = df.reset_index()
df = df.drop(['Date','Adj Close'], axis = 1)
plt.plot(df.Close)

plt.show()
print(df.head()) # remove print
print(df.tail()) # remove print