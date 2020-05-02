import numpy as np
import matplotlib.pyplot as pd
from sklearn.datasets import  make_regression
from sklearn.neighbors import KNeighborsClassifier
from sklearn import linear_model
x,y=make_regression(n_samples=100,n_features=1,noise=10)
x=np.array([1,2,3,4,5])
y=np.array([4,5,6,8,7])


model=linear_model.LinearRegression()
print(x.shape)
print(y.shape)
y=y.reshape(y.shape[0],1)
x=x.reshape(x.shape[0],1)
print(x.shape)
print(y.shape)
model.fit(x,y)

model.score(x,y)

prid=model.predict(x)

print(prid.shape)
pd.scatter(x,y)


#pd.scatter(x['ag,y)
print(x.shape , prid.shape)
pd.plot(x,prid , c='red')
pd.show()

def calc(model,xxx=10):
    xx=np.array(xxx).reshape(1,1)
    print(model.predict(xx))

calc(model)
