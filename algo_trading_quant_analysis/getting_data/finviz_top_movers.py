import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd


url = "https://finviz.com/"
headers = {"User-Agent" : "Chrome/107.0.5304.110"}
page = requests.get(url,headers=headers)
#print(page.status_code) Was successful after adding header
page_content = page.content
soup = BeautifulSoup(page_content,"html.parser")

def get_signals(signal):

    tabl = soup.find_all("table",{"id" :signal})
    columns = ["Ticker", "Last", "Change", "Volume", "Signal"]
    values = np.array([columns])

    for t in tabl:
        rows = t.find_all("tr",{"class":"table-light-row-cp"})
        for row in rows:
            x = row.get_text(separator=(",")).split(",")
            if '\n' in x:
                del x[6]
                del x[0] 
            x = np.array([x])
            values = np.concatenate((values, x))       
        df = pd.DataFrame(values, columns=values[0])
        df = df.iloc[1: , :]

    return df

            
def get_movers():
    #Positive news
    good = get_signals("signals_1")
    #Negative News
    bad = get_signals("signals_2")
    return pd.concat([good,bad],ignore_index=True)

print(get_movers())