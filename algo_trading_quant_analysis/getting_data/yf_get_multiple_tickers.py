import yfinance as yf
import pandas as pd
from pathlib import Path  


stocks = ['AAPL',"AMZN","SPY","GOOG","META","TSLA"]
stocks_df = pd.DataFrame()

for stock in stocks:
    stock_df = yf.download(stock,period="1mo")
    filepath = Path(f"data/{stock}.csv")  
    filepath.parent.mkdir(parents=True, exist_ok=True)  
    stock_df.to_csv(filepath)  



