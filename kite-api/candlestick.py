import pandas as pd
import numpy as np
import time
import os

while True:
    os.system('cls')
    data= pd.read_csv('stock.csv',parse_dates=True, index_col='date', names=['last_price', 'date'])
    # print(data)
    data = pd.DataFrame(data)
    ticks=data.loc[:,['last_price']]
    # print(data)
    data=data.resample('1min').ohlc().dropna()
    
    print(data)
    time.sleep(2)