from scipy import misc
import matplotlib.pyplot as plt
import numpy as np
face=misc.face()

h=face.shape[0]
w=face.shape[1]
z=face.shape[2]
l=[1,2]

#a=face[face<100]=1
zoom=face[:h//4,:w]
zoom=zoom[:,:,:]
plt.imshow(zoom)
plt.show()

#zoom=face[:-h//3,:-w//3]
face=misc.face(gray=True)
zoom2=face[h//4:,:w]
plt.imshow(zoom2)
plt.show()

#zoom22=face[::2]
#plt.imshow(zoom22)
#plt.show()




face=misc.face(gray=True)
h=face.shape[0]
w=face.shape[0]
l=[1,2]

#a=face[face<100]=1
zoom3=face[:h//4,:w]
#plt.imshow(zoom)
#plt.show()
#zoom=face[:-h//3,:-w//3]
zoom4=face[h//3:,:w]
#plt.imshow(zoom4)
#plt.show()

#plt.imshow(face,cmap=plt.cm.gray)

#plt.show()
print(zoom.shape)
print(zoom2.shape)

#g=np.concatenate((zoom,zoom2),axis=0)
#plt.imshow(g)
#plt.show()

