import matplotlib.pyplot as plt
import numpy as np
from pylab import *
list1=[]
list2=[]
N=2
a=200
lamda=633
N=2
D=1
x=2
delta=a*2*x/1
phi = 2 * pi * delta / lamda
#x=np.sin(y)
y = linspace(-phi, phi, 50)
yy= linspace(-phi, phi, 50)
I1=(1/(N**2))
I2=(sin(N*y/2)**2)
I3=(sin((y/2))**2)
z= (I1 * I2 /I3)*7



N=3
I1=(1/(N**2))
I2=(sin(N*yy/2)**2)
I3=(sin(yy/2)**2)
zz= (I1 * I2 /I3)*8

plt.subplot(121)
plt.plot(y,z)
plt.plot(yy,zz)

plt.subplot(122)

#plt.subplot(122)
plt.title('courbe pour  2 sources')

xx = z + 1j * z[:, np.newaxis]
plt.imshow(np.angle(xx), extent=[-50*phi, 50*phi, 0, 300 * np.pi], cmap='gray')
plt.show()

plt.subplot(121)
zzz=z+zz
plt.plot(yy,zzz)

plt.subplot(122)
xx = zzz + 1j * zzz[:, np.newaxis]
plt.imshow(np.angle(xx), extent=[-50*phi, 50*phi, 0, 300 * np.pi], cmap='gray')
plt.show()

from scipy import fftpack,signal

fourier=fftpack.fft(z)
freq=fftpack.fftfreq(z.size)
plt.plot(np.abs(freq),np.abs(fourier))
plt.show()
xx = fourier + 1j * fourier[:, np.newaxis]
plt.imshow(np.angle(xx), extent=[-50*phi, 50*phi, 0, 300 * np.pi], cmap='gray')
plt.show()

d1=signal.detrend(z)
plt.plot(yy,d1)
plt.show()

xx = d1+ 1j * d1[:, np.newaxis]
plt.imshow(np.angle(xx), extent=[-50*phi, 50*phi, 0, 300 * np.pi], cmap='gray')
plt.show()

d2=signal.detrend(zz)
plt.plot(yy,d2)
plt.show()