import numpy as np
import pandas
from pandas_datareader import data, wb
import pandas_datareader as pdr

def read_stock_data(stockcode, start_date, stop_date):
    return pdr.data.get_data_yahoo(stockcode, start_date, stop_date)

def get_stockcol_series(stockdata, col_name):
    return stockdata[col_name]

def get_stats(s, n=252):
    s.dropna()
    wins = len(s[s>0])
    losses = len(s[s<0])
    evens = len(s[s==0])
    mean_w = round(s[s>0].mean(), 3)
    mean_l = round(s[s<0].mean(), 3)
    win_r = round(wins / losses, 3)
    mean_trd = round(s.mean(), 3)
    sd = round(np.std(s), 3)
    max_l = round(s.min(), 3)
    max_w = round(s.max(), 3)
    sharpe_r = round((s.mean() / np.std(s)) * np.sqrt(n), 4)
    cnt = len(s)
    print('Trades:', cnt, \
          '\nWins:', wins, \
          '\nLosses:', losses, \
          '\nBreakeven:', evens, \
          '\nWin/Loss Ratio', win_r, \
          '\nMean Win:', mean_w, \
          '\nMean Loss:', mean_l, \
          '\nMean', mean_trd, \
          '\nStd Dev:', sd, \
          '\nMax Loss:', max_l, \
          '\nMax Win:', max_w, \
          '\nSharpe Ratio:', sharpe_r)






#print("hello world")