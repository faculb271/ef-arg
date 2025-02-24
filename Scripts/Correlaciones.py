import pandas as pd
import yfinance as yf
from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sns 

tickers = "XLY,XLP,XLE,XLF,XLV,XLRE,XLK,XLU"

start_date = "2025-01-01"
end_date = datetime.now()

df = yf.download(tickers, start_date,end_date)["Close"]

corr = df.corr()

plt.figure(figsize=(10, 8))
sns.heatmap(corr, annot=True, fmt=".2f", cmap="RdBu", linewidths=0.5, linecolor='white')
plt.title("Matriz de Correlación")
plt.tight_layout()

plt.show()