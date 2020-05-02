from math import *
import  matplotlib.pyplot as plt
import numpy as np


delta=200
lamda=633
N=0
D=0
list1=[]
list2=[]
k=0
list3=[]
im=1
a=0
for N in range(1,10):
    #list2.append(list1)
    #print('list22',list2)
    list1.clear()

    for delta in range(-317,317):
           if delta!=0:
               phi = 2 * pi * delta / lamda
               if phi%(2*pi)==0:
                   im=I=(1/(N**2))*((sin(N*phi/2)**2)/(sin(phi/2)**2))
                   print(im)
           I=(1/(N**2))*((sin(N*phi/2)**2)/(sin(phi/2)**2))*im
           k+=exp(I*N*phi)
           list1.append(I)
           list3.append(k)

    #x = np.linspace(0, 2 * np.pi, 10)

    #list5.append(list3)

    b = np.array(list1)

    a+=b
    #xx = a + 1j * a[:, np.newaxis]
    list2.append(list(b))
    plt.subplot(121)
    plt.plot(b)

c = np.array(list2)
plt.subplot(122)
plt.plot(a)
plt.show()
for N in range(1,10):
    c = np.array(list2)

    xx = c[:, N-1] + 1j * c[:, N-1][:, np.newaxis]
    plt.imshow(np.angle(xx), extent=[-500 * np.pi, 500 * np.pi, 0, 300 * np.pi], cmap='gray')
plt.show()

    #plt.subplot(121)
    #plt.plot(list1)


    #plt.subplot(122)
    #plt.imshow(np.angle(xx), extent = [-500 * np.pi, 500* np.pi, 0, 300* np.pi], cmap = 'gray')
#plt.imshow(np.abs(xx), extent = [-500 * np.pi, 500* np.pi, 0, 300* np.pi], cmap = 'hsv')
plt.show()
#c= np.array(list2)

#plt.show()
#b = np.array(list2)
#print('list2',list2)
#print(b.shape)

#xx = c[:,0] + 1j * c[:,0][:, np.newaxis]


#plt.imshow(np.angle(xx), extent = [-500 * np.pi, 500* np.pi, 0, 300* np.pi], cmap = 'gray')
# xxx= b[:,1] + 1j * b[:,1][:, np.newaxis]
#plt.imshow(np.angle(xxx), extent = [-500 * np.pi, 500* np.pi, 0, 300* np.pi], cmap = 'gray')
#plt.imshow(np.abs(xx), extent = [-500 * np.pi, 500* np.pi, 0, 300* np.pi], cmap = 'hsv')










