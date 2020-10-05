import matplotlib.pyplot as plt
import numpy as np
from math import *
add = 0
s = str(input("Enter function : "))
temp = s
rads = list(np.arange(-2*pi,2*pi,0.1))
s= s.replace('theta','(theta)')
f = lambda theta:eval(s)
ctr, x, y = -10*pi, [], []
fig = plt.figure(num = 'GPython')
fig.add_subplot(111, projection='polar')
for angle in rads:
        try:
                add = f(angle)
                x.append(angle)
                y.append(add)
                plt.polar(x,y)
        except:
                pass
#plt.polar(x,y)
plt.show()
plt.close()



