import requests
import pandas as pd
def get_data(url,name,date):
    response = requests.get(url)
    # make csv from data
    with open("instruments.csv", "w") as file:
        file.write(response.text)
    df=pd.read_csv('instruments.csv')
    main_data=(df.loc[(df['name']==name) & (df['expiry']==date)])
    main_data.to_csv("maindata.csv")
    print(main_data)

url = "https://api.kite.trade/instruments"
name='NIFTY'
date="2023-03-29"
get_data(url,name,date)