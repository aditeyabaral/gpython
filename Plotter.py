import matplotlib.pyplot as plt
from math import *
add = 0
c = input("Is the function with respect to y or x: ")
s = str(input("Enter function : "))  # Inputs function
temp = s

if c == 'x':
        s = s.replace('x', '(x)')
        ctr, x, y = -10, [], []  # Setting counter to starting values and x,y to empty list
        while ctr <= 10:
                s1 = ''
                add = 0
                # Replaces variable with value at that point
                s1 = s.replace('x', str(ctr))
                try:
                        # Tries to evaluate function at that point, if defined
                        add = eval(s1)
                        x.append(add)
                        y.append(ctr)
                except:
                        pass  # If beyond domain, pass
                ctr += 0.1
        # print (x)
        # print (y)
        plt.figure(num='GPYTHON')
        plt.plot(x, y, label='y = '+temp, color='black')
        plt.xlabel('X Axis')
        plt.ylabel('Y Axis')
        # plt.title(temp.upper())
        # plt.style.use('ggplot')
        ax = plt.gca()
        plt.grid(True)
        plt.legend(bbox_to_anchor=(1.1, 1.05))
        ax.spines['right'].set_color('none')
        ax.spines['top'].set_color('none')
        ax.xaxis.set_ticks_position('bottom')
        ax.spines['bottom'].set_position(('data', 0))
        ax.yaxis.set_ticks_position('left')
        ax.spines['left'].set_position(('data', 0))
        plt.show()
        plt.close()

else:
        s = s.replace('y', '(y)')
        ctr, y, x = -10, [], [] #Setting counter to starting values and x,y to empty list
        while ctr<=10:
                s1 = ''
                add = 0
                s1 = s.replace('y',str(ctr)) #Replaces variable with value at that point
                try:
                        add = eval(s1) #Tries to evaluate function at that point, if defined
                        x.append(add)
                        y.append(ctr)
                except:
                        pass#If beyond domain, pass
                ctr+=0.1
        # print (x)
        # print (y)
        plt.figure(num ='GPYTHON')
        plt.plot(x,y,label = 'x = '+temp,color = 'red')
        plt.xlabel('X Axis')
        plt.ylabel('Y Axis')
        # plt.title(temp.upper())
        # plt.style.use('ggplot')
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




