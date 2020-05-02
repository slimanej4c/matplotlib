from sklearn.neighbors import KNeighborsClassifier
import pandas as pd

import seaborn as sns

import numpy as np
import matplotlib.pyplot as plt

data=pd.read_excel('titanic3.xls')

data=data.drop(['name','sibsp','parch','ticket','fare','cabin','embarked','boat','body','home.dest',],axis=1)

data=data.dropna(axis=0)
data['sex'].replace(['female','male'],[1,0],inplace=True)
y=data['survived']
x=data.drop(['survived'],axis=1)
print(data.head())
model=KNeighborsClassifier()
model.fit(x,y)



model.score(x,y)
prid=model.predict(x)
plt.scatter(x['age'],y)
print(x.shape , prid.shape)
plt.scatter(x['age'],prid , c='red')
plt.show()
print(model.score(x,y))
print(prid)


def survied(model,pclass=3,sex=0,age=29):
    xx=np.array([pclass,sex,age]).reshape(1,3)
    if model.predict(xx)==0:
      print('you are dead')
survied(model)