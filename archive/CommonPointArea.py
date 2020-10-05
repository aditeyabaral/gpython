import matplotlib.pyplot as plt
from math import *
add = 0
global x1,x2,y1,y2
s1 = str(input("Enter function 1: "))
s2 = str(input("Enter function 2: "))
temp1, temp2 = s1,s2
s1= s1.replace('x','(x)')
s2= s2.replace('x','(x)')
f = lambda x: eval(s1)
g = lambda x: eval(s2)
ctr, x1, y1,x2,y2 = -10, [], [],[],[]
a1,a2 = [],[]
while ctr<=10:
        try:
                add1 = f(ctr)
                x1.append(ctr)
                y1.append(add1)
                point = [ctr,add1]
                a1.append(point)
                
        except:
            pass
        try:
            add2 = g(ctr)
            x2.append(ctr)
            y2.append(add2)
            point = [ctr,add2]
            a2.append(point)
        except:
                pass
        ctr+=1
a3 = []
for i in a1:
        if i in a2:
                a3.append(i)
nx,ny = [],[]
for i in a3:
        nx.append(i[0])
beg = nx[0]
x1,y1,x2,y2 = [],[],[],[]
for i in nx[1:]:
        ctr = beg
        add1,add2 = 0,0
        while ctr<=i:
                try:
                        add1 = f(ctr)
                        x1.append(ctr)
                        y1.append(add1)
                except:
                        pass
                try:
                        add2 = g(ctr)
                        x2.append(ctr)
                        y2.append(add2)
                except:
                        pass
                ctr+=0.01
        beg = i
plt.figure(num ='GPYTHON')
plt.plot(x1,y1,label = 'y = '+temp1,color = 'blue')
plt.plot(x2,y2,label = 'y = '+temp2,color = 'red')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
ax = plt.gca()
plt.grid(True)
plt.legend(bbox_to_anchor=(1.1, 1.05))
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))
plt.show()
plt.close()



