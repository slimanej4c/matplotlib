import pandas as pd
import  matplotlib.pyplot as plt

data=pd.read_csv('BTC.csv',index_col='Date',parse_dates=True)
print(data.head())
data['2019']['Close'].plot()

data['2019']['Close'].resample('W').mean().plot(label='la moyen par mois ',lw=1,ls=':',alpha=0.8)
data['2019']['Close'].resample('M').mean().plot(label='la moyen par mois ',lw=1,ls='--',alpha=0.8)
a=data['Close'].resample('W').mean().agg(['std','mean','min','max'])
print(a)
print(data.describe())
plt.show()
a['mean']['2019'].plot(label='mean de 2019')
plt.fill_between(a.index,a['max'],a['min'],alpha=0.2,label='min et max ')
plt.legend()
plt.show()
data=data.index
print(data)