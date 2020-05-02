import numpy as np
import matplotlib.pyplot as plt

a=np.random.randint(0,10,[3,2])
b=np.random.randint(0,10,[3,])
b=b.reshape(b.shape[0],1)
print(a)
#print(a+2)
print(b)
print(b.std(axis=0))
#print(a+b)
plt.plot(a,b)
plt.show()


