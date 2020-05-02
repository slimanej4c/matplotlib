
import numpy as np
import matplotlib.pyplot as plt
from pylab import *

y=np.arange(12)
x1=(20-y)/2

plt.plot(y,x1)

x2=22-(2*y)

plt.plot(y,x2)

x3=12-y

plt.plot(y,x3)
plt.scatter(10,2,marker='+')
plt.show()
f=lambda x,y :300*x+200*y
x1,y=np.meshgrid(x1,y)
z1=f(x1,y)

plt.contourf(y,x1,z1,cmap='RdGy')
plt.colorbar()
#plt.show()
x2,y=np.meshgrid(x2,y)
z2=f(x2,y)

plt.contourf(y,x2,z2,cmap='RdGy')
plt.colorbar()
#plt.show()
x3,y=np.meshgrid(x3,y)
z3=f(x3,y)
plt.contourf(y,x3,z3,cmap='RdGy')
plt.colorbar()
#plt.show()

r=np.intersect1d(list(x1[0]),list(x2[0]),list(x3[0]))
print(r)
print(z1[0])
print(z2[0])
print(z3[0])
h=[7,9,]
f=lambda r,y :300*r+200*y
r1,y=np.meshgrid(r,y)
z4=f(r1,y)
print(z4[0])

