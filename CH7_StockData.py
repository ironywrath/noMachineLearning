import numpy
import pandas
from pandas_datareader import data, wb
import pandas_datareader as pdr

def read_stock_data(stockcode, start_date, stop_date):
    return pdr.data.get_data_yahoo(stockcode, start_date, stop_date)

def get_stockcol_series(stockdata, col_name):
    return stockdata[col_name]

def get_stats(s):
    

#print("hello world")