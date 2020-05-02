import matplotlib.pyplot as plt
import numpy as np
from pylab import *

a=200
lamda=633
N=2
D=1
list1=[]
list2=[]
k=0
x=100
x = np.linspace(-np.pi,np.pi,100)

print(np.pi)
for x in range(1,20):
    delta=2*a*x/D
    phi = 2 * pi * delta / lamda

    I1=(1/(N**2))
    I2=(sin(N*phi/2)**2)
    I3=(sin(phi/2)**2)
    I = I1 * I2 /I3
    list1.append(I)
plt.plot(list1)
plt.show()
N=2
for x in range(1,20):
    delta=2*a*x/D
    phi = 2 * pi * delta / lamda

    I1=(1/(N**2))
    I2=(sin(N*phi/2)**2)
    I3=(sin(phi/2)**2)
    I = I1 * I2 /I3
    list2.append(I)
plt.plot(list2)


plt.show()