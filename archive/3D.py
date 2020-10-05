import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from math import *
import matplotlib.pyplot as plt
s = str(input("Enter function : "))
temp = s
t1,t2,t3 = s.find('x'),s.find('y'),s.find('z')
s= s.replace('x','(x)')
s =s.replace('y','(y)')
ctr1, ctr2, x, y, z = -10, -10, [], [],[]
while ctr1<=10:
     ctr2=-10
     while ctr2<=10:  
        s1 = ''
        add = 0
        s1 = s.replace('x',str(ctr1))
        s1 = s1.replace('y',str(ctr2))
        try:
                add = eval(s1)
                x.append(ctr1)
                y.append(ctr2)
                z.append(add)
        except:
                    pass
        ctr2+=0.1
     ctr1+=0.1
fig = plt.figure(num = 'GPYTHON')
ax = fig.gca(projection='3d')
ax.plot(x, y, z,label = 'z = '+temp)
ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')
ax.set_zlabel('Z Axis')
#plt.zlabel('z - axis')
plt.grid(True)
#add color = 'red' for colour in above line
ax.legend()
plt.show()

