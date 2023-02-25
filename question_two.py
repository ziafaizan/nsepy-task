
import requests
import pandas as pd
def get_data(url):

    response = requests.get(url)
    # make csv from data
    with open("instruments.csv", "w") as file:
        file.write(response.text)
    df=pd.read_csv('instruments.csv')
    # making excel sheet from csv file
    df.to_excel("instruments.xlsx", sheet_name='Sheet1', index=False)
    return df

def main(name,date,df):
    main_data=(df.loc[(df['name']==name) & (df['expiry']==date)])
    main_data.to_csv("maindata.csv")
    print(main_data)

url = "https://api.kite.trade/instruments"
name='NIFTY'
date="2023-03-29"
main(name,date,get_data(url))


"""The above approach takes alot of time so here is the second approch in which i have not exported to excel"""
