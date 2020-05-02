import numpy as np

k=np.array([1,2,3])
print(k.shape)
print(k.size)
t1=np.zeros((3,5))
t2=np.ones((3,5))
np.random.seed(0)
a=np.random.randn(3,5)
a=np.linspace(0,10,20,dtype=np.float16)
print(a)

s=np.hstack((t1,t2))
s=np.vstack((t1,t2))
s=np.concatenate((t1,t2),axis=1)
s=s.reshape(10,3)
print(s.ravel().shape)
r1=np.array([[[1,2,3],[4,5,6],[7,8,9]],[[1,2,3],[4,5,6],[7,8,9]],[[1,2,3],[4,5,6],[7,8,9]]])
print('r1',r1[:,0])
print('shape r1',r1[-1].shape)
r2=np.random.randint(0,10,[5,5])
r2[r2<5]=11

print('r2:',r2<5)
print('r2:',r2)

ni=np.array([[[1,1],[1,1]],[[1,1],[1,1]]])
print('ni shape',ni.shape)


aa=np.random.randint(1,4,[3,3])
print(aa.shape)
bb=np.concatenate((np.zeros((1,aa.shape[1])),aa),axis=0)
print(aa)
print(bb)