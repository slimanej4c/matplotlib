from numpy import *
import numpy as np
from scipy.interpolate import *
from matplotlib.pyplot import *


x=array([0,1,2,3,4,5])
y=array([0,0.8,0.9,0.1,-0.8,-1])
p1=polyfit(x,y,1)
print(p1)
plot(x,y,'o')
plot(polyval(p1,x))
show()

