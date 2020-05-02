import numpy as np
import matplotlib.pyplot as pd
from sklearn.datasets import  make_regression

x,y=make_regression(n_samples=100,n_features=1,noise=10)
pd.scatter(x,y)

print(x.shape)

y=y.reshape(y.shape[0],1)
print(y.shape)
#creation matrice qui va jouer le role de le GRANDE X
X=np.hstack((x,np.ones(x.shape)))
print(X)
# creation une theta parzard

theta=np.random.randn(2,1)
print('theta',theta)

# on faire un fonction pour faire le facteur entre X*thata

def model(X,theta):
    return X.dot(theta)
pd.plot(x,model(X,theta))
pd.show()

def cost_fonction(X,y,theta):
    m=len(y)
    return 1/(2*m)*np.sum((model(X,theta)-y)**2)

print('le cout',cost_fonction(X,y,theta))
def grad(X,y ,theta):
    m=len(y)
    return 1/m*X.T.dot(model(X,theta)-y)
#apprentisage'
def gradien_descent(X,y,theta,learning_rate,n_interation):
    cost_history=np.zeros(n_interation)#pour voir le figure de dégradation des valeur pour minimiser la foction
    for i in range(0,n_interation):
        theta=theta-learning_rate*grad(X,y,theta)
        cost_history[i]=cost_fonction(X,y,theta)

    return theta,cost_history

theta_final,cost_history=gradien_descent(X,y,theta,learning_rate=0.01,n_interation=400)
print(theta_final)
pridiction=model(X,theta_final)

pd.scatter(x,y)
pd.plot(x,pridiction)
pd.show()
# courbe de apprentissage vous adaier a détecter alpha learning-rate

pd.plot(range(400),cost_history)
pd.show()

# coefficient de determination
def coef_determination(y,pred):
    u=((y-pred)**2).sum()
    v=((y-y.mean())**2).sum()
    return 1-u/v

print(coef_determination(y,pridiction))

from sklearn.linear_model import LinearRegression

mode=LinearRegression()
mode.fit(x,y)
mode.score(x,y)
prid=mode.predict(x)
pd.scatter(x,y)
pd.plot(x,prid)
pd.show()
print('prid',prid)
print('score',mode.score(x,y))

