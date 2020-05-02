import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from mpl_toolkits.mplot3d import axes3d
f=lambda x,y :np.sin(x)+np.cos(x+y)



x=np.linspace(0,10,100)
y=np.linspace(0,10,100)
x,y=np.meshgrid(x,y)


z=f(x,y)
ax=plt.axes(projection='3d')
ax.plot_surface(x,y,z,cmap='plasma')
plt.show()






###############################################"


iris = load_iris()
x=iris.data
y=iris.target
name=list(iris.target_names)
print(name)

print(f'x contient {x.shape[0]} exemple et {x.shape[1]} variable')
for i in range(1,2):
  plt.scatter(x[:,0],x[:,i],c=y,alpha=0.5,s=x[:,2]*100)
  print(x[:, i])
plt.show()
xx =  x[:, 0]+ 1j * x[:, 0][:, np.newaxis]
plt.subplot(121)
plt.imshow(np.angle(xx), extent = [-500 * np.pi, 500* np.pi, 0, 300* np.pi], cmap = 'hsv')
plt.subplot(122)
xx =  x[:, 1]+ 1j * x[:, 1][:, np.newaxis]
plt.imshow(np.angle(xx), extent = [-500 * np.pi, 500* np.pi, 0, 300* np.pi], cmap = 'hsv')
#plt.show()
xx =  x[:, 2]+ 1j * x[:, 2][:, np.newaxis]
plt.imshow(np.angle(xx), extent = [-500 * np.pi, 500* np.pi, 0, 300* np.pi], cmap = 'hsv')
#plt.show()
xx =  x[:, 3]+ 1j * x[:, 3][:, np.newaxis]
plt.imshow(np.angle(xx), extent = [-500 * np.pi, 500* np.pi, 0, 300* np.pi], cmap = 'hsv')
#plt.show()
ax=plt.axes(projection='3d')
ax.scatter(x[:,0],x[:,1],x[:,2],c=y)
plt.show()
plt.hist(x[:,0])
plt.hist(x[:,1])
plt.show()
plt.hist2d(x[:,0],x[:,1],cmap='Blues')
plt.colorbar()
plt.show()

