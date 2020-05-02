import numpy as np
import matplotlib.pyplot as plt

img1 = np.zeros((20, 20))
print(img1)
#img1[4:-4, 4:-4] = 6
#img1[7:-7, 7:-7] = 9
#plt.plot(img1)
#plt.show()
ar=np.array([[0,0,0,0],[1,2,3,4],[1,2,3,4],[0,0,0,0]])

#ar[1:-1,:]=3
#ar[1:-1,1:-1]=2

print(ar[1:-1,:])
index1 = ar > 2
index2 = ar < 6
compound_index = index1 & index2
# The compound statement can alternatively be written as
compound_index1 = (ar > 3) & (ar < 7)
ar2 = np.copy(ar)
ar2[compound_index] = 9



plt.plot(ar2)

plt.show()