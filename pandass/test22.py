import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
data=pd.read_excel('titanic3.xls')
data=data.drop(['sibsp','parch','ticket','fare','cabin','embarked','boat','body','home.dest',],axis=1)
data=data.dropna(axis=0)
a1=data['age']
a2=data[data['age']>18].groupby(['sex','pclass']).mean()
a3=data.iloc[0:2,0:2]
a4=data.loc[0:2,['age']]
print(a1)
print(a2)
print(a3)
print(a4)