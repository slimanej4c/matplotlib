import numpy as np
#from numpy.linalg import inv
import matplotlib.pyplot as plt
from scipy import stats
from scipy.stats import iqr
from scipy.interpolate import interp1d ,interp2d
x=np.linspace(0,10,10)
y=x**2
plt.scatter(x,y)
f=interp1d(x,y,kind='linear')
print('f',f(x))
new_x=np.linspace(0,10,30)
result=f(new_x)
plt.scatter(new_x,result,c='r')
plt.show()

x=np.linspace(0,10,10)
y=np.sin(x)
plt.scatter(x,y)
f=interp1d(x,y,kind='cubic')
new_x=np.linspace(0,10,30)
result=f(new_x)
#x=np.linspace(0,10,30)
#y=np.sin(x)
plt.scatter(new_x,result,c='r')
plt.show()

couleur=np.array(['blue','maron','vert','noir'])
valeur=np.array([[4,3,5,4],[10,5,8,1],[10,0,7,4]])
tvaleur=valeur.T

moyen=np.mean(tvaleur)
vmoyen=np.median(valeur,axis=0)
print(couleur)
print(tvaleur)
#print(moyen)
#print(vmoyen)

a=stats.mode(valeur,axis=0)
b=stats.mode(valeur,axis=1)
#print(a)
#print(b)
e=np.percentile(tvaleur,99,axis=1, interpolation='lower') #diviser les valur parprt a cent on faira un barama on est coiser  percentage
ee=np.percentile(tvaleur,2,axis=1, interpolation='lower')
#print(e)
#print(ee)

f=iqr(tvaleur, axis=0 , rng=(34, 75), interpolation='lower')#mada sur un baram
#print(f)

standard_diviation = np.std(tvaleur,axis=1)
print(standard_diviation)


c=np.ptp(tvaleur,axis=1)
d=np.ptp(tvaleur,axis=0)
#print(c)
plt.plot(couleur,tvaleur)
#plt.plot(couleur,vmoyen)
plt.plot(couleur,standard_diviation)
#plt.plot(couleur,c)
plt.legend(['class1','class2','class3','standard diviation'])

#plt.show()
print(b)