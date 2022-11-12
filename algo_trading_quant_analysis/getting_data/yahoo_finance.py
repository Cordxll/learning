
#How to get a single csv file of stock info via yf api.
import yfinance as yf
from pathlib import Path  
filepath = Path('yfiance_data/TSLA.csv')  
filepath.parent.mkdir(parents=True, exist_ok=True)  


data = yf.download("TSLA",period='6mo')
data.to_csv(filepath)  
