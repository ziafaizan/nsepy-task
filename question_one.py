from nsepy import get_history
from datetime import date
import matplotlib.pyplot as plt
import pandas as pd
stock_list = ['SBIN', 'ASIANPAINT', 'AXISBANK']
table_value=pd.DataFrame()

# Q-1
def get_data(stock_list):
    for x in stock_list:
        stock_data=get_history(symbol=x,
                   start=date(2015,1,1),
                   end=date(2015,1,10))
        print(stock_data)
        stock_data.to_csv(x+".csv")
        stock_data[['Close']].plot()
        plt.title(x) 


def make_table(stock_list):
    for i in stock_list:
        data=pd.read_csv(i+".csv")
        table_value['Date']=data['Date']
        table_value[i]=data['Close']
        table_value.to_csv('table_value.csv',index=False)
        print(table_value)
# get_data get all the data using nsepy library
get_data(stock_list)
# make_table make table value and make csv for it using pandas 
make_table(stock_list)
plt.show()
