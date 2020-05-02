import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
data=pd.read_excel('titanic3.xls')
#print(data)
print(data.shape)
#print(data.describe)
print(data.head())
data=data.drop(['sibsp','parch','ticket','fare','cabin','embarked','boat','body','home.dest',],axis=1)
print(data)
print(data.describe())
#data=data.fillna('00')
data=data.dropna(axis=0)
valeur_class=data['pclass'].value_counts()
print(valeur_class)
valeur_class.plot.bar()
data['age'].plot.bar()
plt.show()
data=data.set_index('name')
data.to_excel('test.xls')
mean=data.groupby(['sex','pclass']).mean()
a1=data['age']
print(mean)
print(a1)