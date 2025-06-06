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
df = yf.download(tickers, start, end,auto_adjust=False)
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

# Generate efficient frontier weights (you might need to adjust the number of points)
ws = port.efficient_frontier(model=model,points=100)

# Plot efficient frontier
label = 'Max Risk Adjusted Return Portfolio'
mu = port.mu
cov = port.cov

ax = rp.plot_frontier(w_frontier=ws,
                      mu=mu,
                      cov=cov,
                      returns=returns,
                      rm=rm,
                      rf=0,
                      alpha=0.05,
                      cmap='viridis',
                      w=w,
                      label=label,
                      marker='*',
                      s=16,
                      c='r',
                      height=6,
                      width=10,
                      t_factor=252,
                      ax=None)

plt.show()