from scipy.misc import derivative
import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt
from numpy import *
from math import *
#X = np.arange(-10,10,0.01)
#x=X
s=input("Enter function : ")
temp = s
s = s.replace('x','(x)')
f = lambda x:eval(s)
x,y = [],[]
ctr = -10
while ctr <=10:
    x.append(ctr)
    try:
        y.append(derivative(f,ctr))
    except:
        y.append(None)
    ctr+=0.01
'''def F(x):
    res = np.zeros_like(x)
    for i,val in enumerate(x):
        try:
            y = derivative(f,val)
            res[i]=y
        except:
            res[i] = None
    return res'''
plt.figure(num ='GPYTHON')
plt.plot(x,y,label = 'y = '+temp,color = 'black')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('Derivative of '+temp)
#plt.style.use('ggplot')
ax = plt.gca()
plt.grid()
plt.legend(bbox_to_anchor=(1.1, 1.05))
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))
plt.show()
plt.close()
