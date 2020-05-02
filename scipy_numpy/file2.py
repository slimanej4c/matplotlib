import numpy as np

import matplotlib.pyplot as plt
from scipy import ndimage
image=plt.imread('bac.jpg')
image=image[:,:,0]
image2=image >55
#image2=image2 >120
#print(image2)
open_x=ndimage.binary_opening(image2)

plt.imshow(open_x)
plt.show()
label_image , n_label=ndimage.label(open_x)
print('here label',n_label)
plt.imshow(label_image)
plt.show()

size=ndimage.sum(open_x,label_image,range(n_label))
plt.scatter(range(n_label),size)
plt.show()
print(size)
#plt.imshow(image2)
#image3=np.copy(image)
#plt.hist(image3.ravel(),bins=255)
#print(image.shape)
#plt.show()


x=np.linspace(0,2,100)
y=1/3*x**3-3/5*x**2+2+np.random.randn(x.shape[0])/20

plt.scatter(x,y)
plt.plot(x,y)
plt.show()

def f(x,a,b,c,d):
    return a*x**3+b*x**2+c*x+d

from scipy import optimize

param,para_curve=optimize.curve_fit(f,x,y)
print(param)
plt.plot(x,f(x,param[0],param[1],param[2],param[3]),c='r')

#plt.show()

x=np.linspace(0,20,100)
y=x+4*np.sin(x)+np.random.randn(x.shape[0])

plt.plot(x,y)
from scipy import signal
new_y=signal.detrend(y)
plt.plot(x,new_y)
#plt.show()