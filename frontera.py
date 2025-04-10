import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import yfinance as yf
from datetime import datetime, timedelta
import riskfolio as rp
import warnings
warnings.filterwarnings('ignore')

#Parametros 
tickers = ['GGAL', 'YPF', 'BBAR', 'BMA','CEPU','CRESY','EDN','IRS','LOMA','PAM','SUPV','TEO','TGS','TS','TX']
start = datetime.now() - timedelta(days=10*365)
end = datetime.now()
df = yf.download(tickers, start, end)
returns = df['Close'].pct_change().dropna()

#Variables
method_mu ='hist'
method_cov = 'hist'
hist = True
model = 'Classic'
rm = 'MV'
obj = 'Sharpe'
rf = 0 #Tasa libre de riesgo
l = 0

#Optimizacion
port = rp.Portfolio(returns = returns)
port.assets_stats(method_mu=method_mu, method_cov=method_cov )
w = port.optimization(model=model, rm=rm , obj=obj , rf=rf , l=l , hist=hist)

#Plot Pie Chart
ax = rp.plot_pie(w, title='Portfolio Optimo Ponderacion', cmap = 'tab20')
plt.show()