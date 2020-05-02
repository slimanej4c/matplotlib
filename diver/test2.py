import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
from mpl_toolkits.mplot3d import axes3d
iris = load_iris()
x=iris.data
y=iris.target
name=list(iris.target_names)
print(name[0])

a=[[25,35,45],
  [26,37,49],
  [24,30,44],
  [24,30,44],
  [24,30,44],
  [24,30,44],
  [21,35,48],
  [29,31,49],
  [28,34,40],
  [29,36,45],
  [25,38,41],
  [29,39,49],
  [20,30,45]]
aa=np.array(a)
print('continent',aa.shape[0])
print('variable',aa.shape[1])
plt.scatter(aa[:,0],aa[:,1],c='green',alpha=0.5,s=10)

plt.show()
plt.hist(aa[:,0])
plt.hist(aa[:,1])
plt.show()
plt.hist2d(aa[:,0],aa[:,1],cmap='Blues')
plt.colorbar()
plt.show()

ax=plt.axes(projection='3d')
ax.scatter(aa[:,0],aa[:,1],aa[:,2])
plt.show()